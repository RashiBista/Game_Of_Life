
"""Information panel for Cell Architect."""

import pygame

from game.config import COLORS, BOARD_WIDTH, HUD_HEIGHT


def draw_hud(
    surface: pygame.Surface,
    generation: int,
    population: int,
    speed: int,
    is_running: bool,
) -> None:
    """Display simulation information and keyboard controls."""

    surface.fill(COLORS["target"], (0, 0, BOARD_WIDTH, HUD_HEIGHT))

    title_font = pygame.font.SysFont("arial", 22, bold=True)
    info_font = pygame.font.SysFont("arial", 15)

    title = title_font.render("CELL ARCHITECT", True, COLORS["good"])

    status = "RUNNING" if is_running else "PAUSED"
    status_color = COLORS["good"] if is_running else COLORS["warning"]

    status_text = info_font.render(
        f"{status}  |  Generation: {generation}  |  "
        f"Population: {population}  |  Speed: {speed} gen/s",
        True,
        status_color,
    )

    controls = info_font.render(
        "SPACE: Play/Pause   N: Step   R: Reset   "
        "UP/DOWN: Speed   C: Clear cells   W: Clear walls",
        True,
        COLORS["warning"],
    )

    surface.blit(title, (10, 5))
    surface.blit(status_text, (230, 10))
    surface.blit(controls, (10, 43))
