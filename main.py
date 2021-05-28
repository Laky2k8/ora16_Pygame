import pygame
import random

pygame.init()

player = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")
bg = pygame.image.load("sky.png")

collectible = pygame.image.load("collect.png")

x = 450
y = 200

enemyX = 700
enemyY = 100

colX = random.randint(10, 500)
colY = random.randint(10, 500)

#enemy stuff
steps_number = max( abs(enemyX-x), abs(enemyY-y) )



#player = pygame.transform.scale(player, (200,200))

screen = pygame.display.set_mode([1000,500])
pygame.display.set_caption("My First Pygame :D")

movingUp = False

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill('white')
        screen.blit(bg, (0, 0))

        pRect = player.get_rect()
        cRect = collectible.get_rect()



        screen.blit(collectible, (colX, colY))



        screen.blit(enemy, (enemyX, enemyY))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                y -= 10
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x -= 10
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y += 10
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x += 10

        screen.blit(player, (x, y))



        pygame.display.flip()

pygame.quit()