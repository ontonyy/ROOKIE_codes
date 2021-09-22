# Some actions with cube, for instance: movements, color changing, rotating, new cubes

from ursina import *
import random

app = Ursina()


def update():    # Movements with main CUBE
    if held_keys['a']:
        cube.rotation_y += time.dt * 100
    elif held_keys['d']:
        cube.rotation_y -= time.dt * 100
    elif held_keys['w']:
        cube.rotation_x += time.dt * 100
    elif held_keys['s']:
        cube.rotation_x -= time.dt * 100

    cube.x += held_keys['right arrow'] * .1
    cube.x -= held_keys['left arrow'] * .1
    cube.y += held_keys['up arrow'] * .1
    cube.y -= held_keys['down arrow'] * .1


def input(key):
    if key == 'f':
        red = random.random() * 255
        green = random.random() * 255
        blue = random.random() * 255
        cube.color = color.rgb(red, green, blue)

    if key == 'c':
        x = random.random() * 12 - 7     # Value between -5 and 5
        y = random.random() * 9 - 4     # Value between -5 and 5
        z = random.random() * 10 - 5     # Value between -5 and 5
        s = random.random() * 1          # Scale between 0 and 1
        newcube = Entity(model='cube', color=color.random_color(), position=(x, y, z), scale=(s, s, s), texture='white_cube', rotation = Vec3(random.uniform(-180, 180), random.uniform(-180, 180), random.uniform(-180, 180)))
        cubes.append(newcube)

    if key == 'left mouse down':
        for x in cubes:
            destroy(x)

cubes = []
cube = Entity(model='cube', scale=(2, 2, 2), texture='white_cube')
text = Text(text="CUBE | press c or f |", position=(-0.18, 0.45, 0), color=color.green, scale=1.5)
text2 = Text(text="To destroy mini-cubes press LMD", scale=1.3, color=color.random_color(), position=(-0.23, -0.45))

app.run()