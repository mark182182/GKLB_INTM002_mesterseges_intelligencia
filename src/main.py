from random import randint
import pygame

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

cell_height = SCREEN_HEIGHT / (1 << 5)
cell_width = SCREEN_WIDTH / (1 << 5)


def main():
    clock = pygame.time.Clock()
    last_time = pygame.time.get_ticks()

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    while True:
        current_time = pygame.time.get_ticks()
        delta_time = current_time - last_time
        last_time = current_time
        for i in range(0, SCREEN_HEIGHT, int(cell_height)):
            for j in range(0, SCREEN_WIDTH, int(cell_width)):
                cell = pygame.Rect(0, 0, cell_height, cell_width)
                cell.move_ip(i, j)
                if i + cell_height > SCREEN_HEIGHT or j + cell_width > SCREEN_WIDTH:
                    continue
                pygame.draw.rect(screen, (randint(0, 255), 255, 255), cell)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        clock.tick(60)
        print(pygame.time.get_ticks())
        pygame.display.update()


if __name__ == "__main__":
    main()
