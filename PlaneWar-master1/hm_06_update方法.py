import pygame

pygame.init()

# ゲームウィンドウを作成する 480 * 700
screen = pygame.display.set_mode((480, 700))

# 背景画像を描く
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

# 主人公の飛行機を描く
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# すべての描画作業が完了した後、updateメソッドを一律に呼び出すことができます
pygame.display.update()

while True:
    pass

pygame.quit()
