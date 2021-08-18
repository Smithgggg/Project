import pygame
from plane_sprites import *


# ゲームの初期化
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

# 時計オブジェクトを作成する
clock = pygame.time.Clock()

# 1. 航空機の初期位置を記録するためにrectを定義します
hero_rect = pygame.Rect(150, 300, 102, 126)


# 盗賊のスプライトを作成する
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)
# 盗賊のスプライトグループを作成する
enemy_group = pygame.sprite.Group(enemy, enemy1)


# ゲームループ->はゲームの正式な開始を意味します！
while True:

    # ループ本体内でコードを実行する頻度を指定できます
    clock.tick(60)

    # イベントを聞く
    for event in pygame.event.get():

        # イベントタイプが終了イベントであるかどうかを確認します
        if event.type == pygame.QUIT:
            print("游戏退出...")

            # quit すべてのモジュールをアンインストールします
            pygame.quit()

            # exit() 現在実行中のプログラムを直接終了します
            exit()

    # 2. 航空機の位置を変更します
    hero_rect.y -= 1

    # 航空機の位置を特定する
    if hero_rect.y <= 0:
        hero_rect.y = 700

    # 3. blitメソッドを呼び出して画像を描画します
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # ウィザードグループに2つのメソッドを呼び出させます
    # update - ウィザードグループに2つのメソッドを呼び出させます
    enemy_group.update()

    # draw - 画面にすべてのスプライトを描画します
    enemy_group.draw(screen)


    # 4. updateメソッドを呼び出して、表示を更新します
    pygame.display.update()

pygame.quit()
