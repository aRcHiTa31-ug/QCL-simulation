"""
evaluate.py
Evaluate a trained RL agent
for the QCL Simulator.
"""
from typing import Optional

import numpy as np


def evaluate_agent(
    environment,
    agent,
    episodes: int = 10,
    max_steps: int = 200,
    verbose: bool = False,
) -> dict:
    """
    Evaluate a trained agent with exploration disabled.

    Parameters
    ----------
    environment : Environment
        RL environment. Must implement reset() -> state and
        step(action) -> (next_state, reward, done, info).
    agent : QLearningAgent
        Trained RL agent. Must implement predict(state) -> action
        and expose an `epsilon` attribute.
    episodes : int
        Number of evaluation episodes. Must be >= 1.
    max_steps : int
        Maximum steps per episode. Must be >= 1.
    verbose : bool
        If True, print per-episode reward as evaluation proceeds.

    Returns
    -------
    dict
        Evaluation statistics, including per-episode rewards,
        step counts, and how many episodes terminated naturally
        (done=True) vs. were cut off by max_steps.
    """
    if episodes < 1:
        raise ValueError("episodes must be >= 1.")
    if max_steps < 1:
        raise ValueError("max_steps must be >= 1.")
    if not hasattr(agent, "epsilon"):
        raise AttributeError("agent must expose an 'epsilon' attribute.")

    rewards = []
    steps_per_episode = []
    completed_episodes = 0

    # Disable exploration for evaluation, restoring it afterward
    # even if evaluation raises partway through.
    old_epsilon = agent.epsilon
    agent.epsilon = 0.0
    try:
        for episode in range(episodes):
            state = environment.reset()
            total_reward = 0.0
            done = False
            steps = 0

            while not done and steps < max_steps:
                action = agent.predict(state)
                next_state, reward, done, _ = environment.step(action)
                total_reward += reward
                state = next_state
                steps += 1

            rewards.append(total_reward)
            steps_per_episode.append(steps)
            if done:
                completed_episodes += 1

            if verbose:
                status = "done" if done else "cut off"
                print(
                    f"Episode {episode + 1}/{episodes}: "
                    f"reward={total_reward:.3f}, steps={steps} ({status})"
                )
    finally:
        # Always restore exploration rate, even on error.
        agent.epsilon = old_epsilon

    rewards_arr = np.array(rewards, dtype=float)
    results = {
        "episodes": episodes,
        "episode_rewards": rewards,
        "steps_per_episode": steps_per_episode,
        "average_steps": float(np.mean(steps_per_episode)),
        "completed_episodes": completed_episodes,
        "average_reward": float(np.mean(rewards_arr)),
        "maximum_reward": float(np.max(rewards_arr)),
        "minimum_reward": float(np.min(rewards_arr)),
        "reward_std": float(np.std(rewards_arr)),
    }
    return results


def print_evaluation(results: dict) -> None:
    """
    Print evaluation statistics.
    """
    required_keys = (
        "episodes",
        "average_reward",
        "maximum_reward",
        "minimum_reward",
        "reward_std",
    )
    missing = [k for k in required_keys if k not in results]
    if missing:
        raise KeyError(f"results is missing expected key(s): {missing}")

    print("\n========== RL Evaluation ==========")
    print(f"Episodes         : {results['episodes']}")
    if "completed_episodes" in results:
        print(f"Completed        : {results['completed_episodes']}/{results['episodes']}")
    if "average_steps" in results:
        print(f"Average Steps    : {results['average_steps']:.2f}")
    print(f"Average Reward   : {results['average_reward']:.3f}")
    print(f"Maximum Reward   : {results['maximum_reward']:.3f}")
    print(f"Minimum Reward   : {results['minimum_reward']:.3f}")
    print(f"Reward Std Dev   : {results['reward_std']:.3f}")
    print("===================================\n")