from pynput import mouse, keyboard

def on_press(key):
    try:
        print(f"Клавиша: {key.char}")
    except AttributeError:
        print(f"Специальная клавиша: {key}")
        

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
    on_press = on_press,
    on_release = on_release) as listenter:
    listenter.join()

listenter = keyboard.Listener(
    on_press = on_press,
    on_release = on_release)
listenter.start()




