import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((288, 512))
pygame.display.set_caption("Flappy Bird Movement Lab")
clock = pygame.time.Clock()
# 載入背景、地板、角色
bg_surface = pygame.image.load('flappy-bird-assets/sprites/background-day.png').convert()
floor_surface = pygame.image.load('flappy-bird-assets/sprites/base.png').convert()
bird_surface = pygame.image.load('flappy-bird-assets/sprites/bluebird-midflap.png').convert_alpha()

# 地板座標
floor_x_pos = 0

# 角色初始位置與移動參數
bird_rect = bird_surface.get_rect(center=(50, 256))
gravity = 0.25
bird_movement = 0

# 字型與分數
game_font = pygame.font.Font('04B_19.ttf', 40)
score = 0

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 400))
    screen.blit(floor_surface, (floor_x_pos + 288, 400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 按空白鍵跳躍
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement = -12

    # 背景
    screen.blit(bg_surface, (0, 0))

    # 角色移動（重力影響）
    bird_movement += gravity
    bird_rect.centery += int(bird_movement)
    screen.blit(bird_surface, bird_rect)

    # 地板移動
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -288:
        floor_x_pos = 0

    # 分數顯示
    score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(144, 50))
    screen.blit(score_surface, score_rect)

    pygame.display.update()
    clock.tick(120)

pygame.quit()
sys.exit()