import pygame
pygame.init()
screen = pygame.display.set_mode((288, 512))
bird_surface = pygame.image.load('flappy-bird-assets/sprites/bluebird-midflap.png').convert_alpha()

# 用 center 定位
bird_rect = bird_surface.get_rect(center=(100, 256))
# # 用 topleft 定位（請把上面註解掉，改這行觀察差異）
bird_rect1 = bird_surface.get_rect(topleft=(100, 256))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(bird_surface, bird_rect)
    screen.blit(bird_surface, bird_rect1)
    pygame.display.update()
pygame.quit()