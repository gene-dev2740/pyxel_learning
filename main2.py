import pyxel as px

WINDOW_W, WINDOW_H = (128, 128)
BLOCK_SIZE = 8
MASK = 2

SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_MENU = 2

class Object():
    def __init__(self):
        self.x, self.y = (140, 100)
    
    def update(self, map_u):
        self.x = self.x - map_u

    def draw(self):
        px.rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE, 6)



class Player:
    def __init__(self):
        self.x, self.y = (64, 64)
        self.color = 9
        self.move = 0

    def update(self):
        if px.btn(px.KEY_RIGHT):
            self.move = 1
        if px.btn(px.KEY_LEFT):
            self.move = -1

    def draw(self):
        px.rect((WINDOW_W / 2) - (BLOCK_SIZE / 2), 100, BLOCK_SIZE, BLOCK_SIZE, 2)
        
        


class App:
    def __init__(self):
        px.init(WINDOW_W, WINDOW_H)
        px.load("my_resource.pyxres")

        self.scene = SCENE_PLAY

        self.player = None
        self.u = 0

        px.run(self.update, self.draw)

    
    def update(self):
        self.player = Player()
        self.object = Object()
        if self.scene == SCENE_TITLE:
            if px.btn(px.KEY_RETURN):
                self.scene = SCENE_PLAY

        elif self.scene == SCENE_PLAY:
            self.player.update()
            self.u += self.player.move
            if self.u < 0:
                self.u = 0
            elif self.u >= 128:
                self.u = 128
            self.object.update(self.u)

            # if self.u + self.object.x == 140:
            #     self.u -= 1

        elif self.scene == SCENE_MENU:
            pass


    def draw(self):
        px.cls(0)

        px.bltm(0, 0, 0, self.u, 0, 128, 128)
        px.line(WINDOW_W / 2, 0, WINDOW_W / 2, WINDOW_H, 7)
        px.line(0, WINDOW_H /2, WINDOW_W, WINDOW_H /2, 7)
        px.text(10, 10, str(self.u), 7)
        if self.scene == SCENE_TITLE:
            px.text(10, 64, "PXEXL LEARNING", 7)
            pass
        elif self.scene == SCENE_PLAY:
            self.player.draw()
            self.object.draw()
        elif self.scene == SCENE_MENU:
            pass

App()