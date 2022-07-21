import keyboard

rk = keyboard.record(until = 'Esc')

keyboard.play(rk, speed_factor = 1)
print(rk)
