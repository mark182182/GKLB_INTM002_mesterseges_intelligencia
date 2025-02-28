import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, CELL_HEIGHT, CELL_WIDTH
from models import Position, Cell, Player, Grid, Map
from images import wall_image, route_image, start_image, end_image
import random as rnd
from random import randint, random


def manhattan_distance(a: Position, b: Position) -> int:
    return int(abs(a.x - b.x) + abs(a.y - b.y))


def generate_maze_with_branches(grid: Grid, carve_limit: int):
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
            # Carve midpoint
            mid_x = (current.x + chosen.x) // 2
            mid_y = (current.y + chosen.y) // 2
            mid_pos = Position(mid_x, mid_y)

            if (
                mid_pos in grid.cells_by_position
                and grid.cells_by_position[mid_pos].is_wall
            ):
                grid.cells_by_position[mid_pos].is_wall = False
                grid.cells_by_position[chosen].image = route_image
                carved_count += 1

            # Carve chosen
            grid.cells_by_position[chosen].is_wall = False
            grid.cells_by_position[chosen].image = route_image
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
        grid.cells_by_position[end].image = end_image
    else:
        # If for some reason nothing got carved, fallback
        grid.end_position = start
        grid.cells_by_position[start].image = start_image


def init_grid() -> Grid:
    grid: Grid = Grid()

    for y in range(0, SCREEN_HEIGHT, int(CELL_HEIGHT)):
        for x in range(0, SCREEN_WIDTH, int(CELL_WIDTH)):
            cell: Cell = Cell()
            grid.cells_by_position[Position(x, y)] = cell

    return grid


def main():
    clock = pygame.time.Clock()
    last_time = pygame.time.get_ticks()

    pygame.init()
    pygame.display.set_caption("pygame-deep-q")
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    grid: Grid = init_grid()
    generate_maze_with_branches(grid, 1024)

    while True:
        current_time = pygame.time.get_ticks()
        delta_time = current_time - last_time
        last_time = current_time
        for pos, cell in grid.cells_by_position.items():
            screen.blit(cell.image, (pos.x, pos.y))

        player: Player = Player(cell=Cell())

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
