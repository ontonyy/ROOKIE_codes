import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.click(1738, 15, clicks=3)

pyautogui.moveTo(955, 210, duration=1)
pyautogui.dragTo(1846, 710, duration=1)
