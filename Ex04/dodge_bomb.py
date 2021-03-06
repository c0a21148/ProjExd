import random 
import pygame as pg
import sys
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("GAME OVER")
    root.geometry("500x200")

    label1 = tk.Label(root,text="下手くそ!",font=("Ricty Diminished",80))
    #label2 = tk.Label(root,text=f"{time}",font=("Ricty Diminished",80))
    label1.pack()
    #label2.pack()

    clock = pg.time.Clock()
    a =5
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600,900)) #surface
    screen_rct = screen_sfc.get_rect()

    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    bgimg_rct = bgimg_sfc.get_rect()

    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    kkimg_sfc = pg.image.load("fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900,400

    bmimg_sfc = pg.Surface((20,20))
    bmimg_sfc.set_colorkey((0,0,0))

    pg.draw.circle(bmimg_sfc,(255,0,0),(10,10),10)
    
    bmimg_rct = bmimg_sfc.get_rect()
    bmimg_rct.centerx = random.randint(0,screen_rct.width)
    bmimg_rct.centery = random.randint(0,screen_rct.height)
    vx,vy = +1,+1

    



    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        screen_sfc.blit(kkimg_sfc,kkimg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] : kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN] : kkimg_rct.centery += 1
        if key_states[pg.K_LEFT] : kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] : kkimg_rct.centerx += 1
        if check_bound(kkimg_rct,screen_rct) != (1,1):
            if key_states[pg.K_UP] : 
                kkimg_rct.centery += 1
                
            if key_states[pg.K_DOWN] : 
                kkimg_rct.centery -= 1
                
            if key_states[pg.K_LEFT] : 
                kkimg_rct.centerx += 1
                
            if key_states[pg.K_RIGHT]: 
                kkimg_sfc.centerx -= 1
        if key_states[pg.K_s] : 
            vx *= 1.01
            vy *= 1.01
        if key_states[pg.K_a] == True: 
            x1 = bmimg_rct.centerx
            y1 = bmimg_rct.centery
            a += 1
            bmimg_sfc = pg.Surface((20 + a,20 + a))
            bmimg_sfc.set_colorkey((0,0,0))
            pg.draw.circle(bmimg_sfc,(255,0,0),(10+a/2,10+a/2),10+a/2)
            bmimg_rct =bmimg_sfc.get_rect()
            bmimg_rct.centerx = x1
            bmimg_rct.centery = y1

        if key_states[pg.K_d] == True: 
            x1 = bmimg_rct.centerx
            y1 = bmimg_rct.centery
            a -= 1
            bmimg_sfc = pg.Surface((20 + a,20 + a))
            bmimg_sfc.set_colorkey((0,0,0))
            pg.draw.circle(bmimg_sfc,(255,0,0),(10+a/2,10+a/2),10+a/2)
            bmimg_rct =bmimg_sfc.get_rect()
            bmimg_rct.centerx = x1
            bmimg_rct.centery = y1


        screen_sfc.blit(kkimg_sfc,kkimg_rct)
        bmimg_rct.move_ip(vx,vy)
        screen_sfc.blit(bmimg_sfc,bmimg_rct)
        yoko,tate = check_bound(bmimg_rct,screen_rct)
        vx *= yoko
        vy *= tate

        if kkimg_rct.colliderect(bmimg_rct) == True: #こうかとんが爆弾と重なると
            kkimg_sfc = pg.image.load("fig/3.png")
            root.mainloop()
            


        pg.display.update()
        clock.tick(1000)

def check_bound(rct,scr_rct):
    '''
    [1] rct:こうかとん or 爆弾のrect
    [2] scr_rct:スクリーンのrect
    '''
    yoko,tate = +1,+1
    if rct.left < scr_rct.left or scr_rct.right < rct.right : 
        yoko = -1
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom : 
        tate = -1
    return yoko,tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
