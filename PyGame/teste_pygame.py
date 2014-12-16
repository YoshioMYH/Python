import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Slither')
pygame.display.update()

gameRun = True

while (gameRun):
    for event in pygame.event.get():
        print(event)


pygame.quit()
quit()
