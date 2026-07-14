"""
Simple file utilities.
"""

from pathlib import Path


def create_directory(path):
    Path(path).mkdir(
        parents=True,
        exist_ok=True
    )


def file_exists(path):
    return Path(path).exists()


def delete_file(path):

    path = Path(path)

    if path.exists():
        path.unlink()