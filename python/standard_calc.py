def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """

    reoriented = angle + 180
    bounded = reoriented % 360 # fortunately for us python supports modulus on floating point numbers
    oriented_back = bounded - 180

    # -180 is only valid backwards angle
    if oriented_back == 180:
        return -180
    else:
        return oriented_back


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """

    first_angle_normalized = bound_to_180(first_angle)
    middle_angle_normalized = bound_to_180(middle_angle)
    second_angle_normalized = bound_to_180(second_angle)

    smaller_bound = min(first_angle_normalized, second_angle_normalized)
    bigger_bound = max(first_angle_normalized, second_angle_normalized)

    if bigger_bound - smaller_bound < 180:
        return smaller_bound < middle_angle_normalized and middle_angle_normalized < bigger_bound
    elif bigger_bound - smaller_bound > 180:
        return middle_angle_normalized < smaller_bound or bigger_bound < middle_angle_normalized
    else:
        # the bounds are exactly 180 degrees apart, so there is no well defined reflex arc/minor arc
        return False