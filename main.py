import pyxel as px

WINDOW_W = 128
WINDOW_H = 128
BLOCK_SIZE = 8
MASK = 2
# シーンの定数定義
SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2



class Player:
    def __init__(self):
        # プレイヤー自身の座標などの状態を定義
        self.x, self.y = (20, 60)
        self.w, self.h = (BLOCK_SIZE, BLOCK_SIZE)
        self.color = 9

    def update(self):
        # プレイヤー自身の移動ロジック
        # self.x += 1
        if px.btn(px.KEY_UP):
            self.y -= 1
        if px.btn(px.KEY_DOWN):
            self.y += 1
        if px.btn(px.KEY_RIGHT):
            self.x += 0.5
        if px.btn(px.KEY_LEFT):
            self.x -= 0.5

        if self.x > WINDOW_W:
            self.x = -BLOCK_SIZE

        if self.y == -BLOCK_SIZE:
            self.y = WINDOW_H

        if self.y > WINDOW_H:
            self.y = -BLOCK_SIZE

    def draw(self):
        # プレイヤー自身の描画処理
        px.blt(self.x, self.y, 0, 0, 0, self.w, self.h, MASK)


class Target:
    def __init__(self, x, y, timing):
        self.x, self.y = (x, y)
        self.start_y = y
        self.w, self.h = (BLOCK_SIZE, BLOCK_SIZE)
        self.count = 0
        self.orient = 1
        self.color = 11
        self.target_max = 15
        self.show = True
        self.timing = timing

    def update(self):
        if self.show:
            self.x -= 3

            self.y = self.start_y + (self.target_max - abs((px.frame_count % (self.target_max * 2)) - self.target_max))

            if self.x < -BLOCK_SIZE:
                self.x = WINDOW_W
                self.show = False
        else:
            if int(px.frame_count % self.timing) == 0:
                self.show = True

    def draw(self):
        px.blt(self.x, self.y, 0, 8, 0, self.w, self.h, MASK)


class App:
    def __init__(self):
        px.init(WINDOW_W, WINDOW_H)
        px.load("my_resource.pyxres")
        # 1. ここでPlayerクラスのインスタンスを作成し、self.player に格納します
        self.player = Player()
        self.targets = [
            Target(WINDOW_W, 50, 10), 
            Target(WINDOW_W, 80, 33), 
            Target(WINDOW_W, 20, 55)
            ]

        # 現在のシーンを保持する変数を追加（初期画面はタイトル）
        self.scene = SCENE_PLAY

        px.run(self.update, self.draw)

    def update(self):

        if self.scene == SCENE_TITLE:
            if px.btnp(px.KEY_RETURN):
                self.scene = SCENE_PLAY

        elif self.scene == SCENE_PLAY:
            # 2. ここで self.player の update メソッドを呼び出します
            self.player.update()

            break_index = []
            for index, target in enumerate(self.targets):
                target.update()
                if target.show:
                    break_index.append(index)




            # for target in self.targets:
            #     if (
            #         self.player.x + self.player.w > target.x
            #         and self.player.x < target.x + target.w
            #         and self.player.y + self.player.h > target.y
            #         and self.player.y < target.y + target.h
            #     ):
            #         px.play(0, 0)
            #         self.player.x, self.player.y = (20, 60)
            #         self.scene = SCENE_GAMEOVER
            #         break

        elif self.scene == SCENE_GAMEOVER:
            if px.btnp(px.KEY_RETURN):
                self.scene = SCENE_PLAY
                self.targets = [Target(50, 50), Target(80, 80), Target(100, 20)]


    def draw(self):
        px.cls(0)

        if self.scene == SCENE_TITLE:
            px.text(40, 50, "TITLE", 7)
        elif self.scene == SCENE_PLAY:
            u = int(px.frame_count % 128)
            px.bltm(0, 0, 0, u, 0, 128, 128)
            px.text(10, 10, str(u), 0)
            px.text(10, 30, str(px.frame_count % 40), 0)
            # 3. ここで self.player の draw メソッドを呼び出します
            self.player.draw()

            # (的の描画は一旦そのままにしておきます)
            for target in self.targets:
                target.draw()
        elif self.scene == SCENE_GAMEOVER:
            px.text(40, 50, "GAME OVER", 7)


App()
