import pathlib
import pygame
from constants import CELL_HEIGHT, CELL_WIDTH

assets_path = pathlib.Path(__file__).parent / "assets"

wall_image = pygame.image.load(assets_path / "wall_image.png")
wall_image = pygame.transform.scale(wall_image, (int(CELL_WIDTH), int(CELL_HEIGHT)))

route_image = pygame.image.load(assets_path / "route_image.png")
route_image = pygame.transform.scale(route_image, (int(CELL_WIDTH), int(CELL_HEIGHT)))

start_image = pygame.image.load(assets_path / "start_image.png")
start_image = pygame.transform.scale(start_image, (int(CELL_WIDTH), int(CELL_HEIGHT)))

end_image = pygame.image.load(assets_path / "end_image.png")
end_image = pygame.transform.scale(end_image, (int(CELL_WIDTH), int(CELL_HEIGHT)))
