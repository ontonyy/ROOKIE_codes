from ursina import *
import random

def update():
    global dx
    ball.x += dx
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    hit_info = ball.intersects()
    if hit_info.hit:
        dx = -dx
        ball.color = color.random_color()
        if hit_info.entity in boxes:
            hit_info.entity.color = color.rgb(R, G, B)
            hit_info.entity.color = color.rgb(R, G, B)




app = Ursina()

ball = Entity(model='sphere', color=color.white, position=(0, 0, 0), scale=.5, collider='box')
boxes = []
box1 = Entity(model='cube', color=color.white, scale=(2, 4, 2), texture='white_cube', position=(4, 0, 0), collider='box')
box2 = duplicate(box1, x=-4, texture='brick')
dx = .05
boxes.append(box1)
boxes.append(box2)



app.run()