import pygame

pygame.init()

red = 255
green = 255
blue = 255
color = (red, green, blue)

gameDisplay = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Slither')
# pygame.display.update()

gameRun = True

while (gameRun):
    for event in pygame.event.get():
        # EXIT Handler
        if(event.type == pygame.QUIT):
            gameRun = False

        if(event.type == pygame.KEYDOWN):
            print(event)

    gameDisplay.fill(color)

    pygame.draw.rect(gameDisplay, (0, 0, 0), [300, 300, 10, 10])

    pygame.display.update()
pygame.quit()
quit()
