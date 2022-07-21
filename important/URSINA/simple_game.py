from ursina import *

app = Ursina()

window.color = color.black

up_wall = Entity(model='quad', position=(0, 4.3, 0), scale=(36, 0.5, 0), collider='box')
down_wall = Entity(model='quad', position=(0, -4.3, 0), scale=(36, 0.5, 0), collider='box')
right_wall = Entity(model='quad', position=(7.5, 0, 0), scale=(0.5, 20, 0), collider='box')
left_wall = Entity(model='quad', position=(-7.5, 0, 0), scale=(0.5, 20, 0), collider='box')

paddle1 = Entity(model='quad', color=color.white, scale=(0.1, 1.5, 0), position=(-7, 0, 0), collider='box')
paddle2 = duplicate(paddle1, x=7)
ball = Entity(model='circle', scale=.3, position=(0, 0, 0), collider='box', rotation_z=90)
speed = 5
dx = 5
dy = 1
score1 = 0
score2 = 0
text1 = Text(text='PLAYER 1', position=(-0.85, 0.47, 0), scale=1.5)
text2 = Text(text='PLAYER 2', position=(0.65, 0.47, 0), scale=1.5)


def update():
    global dx, dy, score1, score2
    if held_keys['w']:
        paddle1.y += time.dt * speed
    if held_keys['s']:
        paddle1.y -= time.dt * speed
    if held_keys['up arrow']:
        paddle2.y += time.dt * speed
    if held_keys['down arrow']:
        paddle2.y -= time.dt * speed

    ball.x += time.dt * dx
    ball.y += time.dt * dy

    hit_info = ball.intersects()
    if hit_info.hit:
        if hit_info.entity == paddle1 or hit_info.entity == paddle2:
            dx = -dx

        if hit_info.entity == up_wall or hit_info.entity == down_wall:
            dy = -dy

        if hit_info.entity == right_wall:
            score1 += 1
            print_on_screen(f"{score1} : {score2}", position=(-0.15, 0.4, 0), scale=7)
            reset()

        if hit_info.entity == left_wall:
            score2 += 1
            print_on_screen(f"{score1} : {score2}", position=(-0.15, 0.4, 0), scale=7)
            reset()



def reset():
    ball.x = 0
    ball.y = random.uniform(-0.8, 0.8)

EditorCamera()
app.run()