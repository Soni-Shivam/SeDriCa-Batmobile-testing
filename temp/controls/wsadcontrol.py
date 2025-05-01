import keyboard

while True:
    if keyboard.is_pressed('w'):
        print('Up')
    elif keyboard.is_pressed('s'):
        print('Down')
    elif keyboard.is_pressed('a'):
        print('Left')
    elif keyboard.is_pressed('d'):
        print('Right')
    elif keyboard.is_pressed('q'):
        break
