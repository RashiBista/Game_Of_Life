
"""Main entry point for Cell Architect."""

import pygame

from game.config import (
    GAME_TITLE,
    BOARD_WIDTH,
    BOARD_HEIGHT,
    HUD_HEIGHT,
    DEFAULT_FPS,
    MIN_FPS,
    MAX_FPS,
    RENDER_FPS,
)

from game.interface.board import draw_board, pixel_to_cell
from game.interface.hud import draw_hud
from game.engine.simulation import life_step


def main() -> None:
    pygame.init()

    # --------------------------------------------------
    # 1. CREATE GAME WINDOW
    # --------------------------------------------------

    window_height = BOARD_HEIGHT + HUD_HEIGHT

    screen = pygame.display.set_mode(
        (BOARD_WIDTH, window_height)
    )

    pygame.display.set_caption(GAME_TITLE)

    clock = pygame.time.Clock()

    # Separate drawing surface for the board.
    board_surface = screen.subsurface(
        (0, HUD_HEIGHT, BOARD_WIDTH, BOARD_HEIGHT)
    )

    # --------------------------------------------------
    # 2. GAME STATE
    # --------------------------------------------------

    live_cells: set[tuple[int, int]] = set()
    walls: set[tuple[int, int]] = set()

    # Tracks how many generations each living cell has survived.
    cell_ages: dict[tuple[int, int], int] = {}

    generation = 0
    speed = DEFAULT_FPS
    is_running = False

    last_generation_time = pygame.time.get_ticks()

    # --------------------------------------------------
    # 3. MOUSE BRUSH STATE
    # --------------------------------------------------

    paint_button = None
    paint_value = None

    # Prevents repeatedly modifying the same cell in one stroke.
    visited_cells: set[tuple[int, int]] = set()

    # --------------------------------------------------
    # 4. CELL PAINTING
    # --------------------------------------------------

    def paint_cell(cell: tuple[int, int]) -> None:
        """Apply the active mouse brush to a cell."""

        if cell in visited_cells:
            return

        visited_cells.add(cell)

        # LEFT CLICK: living-cell brush.
        if paint_button == 1:

            # Walls cannot contain living cells.
            if cell in walls:
                return

            if paint_value:
                live_cells.add(cell)
                cell_ages.setdefault(cell, 0)

            else:
                live_cells.discard(cell)
                cell_ages.pop(cell, None)

        # RIGHT CLICK: wall brush.
        elif paint_button == 3:

            if paint_value:
                live_cells.discard(cell)
                cell_ages.pop(cell, None)

                walls.add(cell)

            else:
                walls.discard(cell)

    # --------------------------------------------------
    # 5. COORDINATE CONVERSION
    # --------------------------------------------------

    def get_board_cell(
        position: tuple[int, int],
    ) -> tuple[int, int] | None:
        """Convert window coordinates into board coordinates."""

        x, y = position

        # Ignore the HUD area.
        if y < HUD_HEIGHT:
            return None

        board_position = (
            x,
            y - HUD_HEIGHT,
        )

        return pixel_to_cell(board_position)

    # --------------------------------------------------
    # 6. SIMULATION UPDATE
    # --------------------------------------------------

    def advance_generation() -> None:
        """Calculate the next generation and update cell ages."""

        nonlocal live_cells, generation

        # Calculate the next generation using Conway's rules.
        next_cells = life_step(live_cells, walls)

        next_ages = {}

        for cell in next_cells:

            if cell in live_cells:
                # Existing cell survived.
                next_ages[cell] = cell_ages.get(cell, 0) + 1

            else:
                # Newly born cell.
                next_ages[cell] = 0

        # Update the game state.
        live_cells = next_cells

        cell_ages.clear()
        cell_ages.update(next_ages)

        generation += 1

    # --------------------------------------------------
    # 7. MAIN GAME LOOP
    # --------------------------------------------------

    def main_loop() -> None:

        nonlocal generation
        nonlocal speed
        nonlocal is_running
        nonlocal last_generation_time
        nonlocal paint_button
        nonlocal paint_value

        running = True

        while running:

            # ------------------------------------------
            # HANDLE EVENTS
            # ------------------------------------------

            for event in pygame.event.get():

                # Close window.
                if event.type == pygame.QUIT:
                    running = False

                # --------------------------------------
                # MOUSE BUTTON PRESSED
                # --------------------------------------

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button not in (1, 3):
                        continue

                    cell = get_board_cell(event.pos)

                    if cell is None:
                        continue

                    paint_button = event.button

                    visited_cells.clear()

                    # Determine whether this stroke paints or erases.
                    if paint_button == 1:
                        paint_value = cell not in live_cells

                    else:
                        paint_value = cell not in walls

                    paint_cell(cell)

                # --------------------------------------
                # MOUSE MOVEMENT / DRAGGING
                # --------------------------------------

                elif event.type == pygame.MOUSEMOTION:

                    if paint_button is None:
                        continue

                    buttons = event.buttons

                    # Check that the corresponding mouse button
                    # is still held down.
                    if paint_button == 1 and not buttons[0]:
                        continue

                    if paint_button == 3 and not buttons[2]:
                        continue

                    cell = get_board_cell(event.pos)

                    if cell is not None:
                        paint_cell(cell)

                # --------------------------------------
                # MOUSE BUTTON RELEASED
                # --------------------------------------

                elif event.type == pygame.MOUSEBUTTONUP:

                    if event.button == paint_button:

                        paint_button = None
                        paint_value = None

                        visited_cells.clear()

                # --------------------------------------
                # KEYBOARD INPUT
                # --------------------------------------

                elif event.type == pygame.KEYDOWN:

                    # PLAY / PAUSE.
                    if event.key == pygame.K_SPACE:

                        is_running = not is_running

                        last_generation_time = pygame.time.get_ticks()

                    # STEP: advance one generation.
                    elif event.key == pygame.K_n:

                        is_running = False
                        advance_generation()

                    # RESET: clear cells and generation.
                    # Walls are preserved.
                    elif event.key == pygame.K_r:

                        is_running = False

                        live_cells.clear()
                        cell_ages.clear()

                        generation = 0

                        last_generation_time = pygame.time.get_ticks()

                    # INCREASE SPEED.
                    elif event.key == pygame.K_UP:

                        speed = min(MAX_FPS, speed + 1)

                    # DECREASE SPEED.
                    elif event.key == pygame.K_DOWN:

                        speed = max(MIN_FPS, speed - 1)

                    # CLEAR LIVING CELLS.
                    elif event.key == pygame.K_c:

                        live_cells.clear()
                        cell_ages.clear()

                    # CLEAR WALLS.
                    elif event.key == pygame.K_w:

                        walls.clear()

            # ------------------------------------------
            # AUTOMATIC SIMULATION
            # ------------------------------------------

            current_time = pygame.time.get_ticks()

            generation_interval = 1000 / speed

            if (
                is_running
                and current_time - last_generation_time
                >= generation_interval
            ):

                advance_generation()

                last_generation_time = current_time

            # ------------------------------------------
            # DRAW BOARD
            # ------------------------------------------

            draw_board(
                board_surface,
                live_cells,
                walls,
                cell_ages,
            )

            # ------------------------------------------
            # DRAW INFORMATION PANEL
            # ------------------------------------------

            draw_hud(
                screen,
                generation,
                len(live_cells),
                speed,
                is_running,
            )

            # ------------------------------------------
            # UPDATE DISPLAY
            # ------------------------------------------

            pygame.display.flip()

            clock.tick(RENDER_FPS)

        pygame.quit()

    # Start the game.
    main_loop()


if __name__ == "__main__":
    main()
