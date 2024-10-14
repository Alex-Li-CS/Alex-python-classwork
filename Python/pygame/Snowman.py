import pygame
pygame.init
def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, [35+x, y, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])
    pygame.draw.ellipse(screen, WHITE, [x, 65 + y, 100, 100])

BLUE = [12, 50, 123]
WHITE = [255, 255, 255]
ORANGE = (255, 165, 0, 255)
font = pygame.font.SysFont('Calibri', 25, True, False)
size = [400, 500]
screen = pygame.display.set_mode(size)
 
done = False
clock = pygame.time.Clock()
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill(BLUE)
    text = font.render("El Snowman",True,ORANGE)
    screen.blit(text, [250, 250])
    draw_snowman(screen, 10, 10)
    draw_snowman(screen, 300, 10)
    draw_snowman(screen, 10, 300)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
