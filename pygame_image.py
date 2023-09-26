import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    bg_img2 = pg.transform.flip(bg_img,True, False)
    kk_img2 = pg.transform.rotozoom(kk_img, 10, 1.0)
    lst1= pg.transform.rotozoom(kk_img, 2, 1.0)
    lst2 = pg.transform.rotozoom(kk_img, 4, 1.0) 
    lst3 = pg.transform.rotozoom(kk_img, 6, 1.0) 
    lst4 = pg.transform.rotozoom(kk_img, 8, 1.0) 
    lst5 = pg.transform.rotozoom(kk_img, 10, 1.0)
    lst6 = pg.transform.rotozoom(kk_img, 12, 1.0)
    lst7 = pg.transform.rotozoom(kk_img, 16, 1.0)
    lst8 = pg.transform.rotozoom(kk_img, 18, 1.0)
    lst9 = pg.transform.rotozoom(kk_img, 20, 1.0)
    lst10 = pg.transform.rotozoom(kk_img, 22, 1.0)
    lst11 = pg.transform.rotozoom(kk_img, 24, 1.0)
    lst12 = pg.transform.rotozoom(kk_img, 26, 1.0)
    lst13 = pg.transform.rotozoom(kk_img, 28, 1.0)
    lst14 = pg.transform.rotozoom(kk_img, 30, 1.0)
    lst15 = pg.transform.rotozoom(kk_img, 32, 1.0) 
    
    
    
    kk_imgs = [kk_img, kk_img2, lst1, lst2, lst3, lst4, lst5, lst6, lst7, lst8, lst9, lst10, lst11, lst12, lst13, lst14, lst15, lst14, lst13, lst12, lst11, lst10, lst9, lst8, lst8, lst7, lst6, lst5, lst4, lst3, lst2, lst1]
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 3200
        screen.blit(bg_img, [-x , 0])
        #screen.blit(bg_img, [1600 - x, 0])
        screen.blit(bg_img2, [1600 -x, 0])
        screen.blit(bg_img, [3200, 0])
        screen.blit(kk_imgs[tmr%32], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()