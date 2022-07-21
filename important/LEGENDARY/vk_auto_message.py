from datetime import datetime
import pyautogui as gui
import time

def enter_vk():
	gui.PAUSE = 1.5
	gui.hotkey('winleft', 'q')
	gui.write('Chrome\n', 0.1)
	gui.hotkey('winleft', 'up')
	gui.write('vk.com\n', 0.1)
	gui.dragTo(325, 348)
	gui.click(325, 348)
	gui.dragTo(873, 367)
	gui.click(873, 367)
	time_check()

def time_check():
	e = time.strftime('%H')
	if int(e) < 12:
		gui.write('Good morning', 0.1)
	elif 12 < int(e) < 18:
		gui.write('Good afternoon', 0.1)
	elif 18 < int(e) < 24:
		gui.write('Good evening', 0.1)

if __name__ == '__main__':
	enter_vk()

	
