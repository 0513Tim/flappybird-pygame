Flappy Bird 288x512 — 2 小時教學簡報

這個資料夾包含針對 `game_288x512.py` 的 2 小時教學簡報（Markdown 格式），方便在 VSCode 的 Markdown Preview 或用 reveal.js / pandoc 轉成 PPTX / PDF。

檔案：
- slides.md — 投影片（每段為一張投影片），包含講者筆記與每張投影片建議時長。

如何檢視：
1. 在 VSCode 中打開 `presentation/slides.md`，使用 Markdown Preview 或安裝"Markdown Preview Enhanced"套件可呈現投影片模式。
2. 使用 reveal.js：
   - 安裝 reveal-md（npm i -g reveal-md）
   - 在專案根目錄執行：
     ```powershell
     reveal-md presentation/slides.md --watch
     ```
3. 使用 pandoc 轉成 PPTX 或 PDF：
   - 轉 PPTX：
     ```powershell
     pandoc presentation/slides.md -t pptx -o presentation/Flappy_288x512.pptx
     ```
   - 轉 PDF（需 LaTeX）：
     ```powershell
     pandoc presentation/slides.md -o presentation/Flappy_288x512.pdf
     ```

備註：
- slides.md 中每張投影片的講稿放在每節下面，標記為 "Speaker notes:"。
- 若要我同時產出 PPTX 檔，我可以用 python-pptx 自動化生成（需你允許新增依賴或我提交已生成的檔）。
