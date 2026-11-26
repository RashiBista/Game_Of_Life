
"""Central configuration for Cell Architect."""

# Board dimensions
ROWS = 24
COLS = 40
CELL_SIZE = 20

BOARD_WIDTH = COLS * CELL_SIZE
BOARD_HEIGHT = ROWS * CELL_SIZE

# Original game's colour palette
COLORS = {
    "background": "#bc92cd",
    "empty": "#844cad",
    "grid": "#4e7ab1",
    "build": "#3c2c59",
    "target": "#0f153a",
    "wall": "#195699",
    "gold": "#0b1c3b",
    "pink": "#7a4ba8",
    "warning": "#ceb5d4",
    "good": "#f6d48f",
}

# Age-based cell colours
AGE_COLORS = [
    "#f2e199",
    "#ecb44d",
    "#d5a25e",
    "#c2a368",
    "#f6941d",
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
