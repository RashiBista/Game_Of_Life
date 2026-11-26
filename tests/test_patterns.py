
from game.engine.patterns import (
    BLOCK,
    BLINKER,
    TOAD,
    GLIDER,
    R_PENTOMINO,
    ACORN,
    shift_pattern,
    rotate_pattern,
)


def test_pattern_sizes():
    assert len(BLOCK) == 4
    assert len(BLINKER) == 3
    assert len(TOAD) == 6
    assert len(GLIDER) == 5
    assert len(R_PENTOMINO) == 5
    assert len(ACORN) == 7


def test_shift_pattern():
    shifted = shift_pattern(BLOCK, 5, 10)

    assert shifted == {
        (5, 10), (5, 11),
        (6, 10), (6, 11),
    }


def test_shift_does_not_modify_original():
    original = BLOCK.copy()

    shift_pattern(BLOCK, 5, 10)

    assert BLOCK == original


def test_rotate_pattern():
    rotated = rotate_pattern(BLINKER)

    assert rotated == {
        (0, 0), (1, 0), (2, 0),
    }


def test_rotating_four_times_returns_original():
    rotated = BLINKER

    for _ in range(4):
        rotated = rotate_pattern(rotated)

    assert rotated == BLINKER
