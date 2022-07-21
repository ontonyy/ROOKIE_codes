from ursina import *

def update():
    global speed
    cube.x += time.dt * speed
    if abs(cube.x) > 3:
        speed *= -1
    cube.rotation_z += time.dt * (speed * 100)
    cube.rotation_y += time.dt * (speed * 100)

app = Ursina()


speed = 2
cube = Entity(model='cube', texture='white_cube', color=color.magenta)
camera.position = (0, 0, -10)

app.run()