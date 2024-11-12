import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x,mole_y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position_x = int(event.pos[0] // 32)
                    position_y = int(event.pos[1] // 32)
                    if position_x == mole_x and position_y == mole_y:
                        mole_x = random.randrange(0, 20)
                        mole_y = random.randrange(0, 16)
            screen.fill("light green")

            for i in range(1,21):
                pygame.draw.line(screen, "black", (32 * i ,0 ), (32 * i, 512))
            for i in range (1, 17):
                pygame.draw.line(screen, "black", (0, 32 * i), (640, 32 * i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x * 32, mole_y * 32)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
