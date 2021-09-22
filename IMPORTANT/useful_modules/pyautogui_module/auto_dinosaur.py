import pyautogui
from PIL import ImageGrab
from PIL import ImageOps
from numpy import *
import time

# Auto finding game in Chrome
pyautogui.PAUSE = 1

pyautogui.hotkey('winleft', 'q')
pyautogui.write('chrome\n', 0.1)
pyautogui.hotkey('winleft', 'up')
pyautogui.write('t-rex game\n', 0.1)
pyautogui.click(321, 777)

# Itself auto-dino game

dinosaur = (615, 653)

def restartGame():
    pyautogui.keyDown('space')
    print('Game is restarted')

def image_grab():
    box = (dinosaur[0] + 55, dinosaur[1], dinosaur[0] + 145, dinosaur[1] + 5)
    image = ImageGrab.grab(box)
    grabImage = ImageOps.grayscale(image)
    a = array(grabImage.getcolors())
    return a.sum()


time.sleep(4)
restartGame()

while True:
    image_grab()
    if(image_grab() != 697):
        pyautogui.PAUSE = 0.1
        pyautogui.press('space')