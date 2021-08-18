import pygame

pygame.init()

# ゲームウィンドウを作成する 480 * 700
screen = pygame.display.set_mode((480, 700))

# 背景画像を描く
# 1> 画像データを読み込む
bg = pygame.image.load("./images/background.png")
# 2> blit 画像を描く
screen.blit(bg, (0, 0))
# 3> update 画面表示の更新
pygame.display.update()

# 主人公の飛行機を描く
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))
pygame.display.update()

while True:
    pass

pygame.quit()
