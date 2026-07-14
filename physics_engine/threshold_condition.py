"""
physics/threshold_condition.py

Laser Threshold Condition
"""


def threshold_condition(

    modal_gain,

    mirror_loss,

    internal_loss

):
    """
    Threshold Condition

    Γg >= αm + αi
    """

    return modal_gain >= (

        mirror_loss

        + internal_loss

    )


def threshold_margin(

    modal_gain,

    mirror_loss,

    internal_loss

):
    """
    Threshold Margin
    """

    return (

        modal_gain

        -

        (

            mirror_loss

            +

            internal_loss

        )

    )


if __name__ == "__main__":

    print(

        threshold_condition(

            15,

            8,

            4

        )

    )

    print(

        threshold_margin(

            15,

            8,

            4

        )

    )