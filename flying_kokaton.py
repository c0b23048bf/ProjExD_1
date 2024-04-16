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
    c_img = pg.image.load("fig/3.png")
    
    #こうかとん座標設定
    c_img = pg.transform.flip(c_img, True, False)
    c_img_rct = c_img.get_rect()
    c_img_rct.center = 300,200
    
    tmr,bg_x,bg_y,bg_ax,bg_ay,c_x ,c_y = 0,0,0,1600,0,0,0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        #背景画像blit
        screen.blit(bg_img, [bg_x, bg_y])
        screen.blit(bg_img,[bg_ax,bg_ay])
        
        tmr += 1
        bg_x -= 1
        bg_ax -= 1
        c_x,c_y = 0,0
        
        #背景ループ
        if bg_x <= -1600:
            bg_x = 0
            bg_ax = 1600
        
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