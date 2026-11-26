
"""Core Conway's Game of Life simulation.

This module is independent of Pygame and the user interface.
"""

from collections import Counter

Coordinate = tuple[int, int]

DEFAULT_ROWS = 24
DEFAULT_COLS = 40


def _validate_positions(
    positions: set[Coordinate],
    rows: int,
    cols: int,
    name: str,
) -> None:
    """Ensure every coordinate is inside the board."""
    for row, col in positions:
        if not (0 <= row < rows and 0 <= col < cols):
            raise ValueError(
                f"{name} coordinate {(row, col)} is outside "
                f"the {rows}x{cols} board."
            )


def count_neighbors(
    cell: Coordinate,
    live: set[Coordinate],
) -> int:
    """Count the eight neighbouring positions containing live cells."""
    row, col = cell

    return sum(
        (row + dr, col + dc) in live
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if dr != 0 or dc != 0
    )


def life_step(
    live: set[Coordinate],
    walls: set[Coordinate] | None = None,
    rows: int = DEFAULT_ROWS,
    cols: int = DEFAULT_COLS,
) -> set[Coordinate]:
    """Calculate the next generation using Conway's rules.

    Rules:
    1. A live cell with fewer than 2 neighbours dies.
    2. A live cell with 2 or 3 neighbours survives.
    3. A live cell with more than 3 neighbours dies.
    4. A dead cell with exactly 3 neighbours becomes alive.

    Walls are blocked positions, not additional biological rules.
    Cells cannot occupy walls, but walls do not affect neighbouring cells.
    The board has finite boundaries and does not wrap around.
    """
    if rows <= 0 or cols <= 0:
        raise ValueError("Board dimensions must be positive.")

    live = set(live)
    walls = set(walls) if walls is not None else set()

    _validate_positions(live, rows, cols, "Live cell")
    _validate_positions(walls, rows, cols, "Wall")

    if live & walls:
        raise ValueError("A position cannot contain both a live cell and a wall.")

    neighbour_counts: Counter[Coordinate] = Counter()

    # Count the neighbours of every live cell.
    for row, col in live:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue

                neighbour = (row + dr, col + dc)
                nr, nc = neighbour

                # Ignore positions outside the board and wall positions.
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                if neighbour in walls:
                    continue

                neighbour_counts[neighbour] += 1

    next_generation = set()

    for cell, neighbours in neighbour_counts.items():
        if cell in live:
            if neighbours in (2, 3):
                next_generation.add(cell)
        elif neighbours == 3:
            next_generation.add(cell)

    return next_generation
