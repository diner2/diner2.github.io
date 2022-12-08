import pygame

# 初始化 Pygame
pygame.init()

# 創建一個窗口
screen = pygame.display.set_mode((800, 600))

# 設置窗口標題
pygame.display.set_caption("My 2D Game")

# 遊戲主循環
while True:
    # 更新遊戲狀態
    # 繪制遊戲畫面
    pygame.display.flip()
