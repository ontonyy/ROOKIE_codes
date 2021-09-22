from ursina import *
from random import *

app = Ursina()

score = 0

up_wall = Entity(model='quad', position=(0, 4, 0), scale=(15, 0.5, 0), color=color.green, collider='box')
left_wall = Entity(model='quad', position=(-7.1, 0, 0), scale=(0.5, 8, 0), color=color.green, collider='box')
right_wall = Entity(model='quad', position=(7.1, 0, 0), scale=(0.5, 8, 0), color=color.green, collider='box')
main = Entity(model='quad', position=(0, -4, 0), scale=(3, 0.5, 0), color=color.green, collider='box')
ball = Entity(model='circle', scale=.5, color=color.blue, position=(0, 0, 0), collider='box', rotation_z=90, speed=10)

bricks = []
for x in range(-5, 6):
    for y in range(-1, 3):
        brick = Entity(model='quad', position=(x, y, 0), scale=(0.6, 0.3), color=color.magenta, collider='box')
        bricks.append(brick)


def update():
    global score
    main.x += held_keys['right arrow'] * time.dt * 7
    main.x -= held_keys['left arrow'] * time.dt * 7

    ball.position += ball.right * time.dt * ball.speed

    hit_info = ball.intersects()
    if hit_info.hit:
        if hit_info.entity == main:
            delta = main.x - ball.x
            ball.rotation_z = 270 - delta * 50
            ball.speed *= 1.02
        if hit_info.entity == up_wall:
            ball.rotation_z = - ball.rotation_z
        if hit_info.entity == left_wall or hit_info.entity == right_wall:
            ball.rotation_z = 180 - ball.rotation_z
        if hit_info.entity in bricks:
            ball.rotation_z = - ball.rotation_z
            destroy(hit_info.entity)
            score += 1
        if score >= 44:
            end_game('YOU WIN')
    if ball.position.y < -5:
        end_game('YOU LOSE. SCORE: ' + str(score))


def end_game(user_message):
    message = Text(text=user_message, scale=2, origin=(0, 0), color=color.green, background=True)
    application.pause()


EditorCamera()
app.run()
