"""
簡化版 Flappy Bird（供初學者閱讀與練習）

特點：
- 解析度 288x512
- 單幀鳥（無動畫），簡單重力與跳躍
- 水管 spawn / 移動 / 碰撞與分數（簡單實作）
- 明確註解，易讀且容易修改參數

執行：
    python .\examples\02_simple_flappy.py
"""
import pygame
import sys
import random
import os

# ---------- 初始化 ----------
pygame.init()
SCREEN_W, SCREEN_H = 288, 512
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('Simple Flappy (288x512)')
clock = pygame.time.Clock()
FPS = 60

# 簡單字型
font = pygame.font.Font(None, 36)

# ---------- 資源載入（簡單容錯） ----------
def load_image(path, fallback_size=None, use_alpha=True):
    if os.path.exists(path):
        img = pygame.image.load(path)
        return img.convert_alpha() if use_alpha else img.convert()
    # 找不到檔案時回傳一個顏色塊，讓程式能繼續執行
    if fallback_size is None:
        fallback_size = (50, 50)
    s = pygame.Surface(fallback_size, pygame.SRCALPHA)
    s.fill((200, 50, 50))
    return s

# 資源路徑（預設放在 assets/）
bg = load_image(os.path.join('assets', 'background-day.png'), (SCREEN_W, SCREEN_H), use_alpha=False)
floor_img = load_image(os.path.join('assets', 'base.png'), (SCREEN_W, 112), use_alpha=False)
bird_img = load_image(os.path.join('assets', 'bluebird-midflap.png'), (34, 24), use_alpha=True)
pipe_img = load_image(os.path.join('assets', 'pipe-green.png'), (52, 320), use_alpha=True)

# ---------- 參數 ----------
gravity = 0.25
flap_strength = -7
bird_x = 50
bird_y = SCREEN_H // 2
bird_vel = 0
bird_rect = bird_img.get_rect(center=(bird_x, bird_y))

floor_x = 0
floor_y = SCREEN_H - 112

pipe_list = []
PIPE_EVENT = pygame.USEREVENT + 1
PIPE_INTERVAL = 1600  # 毫秒
pygame.time.set_timer(PIPE_EVENT, PIPE_INTERVAL)
pipe_speed = 3
pipe_gap = 120
pipe_heights = [200, 250, 300]

score = 0
can_score = True
game_active = True

# ---------- 小函式 ----------
# ---------- 初始化 ----------
pygame.init()
try:
    pygame.mixer.init()
except Exception:
    # mixer 初始化失敗不應該阻止教學範例運行
    pass

SCREEN_W, SCREEN_H = 288, 512
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('Simple Flappy (288x512)')
clock = pygame.time.Clock()
FPS = 60

# 簡單字型
font = pygame.font.Font(None, 36)


# ---------- Display （畫面 & 資源載入） ----------
def load_image(path, fallback_size=None, use_alpha=True):
    """簡單的載入函式：檔案不存在時回傳顏色塊（避免初學者因資源缺失卡住）。"""
    if os.path.exists(path):
        img = pygame.image.load(path)
        return img.convert_alpha() if use_alpha else img.convert()
    if fallback_size is None:
        fallback_size = (50, 50)
    s = pygame.Surface(fallback_size, pygame.SRCALPHA)
    s.fill((200, 50, 50))
    return s

# 預設在 assets/ 裡找資源
bg = load_image(os.path.join('assets', 'background-day.png'), (SCREEN_W, SCREEN_H), use_alpha=False)
floor_img = load_image(os.path.join('assets', 'base.png'), (SCREEN_W, 112), use_alpha=False)
bird_img = load_image(os.path.join('assets', 'bluebird-midflap.png'), (34, 24), use_alpha=True)
pipe_img = load_image(os.path.join('assets', 'pipe-green.png'), (52, 320), use_alpha=True)


# ---------- Movement （鳥的物理與跳躍） ----------
gravity = 0.25
flap_strength = -7
bird_x = 50
bird_y = SCREEN_H // 2
bird_vel = 0
bird_rect = bird_img.get_rect(center=(bird_x, bird_y))

floor_x = 0
floor_y = SCREEN_H - 112


# ---------- Obstacle （水管生成、移動與繪製） ----------
pipe_list = []
PIPE_EVENT = pygame.USEREVENT + 1
PIPE_INTERVAL = 1600  # 毫秒
pygame.time.set_timer(PIPE_EVENT, PIPE_INTERVAL)
pipe_speed = 3
pipe_gap = 120
pipe_heights = [200, 250, 300]

def create_pipe():
    h = random.choice(pipe_heights)
    bottom = pipe_img.get_rect(midtop=(SCREEN_W + 50, h))
    top = pipe_img.get_rect(midbottom=(SCREEN_W + 50, h - pipe_gap))
    return bottom, top

def move_pipes(pipes):
    for p in pipes:
        p.centerx -= pipe_speed
    return [p for p in pipes if p.right > -50]

def draw_pipes(pipes):
    for p in pipes:
        if p.bottom >= SCREEN_H:
            screen.blit(pipe_img, p)
        else:
            screen.blit(pygame.transform.flip(pipe_img, False, True), p)


# ---------- Collision （碰撞與計分） ----------
score = 0
can_score = True
game_active = True

def check_collision(pipes):
    """如果碰到水管或出界回傳 False（遊戲結束）。"""
    global can_score
    for p in pipes:
        if bird_rect.colliderect(p):
            # 播放死亡音（若有）由 Music 區塊管理
            if 'death_sound' in globals() and death_sound:
                death_sound.play()
            can_score = True
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= floor_y:
        if 'death_sound' in globals() and death_sound:
            death_sound.play()
        can_score = True
        return False
    return True


# ---------- Music （簡單音效支援） ----------
def load_sound(path):
    if os.path.exists(path):
        try:
            return pygame.mixer.Sound(path)
        except Exception:
            return None
    return None

# 嘗試載入常見路徑下的 sfx（若不存在則為 None，不會中斷程式）
flap_sound = load_sound(os.path.join('sound', 'sfx_wing.wav')) or load_sound(os.path.join('flappy-bird-assets', 'audio', 'wing.wav'))
death_sound = load_sound(os.path.join('sound', 'sfx_hit.wav')) or load_sound(os.path.join('flappy-bird-assets', 'audio', 'hit.wav'))
score_sound = load_sound(os.path.join('sound', 'sfx_point.wav')) or load_sound(os.path.join('flappy-bird-assets', 'audio', 'point.wav'))


# ---------- Utility: 畫地板與顯示分數 ----------
def draw_floor():
    screen.blit(floor_img, (floor_x, floor_y))
    screen.blit(floor_img, (floor_x + SCREEN_W, floor_y))


# ---------- 主迴圈（整合上面五個部分） ----------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_vel = 0
                bird_vel += flap_strength
                if flap_sound:
                    flap_sound.play()
            if event.key == pygame.K_SPACE and not game_active:
                # 重新開始
                game_active = True
                pipe_list.clear()
                bird_rect.center = (bird_x, SCREEN_H // 2)
                bird_vel = 0
                score = 0
        if event.type == PIPE_EVENT and game_active:
            pipe_list.extend(create_pipe())

    # Display: 畫背景
    screen.blit(bg, (0, 0))

    # Movement: 更新鳥的位置
    if game_active:
        bird_vel += gravity
        bird_rect.centery += bird_vel
        screen.blit(bird_img, bird_rect)

        # Obstacle: 管道邏輯
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Collision: 檢查碰撞
        game_active = check_collision(pipe_list)

        # Collision / Score: 簡單分數檢查
        for p in pipe_list:
            if p.bottom >= SCREEN_H:
                if p.centerx < bird_x and can_score:
                    score += 1
                    can_score = False
                    if score_sound:
                        score_sound.play()
            if p.centerx < 0:
                can_score = True
    else:
        # 顯示簡單的「Game Over」訊息
        msg = font.render('Game Over - Press SPACE to restart', True, (255, 255, 255))
        screen.blit(msg, msg.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2)))

    # 地板顯示（Display）
    floor_x -= 1
    if floor_x <= -SCREEN_W:
        floor_x = 0
    draw_floor()

    # 分數顯示（Display）
    score_surf = font.render(str(score), True, (255, 255, 255))
    screen.blit(score_surf, score_surf.get_rect(center=(SCREEN_W // 2, 40)))

    pygame.display.update()
    clock.tick(FPS)
