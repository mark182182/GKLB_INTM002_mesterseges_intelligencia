import pathlib


ASSETS_PATH: pathlib.Path = pathlib.Path(__file__).parent / "assets"

TILESET_SPRITE_PATH: pathlib.Path = ASSETS_PATH / "tileset.png"

SCREEN_HEIGHT: int = 768
SCREEN_WIDTH: int = 768

CELL_HEIGHT: float = SCREEN_HEIGHT / (1 << 5)
CELL_WIDTH: float = SCREEN_WIDTH / (1 << 5)

SPRITE_SIZE: int = 16
CARVE_LIMIT: int = 256

DIRECTIONS: list[tuple[int, int]] = [
    (0, -int(CELL_HEIGHT)),
    (int(CELL_WIDTH), 0),
    (0, int(CELL_HEIGHT)),
    (-int(CELL_WIDTH), 0),
]
