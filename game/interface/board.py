
"""Drawing and coordinate conversion for the game board."""

import pygame

from game.config import (
    ROWS,
    COLS,
    CELL_SIZE,
    COLORS,
)


def draw_board(
    surface: pygame.Surface,
    live: set[tuple[int, int]],
    walls: set[tuple[int, int]],
) -> None:
    """Draw the board, live cells, walls and grid."""

    # 1. Draw the empty board background.
    surface.fill(COLORS["background"])

    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            pygame.draw.rect(
                surface,
                COLORS["empty"],
                (x + 1, y + 1, CELL_SIZE - 1, CELL_SIZE - 1),
            )

    # 2. Draw walls.
    for row, col in walls:
        pygame.draw.rect(
            surface,
            COLORS["wall"],
            (
                col * CELL_SIZE + 1,
                row * CELL_SIZE + 1,
                CELL_SIZE - 1,
                CELL_SIZE - 1,
            ),
        )

    # 3. Draw living cells.
    for row, col in live:
        pygame.draw.rect(
            surface,
            COLORS["build"],
            (
                col * CELL_SIZE + 1,
                row * CELL_SIZE + 1,
                CELL_SIZE - 1,
                CELL_SIZE - 1,
            ),
        )

    # 4. Draw grid lines.
    for col in range(COLS + 1):
        x = col * CELL_SIZE
        pygame.draw.line(
            surface,
            COLORS["grid"],
            (x, 0),
            (x, ROWS * CELL_SIZE),
        )

    for row in range(ROWS + 1):
        y = row * CELL_SIZE
        pygame.draw.line(
            surface,
            COLORS["grid"],
            (0, y),
            (COLS * CELL_SIZE, y),
        )


def pixel_to_cell(
    position: tuple[int, int],
) -> tuple[int, int] | None:
    """Convert a screen pixel position into a board coordinate."""

    x, y = position

    if x < 0 or y < 0:
        return None

    col = x // CELL_SIZE
    row = y // CELL_SIZE

    if row >= ROWS or col >= COLS:
        return None

    return row, col
