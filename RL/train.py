"""
train.py
Training script for the QCL Reinforcement Learning module.
"""
import argparse
import os
import sys
from typing import Optional

from RL.agent import QLearningAgent
from RL.environment import QCLPhysicsEnv
from RL.hyperparameters import (
    NUM_EPISODES,
    MAX_STEPS,
    LEARNING_RATE,
    DISCOUNT_FACTOR,
    EPSILON,
    EPSILON_DECAY,
    EPSILON_MIN,
)


def train(
    num_episodes: int = NUM_EPISODES,
    max_steps: int = MAX_STEPS,
    model_path: str = "models/q_table.pkl",
    seed: Optional[int] = None,
    print_every: int = 10,
) -> dict:
    """
    Train a QLearningAgent on QCLPhysicsEnv and save the result.

    Returns a dictionary containing training statistics and
    learning curves for Streamlit visualization. If training is
    interrupted (KeyboardInterrupt) or fails partway through (any
    other exception, e.g. from the environment's physics), the
    model and whatever episodes did complete are still saved and
    returned, with "completed": False and an "error" message, so
    a caller like a Streamlit dashboard can still show a partial
    learning curve instead of losing everything.
    """

    if num_episodes < 1:
        raise ValueError("num_episodes must be >= 1.")

    if max_steps < 1:
        raise ValueError("max_steps must be >= 1.")

    os.makedirs(os.path.dirname(model_path) or ".", exist_ok=True)

    env = QCLPhysicsEnv(seed=seed)

    agent = QLearningAgent(
        state_size=env.state_size,
        action_size=env.action_size,
        learning_rate=LEARNING_RATE,
        discount_factor=DISCOUNT_FACTOR,
        epsilon=EPSILON,
        epsilon_decay=EPSILON_DECAY,
        epsilon_min=EPSILON_MIN,
        seed=seed,
    )

    # ============================
    # Training History
    # ============================

    episode_rewards = []
    epsilon_history = []

    best_reward = None

    completed = True
    error_message = None

    try:

        for episode in range(num_episodes):

            state = env.reset()

            total_reward = 0.0

            for step in range(max_steps):

                action = agent.choose_action(state)

                next_state, reward, done, _ = env.step(action)

                agent.learn(
                    state,
                    action,
                    reward,
                    next_state,
                    done,
                )

                state = next_state

                total_reward += reward

                if done:
                    break

            # Update epsilon
            agent.decay_epsilon()

            # Save history
            episode_rewards.append(total_reward)
            epsilon_history.append(agent.epsilon)

            if best_reward is None or total_reward > best_reward:
                best_reward = total_reward

            if (episode + 1) % print_every == 0 or episode == num_episodes - 1:

                recent = episode_rewards[-print_every:]

                avg_recent = sum(recent) / len(recent)

                print(
                    f"Episode {episode + 1}/{num_episodes} | "
                    f"Reward = {total_reward:.2f} | "
                    f"Average = {avg_recent:.2f} | "
                    f"Epsilon = {agent.epsilon:.3f}"
                )

    except KeyboardInterrupt:

        print("\nTraining interrupted by user.")
        completed = False
        error_message = "Training interrupted by user."

    except Exception as exc:  # noqa: BLE001 - deliberately broad: see docstring

        print(f"\nTraining stopped early due to an error: {exc}")
        completed = False
        error_message = str(exc)

    finally:

        agent.save(model_path)

        print(f"Model saved to: {model_path}")

        if hasattr(env, "close"):
            env.close()

    if len(episode_rewards) == 0:

        return {
            "episodes": 0,
            "rewards": [],
            "epsilon_history": [],
            "completed": completed,
            "error": error_message,
        }

    results = {

        "episodes": len(episode_rewards),

        "average_reward": sum(episode_rewards) / len(episode_rewards),

        "best_reward": best_reward,

        "final_epsilon": agent.epsilon,

        # -------- Added for Streamlit --------
        "rewards": episode_rewards,

        "epsilon_history": epsilon_history,

        "completed": completed,

        "error": error_message,
    }

    if completed:
        print("\nTraining completed successfully.")
    else:
        print("\nTraining finished with warnings.")
        if error_message:
            print(f"Reason: {error_message}")

    print(f"Episodes        : {results['episodes']}")
    print(f"Average Reward  : {results['average_reward']:.2f}")
    print(f"Best Reward     : {results['best_reward']:.2f}")
    print(f"Final Epsilon   : {results['final_epsilon']:.3f}")

    return results


def parse_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        description="Train the QCL RL Agent."
    )

    parser.add_argument(
        "--episodes",
        type=int,
        default=NUM_EPISODES,
    )

    parser.add_argument(
        "--max-steps",
        type=int,
        default=MAX_STEPS,
    )

    parser.add_argument(
        "--model-path",
        type=str,
        default="models/q_table.pkl",
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=None,
    )

    parser.add_argument(
        "--print-every",
        type=int,
        default=10,
    )

    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()

    try:

        train(
            num_episodes=args.episodes,
            max_steps=args.max_steps,
            model_path=args.model_path,
            seed=args.seed,
            print_every=args.print_every,
        )

    except ValueError as exc:

        print(f"Error: {exc}", file=sys.stderr)

        sys.exit(1)

