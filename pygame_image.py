import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    c_img = pg.image.load("fig/3.png")
    c_img = pg.transform.flip(c_img, True, False)
    c_img_rct = c_img.get_rect()
    c_img_rct.center = 300,200
    tmr = 0
    bg_x = 0
    bg_y = 0
    bg_ax = 1600
    bg_ay = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [bg_x, bg_y])
        screen.blit(bg_img,[bg_ax,bg_ay])
        tmr += 1
        bg_x -= 1
        bg_ax -= 1
        
        if bg_x <= -1600:
            bg_x = 0
            bg_ax = 1600
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            c_img_rct.move_ip((0, -1))
        if key_lst[pg.K_DOWN]:
            c_img_rct.move_ip((0,1))
        if key_lst[pg.K_RIGHT]:
            c_img_rct.move_ip((1,0))
        if key_lst[pg.K_LEFT]:
            c_img_rct.move_ip((-1,0))
        screen.blit(c_img,c_img_rct)
        #bg_y = 0        
        clock.tick(200)
        pg.display.update()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()