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
ball_y = 0
import random
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    ball_y += 2
    if ball_y >= size[1]:
        ball_y = 0

    # --- Screen-clearing code goes here
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    #Snowflake 1
    pygame.draw.ellipse(screen, WHITE, [100, ball_y,10,10],0)
    #Snowflake 2
    pygame.draw.ellipse(screen, WHITE, [200, ball_y,10,10],0)
    #Snowflake 3
    pygame.draw.ellipse(screen, WHITE, [250, ball_y,10,10],0)
    #Snowflake 4
    pygame.draw.ellipse(screen, WHITE, [400, ball_y,10,10],0)


    pygame.display.flip()
    clock.tick(60)
pygame.quit()

