import time
import pyautogui

# Understood that in russian cannot write anything

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.hotkey('winleft', 'q')
pyautogui.write('chrome\n', 0.1)
pyautogui.hotkey('winleft', 'up')
pyautogui.write('valeri moiseev Narva\n', 0.1)
pyautogui.click(448, 310)

# Slow scrolling down page
for _ in range(1, 150):
    pyautogui.PAUSE = 0.05
    pyautogui.scroll(-10)

time.sleep(3)
