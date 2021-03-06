import pygame as pg
import sys
import random
from pygame import mixer


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
        # # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1 
        self.blit(scr)



class Beam:#レーザーを放つ
    def __init__(self,image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self,scr:Screen):
        key_states = pg.key.get_pressed()
        if key_states[pg.K_SPACE]: 
            scr.sfc.blit(self.sfc, self.rct)
        
    def update(self,scr):
        self.blit(scr)
        

class Bomb: #爆弾クラス
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate  
        key_states = pg.key.get_pressed() 
        if key_states[pg.K_s] :  #玉の速度上昇
            self.vx *= 1.01
            self.vy *= 1.01
        if key_states[pg.K_a] :  #玉の速度減少
            self.vx *= 0.99
            self.vy *= 0.99

        

        # 練習5
        self.blit(scr) 



def music(): #音楽の再生
    mixer.init()
    mixer.music.load("fig/2_23_AM.mp3")
    mixer.music.play(5)



def main():
    root = tk.Tk()
    root.title("GAME OVER")
    root.geometry("500x200")

    label1 = tk.Label(root,text="下手くそ!",font=("Ricty Diminished",80))
    label1.pack()

    clock = pg.time.Clock()
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkd = Bomb((255,0,0), 10, (+1,+1), scr)
    attack = Beam("fig/beam.png",0.1,(kkt.rct.centerx,kkt.rct.centery))
    music()

    while True:
        scr.blit()
        
        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        kkt.update(scr)
        bkd.update(scr)
        attack.update(scr)
        if kkt.rct.colliderect(bkd.rct):
            return

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right: 
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: 
        tate = -1 # 領域
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
