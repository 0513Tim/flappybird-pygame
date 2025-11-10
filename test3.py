import pygame
pygame.init()
screen = pygame.display.set_mode((288, 512))
pygame.display.set_caption("Rect Location Example")
clock = pygame.time.Clock()
bg_surface = pygame.image.load('flappy-bird-assets/sprites/background-day.png').convert()
running = True
while running : 
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
    screen.blit(bg_surface, (0, 0))
    clock.tick(60)