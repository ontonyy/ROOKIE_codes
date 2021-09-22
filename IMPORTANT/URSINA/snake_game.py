from ursina import *
from random import randint
import numpy as np

app = Ursina()

dx = .2
points = []
point = Entity(model='sphere', color=color.random_color(), position=(random.uniform(-17, 17), random.uniform(-9.5, 9.5)), collider='box')
points.append(point)

score = 0
snake = Entity(model='sphere', position=(0, 0, 0), scale=(1, 1, 0), collider='box', texture='white_cube')
snakes = [snake]
up_wall = Entity(model='quad', position=(0, 10, 0), scale=(36, 0.5, 0), collider='box')
down_wall = Entity(model='quad', position=(0, -10, 0), scale=(36, 0.5, 0), collider='box')
right_wall = Entity(model='quad', position=(18, 0, 0), scale=(0.5, 20, 0), collider='box')
left_wall = Entity(model='quad', position=(-18, 0, 0), scale=(0.5, 20, 0), collider='box')

camera.position = (0, 0, -50)


def update():
    global point, points, score, snake
    if held_keys['left arrow']:
        snake.x -= dx
        snake.rotation_z = 0
    elif held_keys['right arrow']:
        snake.x += dx
        snake.rotation_z = 0
    elif held_keys['up arrow']:
        snake.y += dx
        snake.rotation_z = 90
    elif held_keys['down arrow']:
        snake.y -= dx
        snake.rotation_z = 90

    hit_info = snake.intersects()
    if hit_info.hit:
        if hit_info.entity == point:
            score += 1
            destroy(hit_info.entity)
            point = Entity(model='sphere', color=color.random_color(), position=(random.uniform(-17, 17), random.uniform(-9, 9)), collider='box')
            points.append(point)

        if hit_info.entity == up_wall or hit_info.entity == down_wall or hit_info.entity == left_wall or hit_info.entity == right_wall:
            end_game(f'YOU LOSE! Score: {score}')


def input(key):
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    if key == 'left arrow':
        snake.color = color.rgb(R, G, B)
    if key == 'right arrow':
        snake.color = color.rgb(R, G, B)
    if key == 'up arrow':
        snake.color = color.rgb(R, G, B)
    if key == 'down arrow':
        snake.color = color.rgb(R, G, B)


def end_game(user_message):
    message = Text(text=user_message, background=True, scale=2, color=color.yellow, position=(-0.25, 0, 0))
    application.pause()


EditorCamera()
app.run()
