# Cube clicker, to be honest, one click destroying all cubes, IDK how to do more ideal
import random

from ursina import *

app = Ursina()

def input(key):
    if key == 'c':
        x = random.uniform(-0.8, 0.8)   # Рандомная позиция куба
        y = random.uniform(-0.5, 0.5)
        z = random.uniform(-0.5, 0.5)
        s = random.uniform(-0.3, 0.3)
        ri = random.randint(-360, 360) # Рандомная ротация куба
        newclick = Button(model='cube', color=color.random_color(), position=(x, y, z), scale=(s, s, s), texture='white_cube', rotation=(ri, ri, ri))
        clicks.append(newclick)

    if key == 'left mouse down':
        for x in clicks:
            destroy(x)

text = Text(text="Press 'c' for destroing this enemies", scale=1.5, position=(-0.3, 0.48, 0), color=color.magenta)
clicks = []

app.run()