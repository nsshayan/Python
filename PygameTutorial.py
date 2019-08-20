import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption("Slither")

#pygame.display.flip() # Same as update function. update enter display at once
pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event)

#Game Loop


pygame.quit() # uninitialize
quit()
