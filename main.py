import pygame

pygame.init()

player = pygame.image.load("player.png")

screen = pygame.display.set_mode([500,500])
pygame.display.set_caption("My First Pygame :D")

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill('white')

        screen.blit(player, (200, 200))
        pygame.display.flip()

pygame.quit()