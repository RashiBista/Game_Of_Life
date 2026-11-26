
"""Main entry point for Cell Architect."""

import pygame

from game.config import (
    GAME_TITLE,
    BOARD_WIDTH,
    BOARD_HEIGHT,
    DEFAULT_FPS,
)
from game.interface.board import draw_board, pixel_to_cell
from game.engine.simulation import life_step


def main() -> None:
    pygame.init()

    # Create the game window.
    screen = pygame.display.set_mode(
        (BOARD_WIDTH, BOARD_HEIGHT)
    )
    pygame.display.set_caption(GAME_TITLE)

    clock = pygame.time.Clock()

    # Game state.
    live_cells: set[tuple[int, int]] = set()
    walls: set[tuple[int, int]] = set()

    running = True

    while running:

        # Handle user input.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                cell = pixel_to_cell(event.pos)

                if cell is None:
                    continue

                # Left click: add/remove a living cell.
                if event.button == 1:
                    if cell in walls:
                        continue

                    if cell in live_cells:
                        live_cells.remove(cell)
                    else:
                        live_cells.add(cell)

                # Right click: add/remove a wall.
                elif event.button == 3:
                    if cell in walls:
                        walls.remove(cell)
                    else:
                        live_cells.discard(cell)
                        walls.add(cell)

            # Space: advance one generation.
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    live_cells = life_step(
                        live_cells,
                        walls,
                    )

                # C: clear living cells.
                elif event.key == pygame.K_c:
                    live_cells.clear()

                # W: clear walls.
                elif event.key == pygame.K_w:
                    walls.clear()

        # Draw everything.
        draw_board(screen, live_cells, walls)

        pygame.display.flip()

        clock.tick(DEFAULT_FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
