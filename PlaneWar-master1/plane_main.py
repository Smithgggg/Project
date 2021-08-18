
import pygame
from plane_sprites import *


class PlaneGame(object):
    """航空機戦争マスターゲーム"""

    def __init__(self):
        print("ゲームの初期化")

        # 1. ゲームウィンドウを作成する
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. ゲームクロックを作成する
        self.clock = pygame.time.Clock()
        # 3. プライベートメソッドの呼び出し、スプライトおよびスプライトグループの作成
        self.__create_sprites()

        # 4. タイマーイベントの設定-盗賊の作成　1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):

        # 背景のスプライトとスプライトグループを作成する
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 盗賊のスプライトグループを作成する
        self.enemy_group = pygame.sprite.Group()

        # ヒーロースプライトとスプライトグループを作成する
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("")

        while True:
            # 1. リフレッシュフレームレートを設定する
            self.clock.tick(FRAME_PER_SEC)
            # 2. イベントモニタリング
            self.__event_handler()
            # 3. 影響チェック
            self.__check_collide()
            # 4. スプライトグループの更新/描画
            self.__update_sprites()
            # 5. 表示を更新
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():

            # ゲームを終了するかどうかを決定する
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敵機が登場...")
                # 盗賊のスプライトを作成する
                enemy = Enemy()

                # バンディットスプライトをバンディットスプライトグループに追加します
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("右に移動...")

        # キーボードが提供するメソッドを使用して、キーボードのキー（キータプル）を取得します
        keys_pressed = pygame.key.get_pressed()
        # タプル内の対応するキーインデックス値を決定します 1
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):

        # 1. 弾丸は敵の航空機を破壊します
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 2. 敵機が主人公を墜落させる
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # リストを判断するときに内容があります
        if len(enemies) > 0:

            # 主人公を犠牲にしましょう
            self.hero.kill()

            # ゲーム終了
            PlaneGame.__game_over()

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("ゲームオーバー")

        pygame.quit()
        exit()

if __name__ == '__main__':
    pygame.init()

    # ゲームオブジェクトを作成する
    game = PlaneGame()

    # ゲームを始める
    game.start_game()
