import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((288, 512))
pygame.display.set_caption("Flappy Bird Lab3 - obstacle")

# 載入資源
bg_surface = pygame.image.load('flappy-bird-assets/sprites/background-day.png').convert()
base_surface = pygame.image.load('flappy-bird-assets/sprites/base.png').convert()
bird_surface = pygame.image.load('flappy-bird-assets/sprites/bluebird-midflap.png').convert_alpha()
bird_rect = bird_surface.get_rect(center=(50, 256))
pipe_surface = pygame.image.load('flappy-bird-assets/sprites/pipe-green.png').convert()

# 小鳥參數
gravity = 0.25
bird_movement = 0

# 水管參數
pipe_list = []
pipe_height = [200, 300, 400]
SPAWNPIPE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNPIPE, 2400)

def draw_floor():
    screen.blit(base_surface, (0, 400))
    screen.blit(base_surface, (288, 400))

def create_pipe():
    height = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(350, height))
    top_pipe = pipe_surface.get_rect(midbottom=(350, height - 150))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 2
    return [pipe for pipe in pipes if pipe.right > -50]

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface, pipe)  # 下水管
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)  # 上水管
            screen.blit(flip_pipe, pipe)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 6
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    # 背景
    screen.blit(bg_surface, (0, 0))

    # 小鳥物理
    bird_movement += gravity
    bird_rect.centery += int(bird_movement)

    # 先移動水管，再畫水管（避免殘影）
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # 地板要蓋在水管上
    draw_floor()

    # 小鳥放最上層
    screen.blit(bird_surface, bird_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
