import enum
from random import randint
from re import S
from models import Position
import pygame
from constants import ASSETS_PATH, CELL_HEIGHT, CELL_WIDTH, SPRITE_SIZE
from sprite import Spritesheet


class ImageId(enum.Enum):
    WALL_IMAGE = Position(0, 2)
    ROUTE_IMAGE = Position(6, 1)
    START_IMAGE = Position(4, 4)
    END_IMAGE = Position(4, 3)
    PLAYER_IMAGE = Position(1, 0)
    ENEMY_IMAGE = Position(3, 3)

    @staticmethod
    def values() -> list["ImageId"]:
        return list(ImageId)


class ImageLoader:
    __sprite_sheet: Spritesheet

    def __init__(self, sprite_sheet: Spritesheet):
        self.__sprite_sheet = sprite_sheet

    def load_all_images(self) -> dict[ImageId, pygame.Surface]:
        images_by_id: dict[ImageId, pygame.Surface] = {}
        for image_id in ImageId.values():
            images_by_id[image_id] = self.__load_image(image_id)
        return images_by_id

    def __load_image(self, image_id: ImageId) -> pygame.Surface:
        image: pygame.Surface = self.__sprite_sheet.get_image(
            SPRITE_SIZE * image_id.value.x, SPRITE_SIZE * image_id.value.y
        )
        image = pygame.transform.scale(image, (int(CELL_WIDTH), int(CELL_HEIGHT)))
        image.set_colorkey((0, 0, 0))
        return image
