import pygame # 引入 pygame
pygame.init() # 初始化 pygame
screen = pygame.display.set_mode((288,512))# 開啟視窗
pygame.display.set_caption("第一個遊戲") # 設定標題
bg = pygame.image.load("flappy-bird-assets/sprites/background-day.png").convert() # 載入背景圖片
floor_surface = pygame.image.load('flappy-bird-assets/sprites/base.png').convert()
bird = pygame.image.load('flappy-bird-assets/sprites/bluebird-midflap.png').convert_alpha()
bird_rect = bird.get_rect(center=(50, 256))
clock = pygame.time.Clock()
floor_x_pos = 0
game_font = pygame.font.Font('04B_19.ttf', 40)
score = 2



def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 400))
    screen.blit(floor_surface, (floor_x_pos + 288, 400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement = -6
    

    screen.blit(bg, (0, 0))  # 畫出背景

    # 畫出地板
    draw_floor() 
    score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(144, 50))
    screen.blit(score_surface, score_rect)
    screen.blit(bird, bird_rect)

    clock.tick(60)
    pygame.display.update()









