title: Flappy Bird (288×512) 教學
author: 你的名字
duration: 120 minutes

# 導入（5 分）

- 目標：說明今天的學習目標、預期成果與流程
- 成果展示：完成版遊戲畫面（若可執行請示範）

Speaker notes:
- 簡短自我介紹
- 播放一段遊玩示範（或請講師載入 `game_288x512.py`）

---

# 大綱與時間分配（共 120 分）

我們會把 120 分鐘分成兩部分：前半（60 分）講解 + 示範，後半（60 分）實作練習（適合初學者）。

時間分配（簡要）：
- 導入（5 分）
- 環境準備（7 分）
- Display（10 分）
- Movement（12 分）
- Obstacle（8 分）
- Collision（7 分）
- Music（5 分）
- Events / Timers（3 分）
- 實作/練習（60 分）
- 延伸與結語（3 分）

Speaker notes:
- 強調實作時間給初學者 60 分鐘，講解以示範與即時操作為主

---

# 一、環境準備（7 分）

- 安裝 Python 3.8+（建議 3.10/3.11）
- 安裝 pygame：`pip install pygame`
- 專案檔案：`game_288x512.py`, `flappy-bird-assets/`（確定 sprites 與 audio 存在）

Speaker notes:
- 示範安裝與快速檢查：`python -V`、`python -c "import pygame; print(pygame.ver)"`

---

# Display（10 分）

- 顯示設定：`pygame.display.set_mode((288,512))`
- Surface 與 blit：背景、地板、物件的繪製順序
- 圖片格式轉換：`.convert()`（最快）與 `.convert_alpha()`（保留透明）
- 解析度策略：同尺寸或整數倍縮放；小螢幕檢測 `pygame.display.Info()`

Code hint:
```python
bg = pygame.image.load('background-day.png').convert()
screen.blit(bg, (0,0))
```

Speaker notes:
- 解釋為何把 `.convert()` 放在 `set_mode()` 之後
- 示範用 `screen.get_size()` 動態設定視窗

---

# Movement（12 分）

- 鸟的物理：重力（gravity）、速度（velocity）、跳跃（flap impulse）
- 旋轉與動畫：根據速度旋轉鳥並切換幀
- 範例參數（本課程使用）: gravity=0.25, flap impulse ≈ -8

Code hint:
```python
bird_vel = 0
bird_vel += gravity
bird_y += bird_vel
if jump: bird_vel = -8
```

Speaker notes:
- 示範調整 gravity 與 jump 值如何影響遊玩手感
- 建議學員用小步驟（改一個值、跑一次）測試

---

# Obstacle（8 分）

- 水管生成：定期 spawn、隨機高度、固定 gap
- 移動邏輯：向左移動並在畫面外銷毀
- 間距控制：`PIPE_SPAWN_INTERVAL` 與 `pipe_speed`

Code hint:
```python
pygame.time.set_timer(SPAWNPIPE, PIPE_SPAWN_INTERVAL)
for pipe in pipes: pipe.centerx -= pipe_speed
```

Speaker notes:
- 解釋為何把 spawn_x 設在 `screen_w + offset`（避免剛出現就太近）
- 建議參數調整範圍（例如 interval 1400-2000 ms）

---

# Collision（7 分）

- 使用 `Rect.colliderect()` 做碰撞偵測
- 邊界檢查：鳥離開上下邊界視為死亡
- 計分：通過水管時加分，使用旗標避免重複計分（`can_score`）

Code hint:
```python
for pipe in pipes:
    if bird_rect.colliderect(pipe): game_active = False
```

Speaker notes:
- 示範如何 debug 碰撞（畫出 rect）
- 討論 edge case：同時碰到多個 pipe 時的行為

---

# Music（5 分）

- 初始化 mixer：`pygame.mixer.init()`
- 載入音效：wing, hit, point（若缺檔應退化處理）
- 播放音效的時機：跳躍、死亡、得分

Code hint:
```python
flap = pygame.mixer.Sound('sfx_wing.wav')
flap.play()
```

Speaker notes:
- 若無音效檔，程式應該仍能運行（印出警告）
- 小心頻繁播放音效造成的重複（可用 channel 控制）

---

# Events / Timers（3 分）

- 自訂事件：`pygame.USEREVENT + n` 用於動畫幀切換、spawn 控制
- 範例：`pygame.time.set_timer(BIRDFLAP, 200)`

Speaker notes:
- 簡短示範一個 timer 的用途

---

# 實作/練習（60 分）

目標：讓初學者有充分時間完成下列任務並理解核心概念

建議進行：
- 前 10 分：講師示範重點（Display、Movement、Obstacle、Collision、Music）
- 40 分：學員實作（可分 A/B/C 难度題）
- 10 分：學員展示與講評

任務建議：
- A（基礎，30 分）：調整 `PIPE_SPAWN_INTERVAL`、`pipe_speed`、`gravity`，讓遊戲變容易或變難
- B（進階，40 分）：新增暫停（P 鍵）與重新開始（R 鍵），或在得分時顯示動畫
- C（挑戰，60 分）：新增排行榜（local file）、或加入簡單開場/結束畫面

Speaker notes:
- 提醒初學者把變更分成小步驟測試
- 講師與助教巡迴協助，並收集常見錯誤

---

# 延伸與結語（3 分）

- 課後作業：實作排行榜、增加難度階段、優化音效與 UI
- 參考資源與程式碼位置：`game_288x512.py`, `presentation/` 資料夾

Speaker notes:
- 提供學生提交作業的方式（GitHub PR 與 README）

