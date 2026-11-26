
"""Reusable pattern definitions for Conway's Game of Life."""

from game.engine.simulation import Coordinate


# Still lifes
BLOCK = {
    (0, 0), (0, 1),
    (1, 0), (1, 1),
}


# Oscillators
BLINKER = {
    (0, 0), (0, 1), (0, 2),
}

TOAD = {
    (0, 1), (0, 2), (0, 3),
    (1, 0), (1, 1), (1, 2),
}


# Spaceships
GLIDER = {
    (0, 1),
    (1, 2),
    (2, 0), (2, 1), (2, 2),
}


# Methuselahs
R_PENTOMINO = {
    (0, 1), (0, 2),
    (1, 0), (1, 1),
    (2, 1),
}

ACORN = {
    (0, 1),
    (1, 3),
    (2, 0), (2, 1), (2, 4), (2, 5), (2, 6),
}


def shift_pattern(
    pattern: set[Coordinate],
    row_offset: int,
    col_offset: int,
) -> set[Coordinate]:
    """Return a copy of a pattern moved to a new position."""
    return {
        (row + row_offset, col + col_offset)
        for row, col in pattern
    }


def rotate_pattern(
    pattern: set[Coordinate],
) -> set[Coordinate]:
    """Rotate a pattern 90 degrees clockwise around its origin."""
    return {
        (col, -row)
        for row, col in pattern
    }

def normalize_pattern(
    pattern: set[Coordinate],
) -> set[Coordinate]:
    """Move a pattern so its minimum row and column are both zero."""
    if not pattern:
        return set()

    min_row = min(row for row, _ in pattern)
    min_col = min(col for _, col in pattern)

    return {
        (row - min_row, col - min_col)
        for row, col in pattern
    }


def pattern_dimensions(
    pattern: set[Coordinate],
) -> tuple[int, int]:
    """Return the pattern's height and width."""
    if not pattern:
        return (0, 0)

    height = max(row for row, _ in pattern) - min(
        row for row, _ in pattern
    ) + 1

    width = max(col for _, col in pattern) - min(
        col for _, col in pattern
    ) + 1

    return (height, width)
