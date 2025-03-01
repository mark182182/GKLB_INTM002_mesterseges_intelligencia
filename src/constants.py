import pathlib


ASSETS_PATH = pathlib.Path(__file__).parent / "assets"

SCREEN_HEIGHT: int = 600
SCREEN_WIDTH: int = 800

CELL_HEIGHT: float = SCREEN_HEIGHT / (1 << 6)
CELL_WIDTH: float = SCREEN_WIDTH / (1 << 6)

SPRITE_SIZE: int = 16