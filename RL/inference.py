"""
inference.py
Inference for Tabular Q-Learning agent (QCL RL module)
"""
import argparse
import os
import sys

import numpy as np

from RL.agent import QLearningAgent
from environment import QCLPhysicsEnv


def run_inference(
    model_path: str = "models/q_table.pkl",
    episodes: int = 5,
    max_steps: int = 500,
    render: bool = True,
) -> dict:
    """
    Run greedy (no-exploration) inference using a trained Q-table.

    Parameters
    ----------
    model_path : str
        Path to the saved Q-table/agent state.
    episodes : int
        Number of episodes to run. Must be >= 1.
    max_steps : int
        Safety cap on steps per episode, in case the environment
        never naturally reaches `done` for some state (e.g. the
        agent oscillates between two states it thinks are optimal).
    render : bool
        Whether to call env.render() after each step.

    Returns
    -------
    dict
        Summary stats: episode rewards, steps taken, and whether
        each episode ended naturally or was cut off.
    """
    if episodes < 1:
        raise ValueError("episodes must be >= 1.")
    if max_steps < 1:
        raise ValueError("max_steps must be >= 1.")
    if not os.path.isfile(model_path):
        raise FileNotFoundError(
            f"No trained model found at '{model_path}'. "
            f"Train an agent first or check the path."
        )

    env = QCLPhysicsEnv()

    try:
        agent = QLearningAgent(
            state_size=env.state_size,
            action_size=env.action_size,
        )

        try:
            agent.load(model_path)
        except Exception as exc:
            raise RuntimeError(
                f"Failed to load model from '{model_path}': {exc}"
            ) from exc

        # Force greedy mode - no exploration during inference
        agent.epsilon = 0.0

        rewards = []
        steps_per_episode = []
        completed_episodes = 0

        for ep in range(episodes):
            state = env.reset()
            done = False
            total_reward = 0.0
            steps = 0

            print(f"\nEpisode {ep + 1} started")

            while not done and steps < max_steps:
                action = agent.predict(state)
                next_state, reward, done, info = env.step(action)
                total_reward += reward
                state = next_state
                steps += 1

                if render:
                    env.render()

            if not done:
                print(
                    f"Episode {ep + 1} did not terminate naturally; "
                    f"cut off after {max_steps} steps."
                )
            else:
                completed_episodes += 1

            print(f"Episode {ep + 1} Reward: {total_reward:.4f} ({steps} steps)")
            rewards.append(total_reward)
            steps_per_episode.append(steps)

        results = {
            "episodes": episodes,
            "completed_episodes": completed_episodes,
            "episode_rewards": rewards,
            "steps_per_episode": steps_per_episode,
            "average_reward": float(np.mean(rewards)),
            "average_steps": float(np.mean(steps_per_episode)),
        }

        print("\n=== INFERENCE COMPLETE ===")
        print(f"Completed episodes : {completed_episodes}/{episodes}")
        print(f"Average Reward     : {results['average_reward']:.4f}")
        print(f"Average Steps      : {results['average_steps']:.2f}")

        return results

    finally:
        # Release any resources (renderer, sim handles, etc.) if
        # the environment defines a close() method.
        if hasattr(env, "close"):
            env.close()


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run QCL RL inference.")
    parser.add_argument(
        "--model-path",
        type=str,
        default="models/q_table.pkl",
        help="Path to the trained Q-table file.",
    )
    parser.add_argument(
        "--episodes",
        type=int,
        default=5,
        help="Number of evaluation episodes to run.",
    )
    parser.add_argument(
        "--max-steps",
        type=int,
        default=500,
        help="Maximum steps allowed per episode.",
    )
    parser.add_argument(
        "--no-render",
        action="store_true",
        help="Disable environment rendering during inference.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    try:
        run_inference(
            model_path=args.model_path,
            episodes=args.episodes,
            max_steps=args.max_steps,
            render=not args.no_render,
        )
    except (FileNotFoundError, RuntimeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)