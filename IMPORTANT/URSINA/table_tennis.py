# Ping pong game, if paddle go away from table, the ball start moving very weird

from ursina import *
from random import uniform

app = Ursina()

window.color = color.cyan
table = Entity(model='cube', color=color.blue, scale=(10, 0.5, 14),
               position=(0, 0, 0), texture="white_cube", rotation=(-35, 0, 0))
line = Entity(parent=table, model='quad', scale=(0.88, 0.2, 0.1), position=(0, 3.5, -0.20))
ball = Entity(parent=table, model='sphere', color=color.red, scale=.05,
              position=(0, 3.71, -0.2), collider='box')

player_A = Entity(parent=table, model='quad', collider='box', color=color.black, scale=(0.2, 0.5, 0.05), position=(0, 3.7, 0.25))
player_B = duplicate(player_A, z=-0.6)

score_A = 0
score_B = 0

Text(text='Player A', color=color.black, position=(-.1, .32), scale=2)
Text(text='Player B', color=color.black, position=(-.1, -.4), scale=2)
dx = 0.2
dz = 0.3
speed = .7

def update():
    global dx, dz, score_A, score_B

    # Paddles moving
    if held_keys['a']:
        player_A.x += time.dt * speed
    if held_keys['d']:
        player_A.x -= time.dt * speed
    if held_keys['left arrow']:
        player_B.x += time.dt * speed
    if held_keys['right arrow']:
        player_B.x -= time.dt * speed

    # Game pausing
    if held_keys['space']:
        application.pause()

    ball.x += time.dt*dx
    ball.z += time.dt*dz

    # Checking if ball and paddles move through field
    if abs(ball.x) > .4:
        dx = -dx


    # Ball scoring, and score increasing
    if ball.z < -0.65:
        score_A += 1
        print_on_screen(f'Player A : Player B = {score_A} : {score_B}', position=(-.85, .4), scale=2, duration=2)
        reset()

    if ball.z > 0.25:
        score_B += 1
        print_on_screen(f'Player A : Player B = {score_A} : {score_B}', position=(-.85, .4), scale=2, duration=2)
        reset()

    # Ball hitting into walls

    if abs(player_A.x) > .4 or abs(player_B.x) > .4:
        dx = -dx

    # Ball hitting with player's paddles

    hit_info = ball.intersects()
    if hit_info.hit:
        if hit_info.entity == player_A or hit_info.entity == player_B:
            dz = -dz


def reset():
    ball.x = 0
    ball.z = -0.2


camera.position = (0, 0, -35)
camera.rotation_x = 0

EditorCamera()
app.run()