from turtle import *
from math import sqrt
import random

def draw_tile(x, y, type_index):
    if type_index == 1:
        setpos(x, y+size)
        seth(270)
    elif type_index == 2:
        setpos(x+size, y+size)
        seth(180)
    elif type_index == 3:
        setpos(x, y)
        seth(0)
    elif type_index == 4:
        setpos(x+size, y)
        seth(90)
    pendown()
    begin_fill()
    forward(size)
    lt(135)
    forward(size*sqrt(2))
    lt(135)
    forward(size)
    end_fill()
    penup()

def draw_tiles():
    for i in range(0, 505, size):
        for j in range(0, 505, size):
            draw_tile(i, j, random.choice([1, 2, 3, 4]))
    #draw_tile(0, 0, 1)
    #draw_tile(100, 100, 1)
    #draw_tile(100, 200, 2)
    #draw_tile(100, 300, 3)
    #draw_tile(100, 400, 4)

if __name__ == "__main__":
    print(f'{window_height()}, {window_width()}')
    mode("world")
    screensize(1920,1080)
    setworldcoordinates(-5, -5, (2460)+5, (1440)+5)
    setup(width=600, height=600, startx=None, starty=None)
    penup()

    size = 50
    speed(0)

    ontimer(draw_tiles, 5000)
    mainloop()