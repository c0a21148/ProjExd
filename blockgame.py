import pygame
import pygame as pg
from pygame.locals import *
import sys
import pygame.mixer
import tkinter as tk

SCREEN = Rect(0, 0, 1200, 900)
root = tk.Tk()
root.title(" ")
root.geometry("500x100")
label = tk.Label(root,text="GAME OVER",font=("Ricty Diminished",20))
label.pack()


class Dai(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN.bottom           # 台のy座標

    def update(self):
        key_states = pg.key.get_pressed() #台の移動
        if key_states[pg.K_LEFT]: 
            self.rect.centerx -= 10
        if key_states[pg.K_RIGHT]: 
            self.rect.centerx += 10                  


class Tama(pygame.sprite.Sprite):
    def __init__(self, filename, dai, blocks, speed):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.dx = self.dy = 0  # たまの速度
        self.dai = dai  # 台への参照
        self.blocks = blocks  
        self.update = self.start # ゲーム開始状態に更新
        self.speed = speed # 玉の初期速度 

    def start(self):
        # 玉の初期位置
        self.rect.centerx = self.dai.rect.centerx
        self.rect.bottom = self.dai.rect.top
        # 玉射出
        if pygame.mouse.get_pressed()[0] == 1:
            self.dx = 0
            self.dy -= self.speed
            self.update = self.move
    # 玉の挙動
    def move(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        # 壁との反射
        if self.rect.left < SCREEN.left:    # 左側      
            self.dx *= -1             
        if self.rect.right > SCREEN.right:  # 右側       
            self.dx *= -1
        if self.rect.top < SCREEN.top:      # 上側  
            self.dy *= -1
        if self.rect.colliderect(self.dai.rect) and self.dy > 0:      
            self.dx = self.speed
            self.dy *= -1                 

        # ボールを落とした場合
        if self.rect.top > SCREEN.bottom:
            self.update = self.start
            root.mainloop()
            sys.exit()

        blocks_collided = pygame.sprite.spritecollide(self, self.blocks, True)
        if blocks_collided:  # 衝突ブロックがある場合
            for block in blocks_collided:
                # ボールが左からブロックへ衝突した場合
                if self.rect.left < block.rect.left and self.rect.right < block.rect.right:
                    self.dx *= -1
                # 右
                if block.rect.left < self.rect.left and block.rect.right < self.rect.right:
                    self.dx *= -1

                # 上
                if self.rect.top < block.rect.top and self.rect.bottom < block.rect.bottom:
                    self.dy *= -1
                # 下
                if block.rect.top < self.rect.top and block.rect.bottom < self.rect.bottom:
                    self.dy *= -1


# ブロックのクラス
class Block(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        # ブロックの左上座標
        self.rect.left = SCREEN.left + x * self.rect.width
        self.rect.top = SCREEN.top + y * self.rect.height



def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN.size)
    group = pygame.sprite.RenderUpdates()  
    blocks = pygame.sprite.Group()   

    Dai.containers = group
    Tama.containers = group
    Block.containers = group, blocks

    # パドルの作成
    dai = Dai("C:/Users/81808/Documents/ProjExD2022/fig/bar128x32.png")

    # ブロックの作成
    for x in range(1, 18):
        for y in range(1, 11):
            Block("C:/Users/81808/Documents/ProjExD2022/fig/block_purple64x24.png", x, y)

    # 玉を作成
    Tama("C:/Users/81808/Documents/ProjExD2022/fig/ball32x32.png",
         dai, blocks, 10)
    
    clock = pygame.time.Clock()

    while (1):
        clock.tick(60)    
        screen.fill((0,20,0))
        group.update()    
        group.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()