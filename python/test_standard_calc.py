from itertools import chain

from standard_calc import bound_to_180, is_angle_between

"""Floating-point math on computers does not have infinite precision."""


def assert_floats_close_enough(a, b):
    assert abs(a - b) < 10**-8


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0


def test_bound_all_nonwrapped_integers():
    for x in range(-180, 180):  # 180 is not included in the bounded interval.
        assert bound_to_180(x) == x


def test_bound_first_bottom_edge():
    assert_floats_close_enough(
        bound_to_180(-180.001),
        179.999
    )

    assert_floats_close_enough(
        bound_to_180(-180),
        -180
    )

    assert_floats_close_enough(
        bound_to_180(-179.999),
        -179.999
    )


def test_bound_first_top_edge():
    assert_floats_close_enough(
        bound_to_180(179.999),
        179.999
    )

    assert_floats_close_enough(
        bound_to_180(180),
        -180
    )

    assert_floats_close_enough(
        bound_to_180(180.001),
        -179.999
    )


def test_bound_large_angles_around_1800_degrees():
    assert_floats_close_enough(
        bound_to_180(-1800.001),
        -0.001
    )

    assert_floats_close_enough(
        bound_to_180(-1800),
        0
    )

    assert_floats_close_enough(
        bound_to_180(-1799.999),
        0.001
    )

    assert_floats_close_enough(
        bound_to_180(1799.999),
        -0.001
    )

    assert_floats_close_enough(
        bound_to_180(1800),
        0
    )

    assert_floats_close_enough(
        bound_to_180(1800.001),
        0.001
    )



""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)


def test_between_basic1_reversed_bounds():
    assert is_angle_between(2, 1, 0)


def test_between_angles_same():
    FIRST = 50
    SECOND = 50

    for x in (49.999, 50, 50.001):
        assert not is_angle_between(FIRST, x, SECOND)

def test_between_angles_180_apart():
    FIRST = -20
    SECOND = 160

    for x in (-20.001, -20, -19.999, 179.999, 180, 180.001):
        assert not is_angle_between(FIRST, x, SECOND)

def test_between_integers_in_simple_angle():
    FIRST = -20
    SECOND = 90

    for x in chain(range(-180, -19), range(90, 180)):
        assert not is_angle_between(FIRST, x, SECOND)

    for x in range(21, 90):
        assert is_angle_between(FIRST, x, SECOND)

def test_between_integers_in_single_wrapping_angle():
    FIRST = 150
    SECOND = 225

    for x in chain(range(0, 151), range(225, 360)):
        assert not is_angle_between(FIRST, x, SECOND)

    for x in range(151, 224):
        assert is_angle_between(FIRST, x, SECOND)

def test_between_multi_wrapping_angles():
    FIRST = 325
    SECOND = -460

    for x in chain(
        range(-500, -460),
        range(-395, -99),
        range(-35, 261),
        range(325, 401)
    ):
        assert not is_angle_between(FIRST, x, SECOND)

    for x in chain(
        range(-459, -395),
        range(-99, -35),
        range(261, 325)
    ):
        assert is_angle_between(FIRST, x, SECOND)

def test_between_precision():
    FIRST = -20.5
    SECOND = 90.5

    for x in (-20.501, -20.5, 90.5, 90.501):
        assert not is_angle_between(FIRST, x, SECOND)

    for x in (-20.499, 90.499):
        assert is_angle_between(FIRST, x, SECOND)
