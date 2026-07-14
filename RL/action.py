"""
action.py
Defines the action space for the
QCL Reinforcement Learning module.
"""
from enum import IntEnum
from typing import Union


class Action(IntEnum):
    """
    Action space for RL.
    The agent changes one operating
    parameter at a time.
    """
    # Current
    INCREASE_CURRENT = 0
    DECREASE_CURRENT = 1
    # Voltage
    INCREASE_VOLTAGE = 2
    DECREASE_VOLTAGE = 3
    # Temperature
    INCREASE_TEMPERATURE = 4
    DECREASE_TEMPERATURE = 5
    # Cascade Stages
    INCREASE_STAGE = 6
    DECREASE_STAGE = 7
    # No operation
    HOLD = 8


ACTION_NAMES = {
    Action.INCREASE_CURRENT: "Increase Current",
    Action.DECREASE_CURRENT: "Decrease Current",
    Action.INCREASE_VOLTAGE: "Increase Voltage",
    Action.DECREASE_VOLTAGE: "Decrease Voltage",
    Action.INCREASE_TEMPERATURE: "Increase Temperature",
    Action.DECREASE_TEMPERATURE: "Decrease Temperature",
    Action.INCREASE_STAGE: "Increase Cascade Stage",
    Action.DECREASE_STAGE: "Decrease Cascade Stage",
    Action.HOLD: "Hold",
}


def get_action_name(action: Union[int, Action]) -> str:
    """
    Return human-readable action name.

    Args:
        action: An Action enum member, or an int
            corresponding to a valid Action value.

    Returns:
        The human-readable string for the action.

    Raises:
        ValueError: If `action` is an int that does not
            correspond to a valid Action.
        TypeError: If `action` is neither an int nor an Action.
    """
    if isinstance(action, Action):
        return ACTION_NAMES[action]

    if isinstance(action, int):
        try:
            return ACTION_NAMES[Action(action)]
        except ValueError as exc:
            raise ValueError(
                f"{action} is not a valid Action value "
                f"(expected 0-{len(Action) - 1})."
            ) from exc

    raise TypeError(
        f"action must be an int or Action, got {type(action).__name__}."
    )


def number_of_actions() -> int:
    """
    Total number of actions.
    """
    return len(Action)