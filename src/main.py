import pygame

running = True
screen = pygame.display.set_mode((900, 900))
clock = pygame.time.Clock()

while running:
        for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                        running = False

        screen.fill((0, 0, 0))
        pygame.display.update()
        clock.tick(100)