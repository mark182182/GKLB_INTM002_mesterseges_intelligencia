import pygame
from dataclasses import dataclass, field


@dataclass
class Position:
    x: float
    y: float

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Cell:
    # image: pygame.Surface
    is_wall: bool = field(default=True)


@dataclass
class Player:
    cell: Cell


@dataclass
class Grid:
    start_position: Position = Position(0, 0)
    end_position: Position = Position(0, 0)
    cells_by_position: dict[Position, Cell] = field(default_factory=dict)
    """
    Stores the cells of the grid and their positions by x, y coordinates.
    """


@dataclass
class Map:
    grid: Grid
