
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

    # Fonts
    title_font = pygame.font.SysFont("arial", 21, bold=True)
    label_font = pygame.font.SysFont("arial", 11, bold=True)
    value_font = pygame.font.SysFont("arial", 17, bold=True)
    control_font = pygame.font.SysFont("arial", 11)

    # Theme colours
    panel_color = COLORS["target"]
    primary = COLORS["good"]
    secondary = "#94A3B8"
    divider_color = "#263653"

    # Background
    surface.fill(panel_color, (0, 0, BOARD_WIDTH, HUD_HEIGHT))

    # Title
    title = title_font.render("CELL ARCHITECT", True, primary)
    surface.blit(title, (14, 9))

    # Running / paused status
    status = "RUNNING" if is_running else "PAUSED"
    status_color = primary if is_running else COLORS["warning"]

    pygame.draw.circle(
        surface,
        status_color,
        (22, 48),
        4,
    )

    status_text = control_font.render(
        status,
        True,
        status_color,
    )
    surface.blit(status_text, (33, 42))

    # Statistics
    stats = [
        ("GENERATION", f"{generation:03}"),
        ("POPULATION", f"{population:03}"),
        ("SPEED", f"{speed} gen/s"),
    ]

    stat_positions = [
        (270, 7),
        (405, 7),
        (540, 7),
    ]

    for (label, value), (x, y) in zip(stats, stat_positions):

        label_surface = label_font.render(
            label,
            True,
            secondary,
        )

        value_surface = value_font.render(
            value,
            True,
            primary,
        )

        surface.blit(label_surface, (x, y))
        surface.blit(value_surface, (x, y + 20))

    # Vertical separators
    for x in (255, 390, 525):
        pygame.draw.line(
            surface,
            divider_color,
            (x, 9),
            (x, 43),
            1,
        )

    # Keyboard shortcuts
    controls = (
        "SPACE: Play/Pause   "
        "N: Step   "
        "R: Reset   "
        "UP/DOWN: Speed   "
        "C: Clear cells   "
        "W: Clear walls"
    )

    controls_surface = control_font.render(
        controls,
        True,
        secondary,
    )

    surface.blit(controls_surface, (14, 56))
