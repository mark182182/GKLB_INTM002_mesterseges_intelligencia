import enum
from random import randint
from re import S
import pygame
from constants import ASSETS_PATH, CELL_HEIGHT, CELL_WIDTH, SPRITE_SIZE
from sprite import Spritesheet


class ImageId(enum.Enum):
    WALL_IMAGE = 1
    ROUTE_IMAGE = 2
    START_IMAGE = 3
    END_IMAGE = 4
    PLAYER_IMAGE = 5
    ENEMY_IMAGE = 6


class ImageLoader:
    __sprite_sheet: Spritesheet

    def __init__(self, sprite_sheet: Spritesheet):
        self.__sprite_sheet = sprite_sheet

    def load_all_images(self) -> dict[ImageId, pygame.Surface]:
        images_by_id: dict[ImageId, pygame.Surface] = {}
        if self.__sprite_sheet:
            images_by_id[ImageId.WALL_IMAGE] = self.__wall_image()
            images_by_id[ImageId.ROUTE_IMAGE] = self.__route_image()
            images_by_id[ImageId.START_IMAGE] = self.__start_image()
            images_by_id[ImageId.END_IMAGE] = self.__end_image()
            images_by_id[ImageId.PLAYER_IMAGE] = self.__player_image()
            images_by_id[ImageId.ENEMY_IMAGE] = self.__enemy_image()
        return images_by_id

    def __wall_image(self) -> pygame.Surface:
        wall_image = self.__sprite_sheet.get_image(0, 0)
        wall_image = pygame.transform.scale(
            wall_image, (int(CELL_WIDTH), int(CELL_HEIGHT))
        )
        return wall_image

    def __route_image(self) -> pygame.Surface:
        route_image = self.__sprite_sheet.get_image(19 * SPRITE_SIZE, 0)
        route_image = pygame.transform.scale(
            route_image, (int(CELL_WIDTH), int(CELL_HEIGHT))
        )
        return route_image

    def __start_image(self) -> pygame.Surface:
        start_image = self.__sprite_sheet.get_image(0 * SPRITE_SIZE, 6 * SPRITE_SIZE)
        start_image = pygame.transform.scale(
            start_image, (int(CELL_WIDTH), int(CELL_HEIGHT))
        )
        return start_image

    def __end_image(self):
        end_image = pygame.image.load(ASSETS_PATH / "end_image.png")
        end_image = pygame.transform.scale(
            end_image, (int(CELL_WIDTH), int(CELL_HEIGHT))
        )
        return end_image

    def __player_image(self):
        player_image = pygame.image.load(ASSETS_PATH / "player_image.png")
        player_image = pygame.transform.scale(
            player_image, (int(CELL_WIDTH), int(CELL_HEIGHT))
        )
        return player_image

    def __enemy_image(self) -> pygame.Surface:
        return None
