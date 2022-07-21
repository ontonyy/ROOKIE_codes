from ursina import *

app = Ursina()

balls = []

for _ in range(20):
    ball = Entity(
        model='sphere',
        color=color.random_color(),
        texture='sphere'
    )
    ball.x = random.randint(-7, 7)
    ball.y = random.randint(-4, 4)
    ball.dx = random.uniform(0.01, 0.10)
    ball.dy = random.uniform(0.01, 0.10)
    balls.append(ball)

def update():
    for ball in balls:
        ball.x += ball.dx
        ball.y += ball.dy
        if ball.x > 7:
            ball.x = 7
            ball.dx *= -1
            ball.color=color.random_color()
        if ball.x < -7:
            ball.x = -7
            ball.dx *= -1
            ball.color = color.random_color()

        if ball.y > 4:
            ball.y = 4
            ball.dy *= -1
            ball.color = color.random_color()
        if ball.y < -4:
            ball.y = -4
            ball.dy *= -1
            ball.color = color.random_color()

    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            ball1 = balls[i]
            ball2 = balls[j]
            x = ball1.x - ball2.x
            y = ball1.y - ball2.y
            d = (x**2) + (y**2) ** 0.5
            if d < 1:
                ball1.dx, ball2.dx = ball2.dx, ball1.dx
                ball1.dy, ball2.dy = ball2.dy, ball1.dy

app.run()