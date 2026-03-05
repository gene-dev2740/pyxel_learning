import pyxel as px

WINDOW_W = 120
WINDOW_H = 120
# シーンの定数定義
SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2


class Player:
    def __init__(self):
        # プレイヤー自身の座標などの状態を定義
        self.x, self.y = (0, 0)
        self.w, self.h = (10, 10)
        self.color = 9

    def update(self):
        # プレイヤー自身の移動ロジック
        self.x += 1
        if px.btn(px.KEY_UP):
            self.y -= 1
        if px.btn(px.KEY_DOWN):
            self.y += 1

        if self.x > WINDOW_W:
            self.x = -10

        if self.y == -10:
            self.y = WINDOW_H

        if self.y > WINDOW_H:
            self.y = -10

    def draw(self):
        # プレイヤー自身の描画処理
        px.blt(self.x, self.y, 0, 0, 0, self.w, self.h, 0)


class Target:
    def __init__(self, x, y):
        self.x, self.y = (x, y)
        self.w, self.h = (10, 10)
        self.color = 11

    def update(self):
        self.x -= 1

        if self.x < -10:
            self.x = WINDOW_W

    def draw(self):
        px.blt(self.x, self.y, 0, 10, 0, self.w, self.h, 0)


class App:
    def __init__(self):
        px.init(WINDOW_W, WINDOW_H)
        px.load("my_resource.pyxres")
        # 1. ここでPlayerクラスのインスタンスを作成し、self.player に格納します
        self.player = Player()
        self.targets = [Target(50, 50), Target(80, 80), Target(100, 20)]

        # 現在のシーンを保持する変数を追加（初期画面はタイトル）
        self.scene = SCENE_TITLE

        px.run(self.update, self.draw)

    def update(self):

        if self.scene == SCENE_TITLE:
            if px.btnp(px.KEY_RETURN):
                self.scene = SCENE_PLAY

        elif self.scene == SCENE_PLAY:
            # 2. ここで self.player の update メソッドを呼び出します
            self.player.update()

            for target in self.targets:
                target.update()

            for target in self.targets:
                if (
                    self.player.x + self.player.w > target.x
                    and self.player.x < target.x + target.w
                    and self.player.y + self.player.h > target.y
                    and self.player.y < target.y + target.h
                ):
                    px.play(0, 0)
                    self.player.x, self.player.y = (0, 0)
                    self.scene = SCENE_GAMEOVER
                    break

        elif self.scene == SCENE_GAMEOVER:
            if px.btnp(px.KEY_RETURN):
                self.scene = SCENE_TITLE

    def draw(self):
        px.cls(0)

        if self.scene == SCENE_TITLE:
            px.text(40, 50, "TITLE", 7)
        elif self.scene == SCENE_PLAY:
            # 3. ここで self.player の draw メソッドを呼び出します
            self.player.draw()

            # (的の描画は一旦そのままにしておきます)
            for target in self.targets:
                target.draw()
        elif self.scene == SCENE_GAMEOVER:
            px.text(40, 50, "GAME OVER", 7)


App()
