import pygame
from constants import ASSETS_PATH, SCREEN_HEIGHT, SCREEN_WIDTH, CELL_HEIGHT, CELL_WIDTH
from models import Position, Cell, Player, Grid, Map
from images import ImageId, ImageLoader
import random as rnd
from random import randint, random

from sprite import Spritesheet


def manhattan_distance(a: Position, b: Position) -> int:
    return int(abs(a.x - b.x) + abs(a.y - b.y))


def generate_maze_with_branches(
    images_by_id: dict[ImageId, pygame.Surface], grid: Grid, carve_limit: int
):
    """
    Carves out up to 'carve_limit' cells in the grid using a DFS-based approach
    that can branch. Also sets grid.start_position and grid.end_position.
    """
    # 1) Mark every cell as a wall
    for pos, cell in grid.cells_by_position.items():
        cell.is_wall = True

    # 2) Pick a random start cell
    all_positions = list(grid.cells_by_position.keys())
    start = rnd.choice(all_positions)
    grid.cells_by_position[start].is_wall = False
    stack = [start]
    carved_count = 1

    # Save the start in the grid so we can draw it
    grid.start_position = start

    directions = [
        (0, -int(CELL_HEIGHT)),
        (int(CELL_WIDTH), 0),
        (0, int(CELL_HEIGHT)),
        (-int(CELL_WIDTH), 0),
    ]

    # 3) DFS loop, carve until we reach carve_limit or run out of neighbors
    while stack and carved_count < carve_limit:
        current = stack[-1]
        neighbors: list[Position] = []
        for dx, dy in directions:
            nxt = Position(current.x + dx, current.y + dy)
            if nxt in grid.cells_by_position and grid.cells_by_position[nxt].is_wall:
                neighbors.append(nxt)

        if neighbors and carved_count < carve_limit:
            chosen: Position = rnd.choice(neighbors)

            # Carve chosen
            grid.cells_by_position[chosen].is_wall = False
            if carved_count == 1:
                grid.cells_by_position[chosen].image = images_by_id[ImageId.START_IMAGE]
            else:    
                grid.cells_by_position[chosen].image = images_by_id[ImageId.ROUTE_IMAGE]
            
            carved_count += 1

            stack.append(chosen)
        else:
            stack.pop()

    # 4) Once done, pick an end cell among the carved cells
    carved_positions: list[Position] = [
        p for p in all_positions if not grid.cells_by_position[p].is_wall
    ]
    # Choose the farthest from start by Manhattan distance
    if carved_positions:
        end = max(carved_positions, key=lambda p: manhattan_distance(start, p))
        grid.end_position = end
        grid.cells_by_position[end].image = images_by_id[ImageId.END_IMAGE]
    else:
        # If for some reason nothing got carved, fallback
        grid.end_position = start
        grid.cells_by_position[start].image = images_by_id[ImageId.START_IMAGE]


def init_grid(images_by_id: dict[ImageId, pygame.Surface]) -> Grid:
    grid: Grid = Grid()

    for y in range(0, SCREEN_HEIGHT, int(CELL_HEIGHT)):
        for x in range(0, SCREEN_WIDTH, int(CELL_WIDTH)):
            cell: Cell = Cell(image=images_by_id[ImageId.WALL_IMAGE])
            grid.cells_by_position[Position(x, y)] = cell

    return grid


def main():
    clock = pygame.time.Clock()
    last_time = pygame.time.get_ticks()

    pygame.init()
    pygame.display.set_caption("pygame-deep-q")
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    sprite_sheet = Spritesheet(
        ASSETS_PATH / "16x16-dark-tech-base-tileset/troid_spritesheet16.gif"
    )
    image_loader: ImageLoader = ImageLoader(sprite_sheet)
    images_by_id: dict[ImageId, pygame.Surface] = image_loader.load_all_images()

    grid: Grid = init_grid(images_by_id)
    generate_maze_with_branches(images_by_id, grid, 1024)

    while True:
        current_time = pygame.time.get_ticks()
        delta_time = current_time - last_time
        last_time = current_time
        for pos, cell in grid.cells_by_position.items():
            screen.blit(cell.image, (pos.x, pos.y))

        player: Player = Player(cell=Cell(image=images_by_id[ImageId.PLAYER_IMAGE]))

        non_wall_positions: list[Position] = [
            pos for pos, cell in grid.cells_by_position.items() if not cell.is_wall
        ]
        player_pos: Position = rnd.choice(non_wall_positions)

        player_rect = pygame.rect.Rect(
            player_pos.x, player_pos.y, CELL_WIDTH, CELL_HEIGHT
        )

        pygame.draw.rect(screen, (255, 0, 0), player_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        clock.tick(60)
        # print(pygame.time.get_ticks())
        pygame.display.update()


if __name__ == "__main__":
    main()
