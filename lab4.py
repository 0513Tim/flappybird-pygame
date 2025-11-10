import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((288, 512))
pygame.display.set_caption("Flappy Bird Lab4 - Collision")

# 載入資源
bg_surface = pygame.image.load('flappy-bird-assets/sprites/background-day.png').convert()
base_surface = pygame.image.load('flappy-bird-assets/sprites/base.png').convert()
bird_surface = pygame.image.load('flappy-bird-assets/sprites/bluebird-midflap.png').convert_alpha()
bird_rect = bird_surface.get_rect(center=(50, 256))
pipe_surface = pygame.image.load('flappy-bird-assets/sprites/pipe-green.png').convert()

# 小鳥參數
gravity = 0.25
bird_movement = 0
game_active = True

# score
score = 0
high_score = 0
can_score = True
game_font = pygame.font.Font('04B_19.ttf', 40)  # 沒有字型檔可改 None

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
        pipe.centerx -= 5
    return [pipe for pipe in pipes if pipe.right > -50]

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface, pipe)               # 下水管
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)  # 上水管
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            
            return False
    if bird_rect.top <= 0 or bird_rect.bottom >= 400:  # 地板頂端 y=400
        return False
    return True

def update_score(score, high_score):
	if score > high_score:
		high_score = score
	return high_score

def pipe_score_check():
    global score, can_score 
    if pipe_list:
        for pipe in pipe_list:
            # 小鳥中心 x ≈ 100，當下水管中心通過這條線時 +1
            if 95 < pipe.centerx < 105 and can_score:
                score += 1
                can_score = False
            # 這根管子整組離開畫面後，允許下次計分
            if pipe.centerx < 0:
                can_score = True

def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255,255,255))
        score_rect = score_surface.get_rect(center=(144, 50))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255,255,255))
        score_rect = score_surface.get_rect(center=(144, 50))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High score: {int(high_score)}', True, (255,255,255))
        high_score_rect = high_score_surface.get_rect(center=(144, 425))
        screen.blit(high_score_surface, high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 6
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (50, 256)
                bird_movement = 0
                score = 0
                can_score = True


        if event.type == SPAWNPIPE and game_active:
            pipe_list.extend(create_pipe())

    # 背景
    screen.blit(bg_surface, (0, 0))

    # 物理更新（只在進行中）
    if game_active:
        bird_movement += gravity
        bird_rect.centery += int(bird_movement)
        pipe_list = move_pipes(pipe_list)

    # 先畫水管，再畫地板，最後畫小鳥（小鳥在最上層）
    draw_pipes(pipe_list)
    draw_floor()
    screen.blit(bird_surface, bird_rect)

    # 碰撞檢查
    if game_active:
        game_active = check_collision(pipe_list)
        pipe_score_check()
        score_display('main_game')
    else:
        high_score = update_score(score, high_score)
        score_display('game_over')

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
