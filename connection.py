import pgzrun
import time

from pgzrun import *
from random import randint

WIDTH = 600
HEIGHT = 600

dots = []
lines = []

next_dot = 0
start_time = 0

for dot in range(0, 10):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)

result_message = ""

def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        dot.draw()
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))        
        number = number + 1

    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))

    screen.draw.text(result_message, (WIDTH // 6, 10), color="white")

def on_mouse_down(pos):
    global next_dot
    global lines
    global result_message
    global start_time

    if next_dot < len(dots):
        if dots[next_dot].collidepoint(pos):
            if next_dot == 0:
                start_time = time.time()
            if next_dot:
                lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
            next_dot = next_dot + 1
            if next_dot == len(dots):
                end_time = time.time()
                elapsed_time = round(end_time - start_time, 2)
                result_message = f"You successfully connected the numbers in {elapsed_time} seconds!"
        else:
            lines = []
            next_dot = 0    

pgzrun.go()
