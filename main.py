import pygame as pg
import time

WIDTH = 800
HEIGHT = 600
drawn = False

def prime(n):
    for i in range(2, n//2):
        if n%i == 0:
            return False
    return True


def change_direction(dx, dy):
    if dx == 1:
        print('gora')
        return (0, -1)
    elif dx == -1:
        print('dol')
        return (0, 1)
    elif dy == 1:
        print('prawo')
        return (1, 0)
    elif dy == -1:
        print('lewo')
        return (-1, 0)

def draw(display):
    global drawn
    c = 2
    n = 2
    dx = 1
    dy = 0
    x = WIDTH//2
    y = HEIGHT//2
    surface = FONT.render(str(2), True, (255, 0, 0))
    display.blit(surface, (x, y))

    if drawn:
        return
    for i in range(3, 10000):
        x += dx*5
        y += dy*5
        print((dx, dy))
        if prime(i):
            rect = pg.Rect((x, y), (5, 5))
            pg.draw.rect(display, (255, 0, 0), rect)
        c -= 1
        if c == 0:
            dx, dy = change_direction(dx, dy)
            c = n
            n += 1
     
        pg.display.flip()
    
    drawn = True

                

        



        


    

def events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()





if __name__ == '__main__':
    pg.init()
    pg.font.init()
    display = pg.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pg.time.Clock()
 
    FONT = pg.font.SysFont('Comic Sans ms', 3)


    while True:
        CLOCK.tick(144)
        draw(display)
        events()

        
