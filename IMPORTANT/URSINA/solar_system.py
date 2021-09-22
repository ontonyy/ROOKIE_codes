# Some tries to do solar system

from ursina import *
import numpy as np

app = Ursina()


def update():
    global p
    p += .02
    angle = np.pi * 40 / 180

    radius_1 = 1
    Mercury.x = np.cos(p) * radius_1
    Mercury.z = np.cos(p) * radius_1

    radius_2 = 1.4
    Venus.x = np.cos(p + angle) * radius_2
    Venus.z = np.cos(p + angle) * radius_2

    radius_3 = 1.8
    Earth.x = np.cos(p + angle * 2) * radius_3
    Earth.z = np.cos(p + angle * 2) * radius_3

    radius_4 = 2.2
    Mars.x = np.cos(p + angle * 3) * radius_4
    Mars.z = np.cos(p + angle * 3) * radius_4

    radius_5 = 2.6
    Jupiter.x = np.cos(p + angle * 4) * radius_5
    Jupiter.z = np.cos(p + angle * 4) * radius_5

    radius_6 = 3
    Saturn.x = np.cos(p + angle * 5) * radius_6
    Saturn.z = np.cos(p + angle * 5) * radius_6

    radius_7 = 3.4
    Uranus.x = np.cos(p + angle * 6) * radius_7
    Uranus.z = np.cos(p + angle * 6) * radius_7

    radius_8 = 3.8
    Neptune.x = np.cos(p + angle * 7) * radius_8
    Neptune.z = np.cos(p + angle * 7) * radius_8


Sun = Entity(model='sphere', color=color.yellow, position=(0, 0, 0))

Mercury = Entity(model='sphere', color=color.red, scale=.1)
Venus = Entity(model='sphere', color=color.orange, scale=.18)
Earth = Entity(model='sphere', color=color.green, scale=.19)
Mars = Entity(model='sphere', color=color.brown, scale=.12)
Jupiter = Entity(model='sphere', color=color.gray, scale=.5)
Saturn = Entity(model='sphere', color=color.white, scale=.4)
Uranus = Entity(model='sphere', color=color.cyan, scale=.3)
Neptune = Entity(model='sphere', color=color.blue, scale=.28, )

p = -np.pi
camera.rotation = (0, 0, 30)

app.run()
