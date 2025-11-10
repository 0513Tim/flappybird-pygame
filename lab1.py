import pygame
import sys

# 初始化 pygame
pygame.init()

# 視窗設定
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird lab1 - Display")

# FPS 設定
clock = pygame.time.Clock()
FPS = 60

# 載入圖片
bg_surface = pygame.image.load('flappy-bird-assets/sprites/background-day.png').convert()
floor_surface = pygame.image.load('flappy-bird-assets/sprites/base.png').convert()
bird_surface = pygame.image.load('flappy-bird-assets/sprites/bluebird-midflap.png').convert_alpha()

# 地板座標
floor_x_pos = 0

# 載入字型
game_font = pygame.font.Font('04B_19.ttf', 40)
score = 0

# 角色 rect 設定（以中心點定位）
bird_rect = bird_surface.get_rect(center=(50, 256))
# print(bird_rect)
def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 400))
    screen.blit(floor_surface, (floor_x_pos + SCREEN_WIDTH, 400))

# 主迴圈
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 畫背景
    screen.blit(bg_surface, (0, 0))

    # 畫地板（移動效果）
    # floor_x_pos -= 1
    draw_floor()
    # if floor_x_pos <= -SCREEN_WIDTH:
    #     floor_x_pos = 0

    # 畫角色
    screen.blit(bird_surface, bird_rect)
    # 畫角色碰撞箱（紅色框線，方便觀察）
    # pygame.draw.rect(screen, (255, 0, 0), bird_rect, 2)

    # 顯示分數
    score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(SCREEN_WIDTH//2, 50))
    screen.blit(score_surface, score_rect)

    pygame.display.update()

pygame.quit()
sys.exit()