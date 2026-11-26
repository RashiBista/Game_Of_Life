
"""Central configuration for Cell Architect."""

# Board dimensions
ROWS = 24
COLS = 40
CELL_SIZE = 20

BOARD_WIDTH = COLS * CELL_SIZE
BOARD_HEIGHT = ROWS * CELL_SIZE

# Original game's colour palette

COLORS = {
    "background": "#24305d",
    "empty": "#111A2E",
    "grid": "#263653",
    "build": "#1E293B",
    "target": "#70568A",
    "wall": "#F59E0B",
    "gold": "#FBBF24",
    "pink": "#63376A",
    "warning": "#c9c6d9",
    "good": "#f7f4ff",
}

AGE_COLORS = [
    "#B8F7D4",
    "#63E6BE",
    "#38BDF8",
    "#818CF8",
    "#f1edf7",
]


# Simulation defaults
DEFAULT_FPS = 10
MIN_FPS = 1
MAX_FPS = 30

# Game information
GAME_TITLE = "Cell Architect"
TOTAL_CAMPAIGN_LEVELS = 10

# Window and interface
HUD_HEIGHT = 70
RENDER_FPS = 60

# Simulation Speed -generation per sec
DEFAULT_FPS = 5
MIN_FPS = 1
MAX_FPS = 30
