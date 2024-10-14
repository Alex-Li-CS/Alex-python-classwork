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

# POSITIONS
ball_x = 290
ball_y = 190
velocity_x = 5
velocity_y = 5
score = 0
bouncer_righty = 190
bouncer_lefty = 190
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    # Velocity
    ball_x += velocity_x
    ball_y += velocity_y
    # If x coordinate of the ball is off the left side or right side
    # off the screen the ball resets to the middle 
    if ball_x >= size[0] + 10 or ball_x <= -10:
        ball_x = 290
        ball_y = 190
        score += 1
    # If y coordinate of ball hits top or bottom of screen reverse direction
    if ball_y >= size[1] or ball_y <= 0:
        velocity_y = velocity_y * -1
    # If the Ball hits LEFT Bouncer
    if 680 <= ball_x <= 695 and bouncer_lefty <= ball_y <= bouncer_lefty + 180:
        velocity_x = velocity_x * -1
    # If the Ball hits RIGHT Bouncer
    if 5<= ball_x <= 20 and bouncer_righty <= ball_y >= bouncer_righty + 180:
        velocity_x = velocity_x * -1
    
    # CONTROLS
    # Bouncer RIGHT
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            bouncer_righty -= 4
        if event.key == pygame.K_DOWN:
            bouncer_righty += 4
        if event.key == pygame.K_w:
            bouncer_lefty -= 4
        if event.key == pygame.K_s:
            bouncer_lefty += 4


    screen.fill(BLACK)
    # Ball
    pygame.draw.ellipse(screen, WHITE, [ball_x, ball_y,20,20],0)

    # Bouncer LEFT
    pygame.draw.rect(screen, RED, [0, bouncer_lefty, 10, 180],0)

    #Bouncer RIGHT
    pygame.draw.rect(screen, RED, [690, bouncer_righty, 10, 180],0)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()