import random
import pygame

# 画面サイズの定数
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# フレームレートを更新する
FRAME_PER_SEC = 60
# 盗賊のタイマー定数を作成する
CREATE_ENEMY_EVENT = pygame.USEREVENT
# ヒーローが弾丸事件を発砲
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飛行機戦争ゲームウィザード"""

    def __init__(self, image_name, speed=1):

        # 親クラスの初期化メソッドを呼び出す
        super().__init__()

        # オブジェクトのプロパティを定義します
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 画面の垂直方向に移動します
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1. 親クラスメソッドを呼び出して、ウィザードの作成を実現します(image/rect/speed)
        super().__init__("./images/background.png")

        # 2. 代替画像かどうかを判断します。代替画像の場合は、初期位置を設定する必要があります
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1. 親クラスのメソッド実装を呼び出す
        super().update()

        # 2. 画面の外に移動するかどうかを決定します。画面の外に移動する場合は、画像を画面の上部に設定します
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):

        # 1. 親クラスメソッドを呼び出して、敵機のスプライトを作成し、同時に敵機の画像を指定します
        super().__init__("./images/enemy1.png")

        # 2. 盗賊の初期ランダム速度を指定します 1 ~ 3
        self.speed = random.randint(1, 3)

        # 3. 盗賊の最初のランダムな位置を指定します
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # 1. 親クラスのメソッドを呼び出して、垂直飛行を維持します
        super().update()

        # 2. 画面から飛び出すかどうかを決定します。飛び出す場合は、ウィザードグループから敵の航空機を削除する必要があります。
        if self.rect.y >= SCREEN_RECT.height:
            # print("画面から飛び出し、ウィザードグループから削除する必要があります...")
            # killメソッドを使用すると、すべてのウィザードグループからウィザードを削除でき、ウィザードは自動的に破棄されます。
            self.kill()

    def __del__(self):
        # print("敵機がハングアップしている %s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):

        # 1. 親クラスのメソッドを呼び出し、画像と速度を設定します
        super().__init__("./images/me1.png", 0)

        # 2. 主人公の初期位置を設定します
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3. 弾丸のスプライトグループを作成する
        self.bullets = pygame.sprite.Group()

    def update(self):

        # 主人公は水平方向に動きます
        self.rect.x += self.speed

        # コントロールヒーローは画面を離れることができません
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹...")

        for i in (0, 1, 2):
            # 1. 箇条書きの作成ウィザード
            bullet = Bullet()

            # 2. スプライトの位置を設定します
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 3. スプライトグループにスプライトを追加します
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """弾丸ウィザード"""

    def __init__(self):

        # 親クラスのメソッドを呼び出し、箇条書きの画像を設定し、初速度を設定します
        super().__init__("./images/bullet1.png", -2)

    def update(self):

        # 親クラスのメソッドを呼び出して、弾丸を垂直方向に飛ばします
        super().update()

        # 弾丸が画面から飛び出すかどうかを確認します
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("弾丸は破壊されます...")
