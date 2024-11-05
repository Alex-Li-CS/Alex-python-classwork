import pygame
import random

# Define some colors
BLACK = 0x000000
WHITE = 0xFFFFFF
class Flake: # This is a record
    def __init__(self,x_pos,y_pos,velocity,size) -> None:
        self.x = x_pos
        self.y = y_pos
        self.size = size    
        self.vel = velocity
    # End fields
#end record


pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


rows = 50  
arr = [None for j in range(rows)]  



for row in range(rows):  
     x = random.randint(0,size[0]-1)
     y = random.randint(0,size[1]-1)
     my_flake = Flake(x,y,3,random.randint(5,10))
     arr[row] = my_flake
#next row       
print(arr)

flake_v = 2


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    for row in range(rows):
        arr[row].y += arr[row].vel
        if arr[row].y > size[1]:
            arr[row].y = 0

    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here
    for row in range(rows):
        pygame.draw.rect(screen,WHITE,(arr[row].x,arr[row].y,arr[row].size,arr[row].size)) 


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()