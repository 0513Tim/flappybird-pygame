import pygame
import random
import os
pygame.init()
gravity = 0.20 
bird_movement = 0

# 水管參數
pipe_list = []
pipe_height = [200, 300, 400]
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 2400)


screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()
# 載入背景圖片
bg_surface = pygame.image.load("flappy-bird-assets/sprites/background-day.png").convert()

# 載入地板圖片
floor_surface = pygame.image.load('flappy-bird-assets/sprites/base.png').convert()
floor_x_pos = 0

# 載入角色圖片
bird_surface = pygame.image.load('flappy-bird-assets/sprites/bluebird-midflap.png').convert_alpha()
bird_rect = bird_surface.get_rect(center=(50, 256))

# 載入水管圖片
pipe_surface = pygame.image.load('flappy-bird-assets/sprites/pipe-green.png').convert_alpha()
pipe_list = []

# 顯示地板
def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 400))
    screen.blit(floor_surface, (floor_x_pos + 288, 400))

# 產生水管
def create_pipe():
    random_pipe_pos = random.randint
    bottom_pipe = pipe_surface.get_rect(midtop=(350, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(350, random_pipe_pos - 150))
    print(bottom_pipe, top_pipe)
    return bottom_pipe, top_pipe

# 畫水管
def draw_pipes():
    for pipe in pipe_list:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

# 水管移動
def move_pipes():
    for pipe in pipe_list:
        pipe.centerx -= 5
    return pipe_list

def check_collision(pipes):
    global can_score
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
        # death_sound.play()
            can_score = True
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        can_score = True
        return False
    return True


score = 0
# 載入字型
game_font = pygame.font.Font('04B_19.ttf', 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0 
                bird_movement = -12
    # 畫背景
    screen.blit(bg_surface, (0, 0))
    # 畫地板
    draw_floor()
    # 地板移動
    floor_x_pos -= 1
    # 避免地板消失
    if floor_x_pos <= -288:
        floor_x_pos = 0
    # 角色移動
    bird_movement += gravity 
    bird_rect.centery += int(bird_movement)
    screen.blit(bird_surface, bird_rect)

    # 產生水管
    if len(pipe_list) == 0 or pipe_list[-1].centerx < 150:
        pipe_list.extend(create_pipe())

    # 畫水管
    draw_pipes()
    # 水管移動
    pipe_list = move_pipes()


    # 按空白鍵時
    # 顯示分數
    score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(144, 50))
    screen.blit(score_surface, score_rect)
    if check_collision(pipe_list):
        score += 0.01
        print("Score:", score)
        can_score = False
    if not check_collision(pipe_list):
        score = 0

    pygame.display.update()
    clock.tick(60)