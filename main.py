import pygame as pg
import time

WIDTH = 800
HEIGHT = 600

def change_direction(dx, dy):
    if dx == 1:
        return (0, -1)
    elif dx == -1:
        return (0, 1)
    elif dy == 1:
        return (-1, 0)
    elif dy == -1:
        return (-1, 0)

def draw(display):
    c = 1
    n = 1
    dx = 1
    dy = 0
    x = WIDTH//2
    y = HEIGHT//2
    surface = FONT.render(str(0), True, (255, 0, 0))
    display.blit(surface, (x, y))

    for i in range(1, 30):
        x += dx*30
        y += dy*30
        print((dx, dy))
        surface = FONT.render(str(i), True, (255, 0, 0))
        display.blit(surface, (x, y))
        c -= 1
        if c == 0:
            print('chuj')
            dx, dy = change_direction(dx, dy)
            c = n
            n += 1
        pg.display.flip() 
        time.sleep(1)

                

        



        


    

def events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()





if __name__ == '__main__':
    pg.init()
    pg.font.init()
    display = pg.display.set_mode(size=(WIDTH, HEIGHT))
    CLOCK = pg.time.Clock()
 
    FONT = pg.font.SysFont('Comic Sans ms', 16)


    while True:
        CLOCK.tick(1)
        draw(display)
        events()

        
