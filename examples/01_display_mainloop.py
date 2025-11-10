"""
Minimal Pygame example: import, display, and main loop.
Run: python .\examples\01_display_mainloop.py
"""
import pygame
import sys

# Initialize pygame modules
pygame.init()

# Window size (288 x 512 is the Flappy Bird asset size)
SCREEN_W, SCREEN_H = 288, 512

# Create the display surface (window)
# You can add flags like pygame.RESIZABLE or pygame.SCALED if desired
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('Display & Main Loop Example')

# Clock for FPS control
clock = pygame.time.Clock()
FPS = 60

# Basic background color (R,G,B)
BG_COLOR = (30, 30, 40)

# Example main loop
def main():
    running = True
    while running:
        # 1) Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 2) Game update logic would go here
        # (movement, collision, spawning, etc.)

        # 3) Drawing
        screen.fill(BG_COLOR)

        # Example drawing: a white rectangle in the center
        rect_w, rect_h = 100, 40
        rect = pygame.Rect((SCREEN_W - rect_w) // 2, (SCREEN_H - rect_h) // 2, rect_w, rect_h)
        pygame.draw.rect(screen, (240, 240, 240), rect)

        # 4) Flip the display (update the screen)
        # .flip() updates the full display; .update(rect) can update a portion
        pygame.display.flip()

        # 5) Tick the clock to limit the frame rate
        clock.tick(FPS)

    # Clean up
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
