from ursina import *


def update():
    vinni.x += held_keys['right arrow'] * .1
    vinni.x -= held_keys['left arrow'] * .1
    vinni.y += held_keys['up arrow'] * .1
    vinni.y -= held_keys['down arrow'] * .1
    gera.x += held_keys['d'] * .1
    gera.x -= held_keys['a'] * .1
    gera.y += held_keys['w'] * .1
    gera.y -= held_keys['s'] * .1

app = Ursina()

vinni = Entity(model='quad', texture="anton.png", position=(-4, 0))

gera = Entity(model='quad', texture='gera.png', position=(4, 0))

txt = Text(text="FRIENDS GAME, FIRST TRIES", position=(-0.35, 0.4, 0), color=color.yellow, scale=2)

Text.size = 0.05
Text.default_resolution = 1080 * Text.size
info = Text(text="A powerful waterfall roaring on the mountains")
info.x = -0.5
info.y = 0.4
info.background = True
info.visible = False        # Do not show this text

app.run()
