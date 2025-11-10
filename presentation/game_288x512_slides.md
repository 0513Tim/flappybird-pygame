## Flappy Bird (288×512) — 程式檔案導覽

簡短說明：這份投影片以 `game_288x512.py` 為素材，分段說明遊戲架構與重點：初始化、資源、主迴圈、鳥的動畫與物理、障礙物（pipes）的生成/移動/繪製、碰撞與分數、音效、以及可調參數與練習題。

---

## 1 — 目標與學習要點
- 建立 288×512 的 Pygame 遊戲視窗
- 理解主迴圈（事件 → 更新 → 繪製）
- 實作鳥的移動（gravity / flap）與簡單動畫
- 產生、移動、繪製障礙物（水管）
- 碰撞偵測（Rect 基礎）與分數機制
- 加入音效與調參示範

Speaker notes: 請在教學時逐步示範每個區塊，先跑 lab0..lab2 再到 lab3 (pipes)，最後到 lab4 (collision) 與 lab5 (sound)。

---

## 2 — 快速執行（Pre-req）
- Python 3.x
- pygame 安裝： `pip install pygame`
- 在專案根目錄執行：

```powershell
python .\game_288x512.py
```

Speaker notes: 若沒有 assets，程式可能會因檔案路徑錯誤停下，建議先確認 `flappy-bird-assets/` 資料夾於專案根目錄。

---

## 3 — 檔案結構（重點片段）
- 初始化：畫面、時鐘、字型、sound mixer（若啟用）
- 資源：背景、地板、鳥幀、管子、音效
- 事件：`SPAWNPIPE`, `BIRDFLAP`, `SCOREEVENT` 等
- 主迴圈：事件處理 → 遊戲狀態（game_active）更新 → 繪製 → FPS 控制

Speaker notes: 可把這一張投影片當作導覽地圖，方便學生看到文件位置再 dive-in。

---

## 4 — 初始化與常數（重點）
- 視窗： `screen = pygame.display.set_mode((288,512))`
- 遊戲參數示例：
  - gravity = 0.25
  - pipe interval = 2400 ms
  - pipe speed (在程式中每幀減 x = 5)

Speaker notes: 強調用 288×512 作為教學基準，並說明如何透過常數調整難度。

---

## 5 — 資源載入
- 背景、地板、鳥幀、管子圖與音效皆以 `pygame.image.load` / `pygame.mixer.Sound` 載入。
- 注意 `.convert()` 與 `.convert_alpha()` 用法以及 missing-file 的 fallback策略（教學中可示範 safe loader）。

Speaker notes: 建議示範把某個檔名故意改錯讓學生看懂 fallback 或錯誤訊息。

---

## 6 — 鳥：動畫、旋轉與物理
- 動畫：定時事件 `BIRDFLAP` 每 200 ms 切換 `bird_frames`（down/mid/up）
- 旋轉：使用 `pygame.transform.rotozoom(bird, -bird_movement * 3, 1)` 依速度傾斜
- 物理：`bird_movement += gravity`；跳躍時 `bird_movement = -6`

Speaker notes: 示範如何調整 `gravity` 與 `flap` 強度來改變遊戲手感。

---

## 7 — Pipes：生成（create_pipe）
- 原理：以隨機高度 (pipe_height list) 決定 midtop / midbottom
- 程式中的參數（範例）：
  - spawn x ≈ 350（程式中）
  - pipe_height = [200,300,400]
  - 生成事件間隔 2400 ms

Code (summary):
```python
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(350, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(350, random_pipe_pos - 150))
    return bottom_pipe, top_pipe
```

Speaker notes: 教學時解釋為何 top 使用 `midbottom` 且 y 減 150 用來製造 gap（gap = 150 在此實作）。討論如何改成基於 `SCREEN_W/SCREEN_H` 的算法。

---

## 8 — Pipes：移動（move_pipes）
- 每幀把所有 pipe 的 centerx 減一個值（程式為 5 px/幀）
- 移除已超出畫面左側的 pipe（cast off 保持 list 小）

Code (summary):
```python
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    visible_pipes = [p for p in pipes if p.right > -50]
    return visible_pipes
```

Speaker notes: 示範如何用不同速度產生不同難度，或用 `dt`（delta time）使速度與 FPS 無關。

---

## 9 — Pipes：繪製（draw_pipes）
- 畫 bottom pipe 原圖；畫 top pipe 時把圖翻轉 (flip) 再 blit

Code (summary):
```python
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
```

Speaker notes: 為何檢查 `pipe.bottom >= 512`（用以判斷是底管或頂管），以及翻轉的必要性。

---

## 10 — 碰撞與分數
- 碰撞：`bird_rect.colliderect(pipe)`；碰到地板或飛出上方也視為死亡
- 分數：當任一 pipe 的 centerx 經過特定範圍且 `can_score` 為 True 時，分數遞增並觸發音效

Speaker notes: 講解 `can_score` 這個旗標如何避免重複計分。示範把計分條件改為「bird 與管子中間通過中心線」的精確做法。

---

## 11 — 音效與事件
- flap, death, point 三種 Sound
- `pygame.time.set_timer` 用來做鳥扇動與其他週期性事件

Speaker notes: 在教學中展示如何安全載入音效（避免無檔案時程式崩潰），以及如何調整音量或用 channel 控制同時音效數量。

---

## 12 — 可調參數（教學練習）
- gravity, flap_strength, pipe_interval, pipe_speed, pipe_gap
- 練習：讓學生改變 2 個參數，觀察手感與難度差異

Exercise suggestions:
- Q1: 把 pipe interval 改小到 1800，描述遊戲行為差異
- Q2: 將 pipe gap 改為 100，觀察玩家成功率
- Q3: 改用 mask collision 做像素精準判定

---

## 13 — 教學流程建議（2 小時）
0–20 min: lab0 初始化 + 顯示
20–40 min: lab1 背景與資源載入
40–70 min: lab2 鳥的移動與動畫
70–100 min: lab3 pipes 生成/移動/繪製（實作題）
100–115 min: lab4 碰撞與分數
115–120 min: lab5 音效 + Q&A

Speaker notes: 把練習分組，讓學生在 lab3 實作並互相展示不同參數組合。

---

## 14 — 附錄：關鍵程式碼（copy-ready）
- create_pipe / move_pipes / draw_pipes 的完整片段（請參照 `game_288x512.py`）

---

## 15 — 轉換與使用
- 如果你想用 Reveal.js/markdown 做簡報：
  - 安裝 reveal-md： `npm i -g reveal-md`（或用 Docker）
  - 在專案資料夾執行： `reveal-md presentation/game_288x512_slides.md --open`
- 若要 PPTX：使用 pandoc 或手動匯出（可另行自動化）。

Speaker notes: 我可以幫你把 slides 轉成 PPTX（需安裝 pandoc / libreoffice），或把投影片排版微調。
