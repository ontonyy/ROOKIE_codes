from ursina import *

app = Ursina()

dx = .2
up_wall = Entity(model='quad', position=(0, 10, 0), scale=(36, 0.5, 0), collider='box')
down_wall = Entity(model='quad', position=(0, -10, 0), scale=(36, 0.5, 0), collider='box')
right_wall = Entity(model='quad', position=(18, 0, 0), scale=(0.5, 20, 0), collider='box')
left_wall = Entity(model='quad', position=(-18, 0, 0), scale=(0.5, 20, 0), collider='box')

points = []
point = Entity(model='sphere', color=color.random_color(), position=(random.uniform(-17, 17), random.uniform(-9.5, 9.5)), collider='box')
points.append(point)

score = 0
snakes = []
snake = Entity(model='quad', position=(0, 0, 0), scale=3, collider='box', texture='snake.png')
snakes.append(snake)

camera.position = (0, 0, -50)


def update():
    global point, points, score, snake, snakes

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
        for x in snakes:
            if hit_info.entity == x:
                end_game(f'YOU LOSE! Score: {score}')
        if hit_info.entity == point:
            score += 1
            destroy(hit_info.entity)

            point = Entity(model='sphere', color=color.random_color(), position=(random.uniform(-16.5, 16.5), random.uniform(-8.5, 8.5)), collider='box')
            points.append(point)

            snake = Entity(model='quad', position=(random.uniform(-16.5, 16.5), random.uniform(-8.5, 8.5)), color=color.random_color(), scale=3, collider='box', texture='snake.png')
            snakes.append(snake)

        if hit_info.entity == up_wall or hit_info.entity == down_wall or hit_info.entity == left_wall or hit_info.entity == right_wall:
            end_game(f'YOU LOSE! Score: {score}')


def end_game(user_message):
    message = Text(text=user_message, background=True, scale=2, color=color.yellow, position=(-0.25, 0, 0))
    application.pause()


EditorCamera()
app.run()