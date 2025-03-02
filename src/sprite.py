import pathlib
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPRITE_SIZE
import pygame


class Spritesheet:
    sprite_size: int = SPRITE_SIZE

    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load(filename).convert()

    def get_image(self, x, y):
        image = pygame.Surface([self.sprite_size, self.sprite_size], pygame.SRCALPHA)
        image.blit(
            self.sprite_sheet,
            (0, 0),
            (x, y, self.sprite_size, self.sprite_size),
        )
        return image


def main():
    # test the spritesheet
    sprite_sheet = Spritesheet(
        pathlib.Path(__file__).parent
        / "assets/16x16-dark-tech-base-tileset/troid_spritesheet16.gif"
    )
    image = sprite_sheet.get_image(0 * SPRITE_SIZE, 6 * SPRITE_SIZE)
    screen.blit(image, (0, 0))

    image = sprite_sheet.get_image(0 * SPRITE_SIZE, 7 * SPRITE_SIZE)
    screen.blit(image, (0, SPRITE_SIZE))


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("pygame-deep-q")
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
