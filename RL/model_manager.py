"""
model_manager.py
Handles saving, loading, and versioning of RL models
(Q-Learning / DQN) for the QCL Simulator project.
"""
import os
import pickle
import re
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple


class ModelManager:
    """
    Generic model manager for RL agents.
    Supports:
    - Saving models with timestamped versioning
    - Loading the latest or a specific checkpoint
    - Listing and deleting saved models
    """

    _TIMESTAMP_FMT = "%Y%m%d_%H%M%S"
    _FILENAME_RE = re.compile(r"^(?P<name>.+)_(?P<timestamp>\d{8}_\d{6})\.pkl$")

    def __init__(self, save_dir: str = "models"):
        self.save_dir = save_dir
        os.makedirs(self.save_dir, exist_ok=True)

    # -----------------------------
    # Path safety helpers
    # -----------------------------
    def _safe_path(self, filename: str) -> str:
        """
        Resolve `filename` inside save_dir and guard against path
        traversal (e.g. filename="../../etc/passwd") or absolute
        paths that would otherwise escape save_dir.
        """
        candidate = os.path.normpath(os.path.join(self.save_dir, filename))
        save_dir_abs = os.path.abspath(self.save_dir)
        candidate_abs = os.path.abspath(candidate)
        if os.path.commonpath([save_dir_abs, candidate_abs]) != save_dir_abs:
            raise ValueError(
                f"'{filename}' resolves outside of the managed "
                f"save directory '{self.save_dir}'."
            )
        return candidate

    @staticmethod
    def _validate_name(name: str) -> None:
        if not name or os.sep in name or (os.altsep and os.altsep in name):
            raise ValueError(
                f"Invalid model name '{name}': must be non-empty and "
                f"must not contain path separators."
            )

    # -----------------------------
    # Save model
    # -----------------------------
    def save(self, model: Any, name: str, metadata: Optional[Dict] = None) -> str:
        """
        Save RL model with timestamp versioning.

        Returns the full path the model was saved to.
        """
        self._validate_name(name)

        timestamp = datetime.now().strftime(self._TIMESTAMP_FMT)
        filename = f"{name}_{timestamp}.pkl"
        file_path = self._safe_path(filename)

        if os.path.exists(file_path):
            # Extremely unlikely (same name + same second), but silently
            # overwriting a checkpoint would be a nasty way to lose a
            # trained model. Disambiguate instead.
            counter = 1
            while os.path.exists(file_path):
                filename = f"{name}_{timestamp}_{counter}.pkl"
                file_path = self._safe_path(filename)
                counter += 1

        package = {
            "model": model,
            "metadata": metadata or {},
            "timestamp": timestamp,
        }

        # Write to a temp file first and rename, so a crash mid-save
        # can't leave a corrupted/truncated .pkl behind.
        tmp_path = file_path + ".tmp"
        try:
            with open(tmp_path, "wb") as f:
                pickle.dump(package, f)
            os.replace(tmp_path, file_path)
        except Exception:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
            raise

        print(f"[ModelManager] Model saved at: {file_path}")
        return file_path

    # -----------------------------
    # Internal: find + sort checkpoints for a name
    # -----------------------------
    def _matching_checkpoints(self, name: str) -> List[Tuple[str, str]]:
        """
        Return (filename, timestamp) pairs for all checkpoints that
        match `name` exactly (not just as a string prefix), sorted
        oldest -> newest by timestamp.
        """
        matches = []
        for f in os.listdir(self.save_dir):
            m = self._FILENAME_RE.match(f)
            if m and m.group("name") == name:
                matches.append((f, m.group("timestamp")))

        # Sort by parsed timestamp value, not lexicographic filename,
        # so this is correct even if a counter suffix was appended.
        matches.sort(key=lambda pair: datetime.strptime(pair[1], self._TIMESTAMP_FMT))
        return matches

    # -----------------------------
    # Load latest model
    # -----------------------------
    def load_latest(self, name: str) -> Tuple[Any, Dict]:
        """
        Load the latest saved model with the given exact name.
        """
        self._validate_name(name)
        matches = self._matching_checkpoints(name)
        if not matches:
            raise FileNotFoundError(f"No saved models found for: {name}")

        latest_file, _ = matches[-1]
        return self.load(latest_file)

    # -----------------------------
    # Load specific file
    # -----------------------------
    def load(self, file_path: str) -> Tuple[Any, Dict]:
        """
        Load a model. Accepts either a bare filename inside
        save_dir, or a full path.
        """
        # If it's a bare filename, resolve it safely inside save_dir.
        # If it's already an existing path (e.g. returned by save()),
        # use it as-is.
        resolved_path = file_path if os.path.isabs(file_path) or os.path.exists(file_path) \
            else self._safe_path(file_path)

        if not os.path.isfile(resolved_path):
            raise FileNotFoundError(f"No such model file: {resolved_path}")

        try:
            with open(resolved_path, "rb") as f:
                package = pickle.load(f)
        except (pickle.UnpicklingError, EOFError) as exc:
            raise RuntimeError(
                f"Failed to load model from '{resolved_path}': "
                f"file appears corrupted or is not a valid checkpoint."
            ) from exc

        if not isinstance(package, dict) or "model" not in package:
            raise ValueError(
                f"'{resolved_path}' does not look like a ModelManager "
                f"checkpoint (missing 'model' key)."
            )

        print(f"[ModelManager] Loaded model from: {resolved_path}")
        return package["model"], package.get("metadata", {})

    # -----------------------------
    # List all models
    # -----------------------------
    def list_models(self, name: Optional[str] = None) -> List[str]:
        """
        List all saved model filenames, most recent first.
        If `name` is given, only checkpoints for that exact name
        are returned.
        """
        if name is not None:
            return [f for f, _ in reversed(self._matching_checkpoints(name))]

        files = [f for f in os.listdir(self.save_dir) if f.endswith(".pkl")]
        # Sort by file modification time, most recent first, so the
        # ordering is meaningful even for filenames that don't match
        # the standard "<name>_<timestamp>.pkl" pattern.
        files.sort(
            key=lambda f: os.path.getmtime(os.path.join(self.save_dir, f)),
            reverse=True,
        )
        return files

    # -----------------------------
    # Delete model
    # -----------------------------
    def delete_model(self, filename: str) -> bool:
        """
        Delete a saved model file by filename (inside save_dir).

        Returns True if a file was deleted, False if it didn't exist.
        """
        file_path = self._safe_path(filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"[ModelManager] Deleted: {file_path}")
            return True

        print(f"[ModelManager] File not found: {filename}")
        return False