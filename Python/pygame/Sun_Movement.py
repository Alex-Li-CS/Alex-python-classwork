import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 255, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("The Sun")
done = False
clock = pygame.time.Clock()

# Sun's initial position
x = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    x += 1 
    if x > size[0]:
        x = -100 
    y = int(100 * (1 - (x / size[0])) ** 2 + 100)

    # --- Screen-clearing code goes here
    screen.fill(BLACK)

    # --- Drawing code should go here
    # THE SUN
    pygame.draw.ellipse(screen, YELLOW, [x, y, 100, 100])

    # House
    pygame.draw.rect(screen, RED, [250, 250, 200, 100])
    # Windows
    pygame.draw.rect(screen, BLUE, [275, 275, 50, 30])
    pygame.draw.rect(screen, BLUE, [375, 275, 50, 30])
    # Ground
    pygame.draw.rect(screen, GREEN, [0, 350, 700, 700])
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)