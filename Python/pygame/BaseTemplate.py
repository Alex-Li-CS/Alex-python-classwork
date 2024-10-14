import pygame
 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 255, 255)
 
pygame.init()
 

size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False

clock = pygame.time.Clock()
 

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    # --- Screen-clearing code goes here
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)




    pygame.display.flip()
    clock.tick(60)
pygame.quit()