import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    #スクリーン設定
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    
    #背景画像とこうかとん
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img2, True, False)
    
    #こうかとん座標設定
    c_img = pg.image.load("fig/3.png")
    c_img = pg.transform.flip(c_img, True, False)
    c_img_rct = c_img.get_rect()
    c_img_rct.center = 300,200
    
    tmr,c_x ,c_y = 0,0,0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        #背景画像blit
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg_img2, [-x+4800, 0]) 
        
        tmr += 1
        c_x,c_y = 0,0
        
        #こうかとんボタン操作
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            c_y += -1
        elif key_lst[pg.K_DOWN]:
            c_y += 1
        elif key_lst[pg.K_RIGHT]:
            c_x += 2
        elif key_lst[pg.K_LEFT]:
            c_x += -1
        else:
            c_x += -1
        c_img_rct.move_ip((c_x,c_y))
        screen.blit(c_img,c_img_rct)
            
        clock.tick(200)
        pg.display.update()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()