import pygame
# initialize the pygame window 
pygame.init()

#making a display object with set_mode 
screen = pygame.display.set_mode((500,500))

#making a varibale
event_loop= True



# looping throuh the event loop
while event_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event_loop=False
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    pygame.display.flip()

pygame.quit()
