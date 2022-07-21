from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

gera_texture = load_texture('vinni.png')
anton_texture = load_texture('anton.png')
arm_texture = load_texture('arm.png')
block_pick = 1

def update():
    global block_pick
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=anton_texture):
        super().__init__(
            model='cube',
            color=color.color(0, 0, random.uniform(0.9, 1)),
            position=position,
            parent=scene,
            texture=texture,
            origin_y=1,
            scale=1,
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal, texture=anton_texture)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture=gera_texture)

            if key == 'right mouse down':
                destroy(self)


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='cube',
            texture=arm_texture,
            scale=(0.15, 0.5, 0.1),
            position=Vec2(0.4, -0.3),
            rotation=Vec3(-10,60,5),
        )


for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
hand = Hand()

app.run()
