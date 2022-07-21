from ursina import *

app = Ursina()

camera.orthographic = True
camera.fov = 4
camera.position = (1, 1)

player = Entity(name='O', color=color.azure)
cursor = Cursor(color=player.color, origin=(0, 0), scale=.08, enabled=True)

bg = Entity(parent=scene, model='quad', texture='shore', scale=(16, 8), z=10, color=color.magenta)

board = [[None for x in range(3)] for y in range(3)]

for y in range(3):
    for x in range(3):
        b = Button(parent=scene, position=(x, y))
        board[x][y]=b

        def on_click(b=b):
            b.text = player.name
            b.color = player.color
            b.collision = False

            if player.name == 'O':
                player.name = 'X'
                player.color = color.orange
            else:
                player.name = "O"
                player.color = color.azure

            cursor.text = ''
            cursor.color = player.color
        b.on_click = on_click

def victorycheck():

    name = player.name
    won = (
        (board[0][0] == name and board[1][0] == name and board[2][0] == name),
        (board[0][2].text == name and board[0][1].text == name and board[0][0].text == name)
    )
    if won:
        print("Winner is", name)


app.run()