import pygame

pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()

rect = pygame.Rect(100, 50, 80, 40)

rect.midtop = (200, 10)
print(rect.left, rect.top)      # 160, 10    (left = 200 - 80//2)

rect.midbottom = (200, 10)
print(rect.left, rect.top)      # 160, -30   (top = 10 - 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(bird_rect.width, bird_rect.height)  # 會印出圖片的寬高
            pygame.quit()
            exit()
    # 把背景變成白的
    screen.fill((255, 255, 255))

    bird_surface = pygame.image.load('flappy-bird-assets/sprites/bluebird-downflap.png').convert()
    bird_rect = bird_surface.get_rect(center=(50, 256))

    screen.blit(bird_surface, bird_rect)

    pygame.display.update()
    clock.tick(120)
