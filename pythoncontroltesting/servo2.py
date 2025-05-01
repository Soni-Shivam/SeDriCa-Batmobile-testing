from gpiozero import AngularServo
from time import sleep
import threading

servo = AngularServo(21, min_angle=-90, max_angle=90)
exit_flag = False

def check_for_exit():
    global exit_flag
    while True:
        user_input = input("Press 'q' then Enter to quit:\n")
        if user_input.lower() == 'q':
            exit_flag = True
            break

threading.Thread(target=check_for_exit, daemon=True).start()

try:
    while not exit_flag:
        for angle in [-90, -45, 0, 45, 90,45,0,-45]:
            if exit_flag:
                break
            servo.angle = angle
            print(f"Moved servo to angle: {angle}°")
            sleep(2)
except KeyboardInterrupt:
    print("\nKeyboardInterrupt received. Exiting safely...")
finally:
    servo.angle = 0
    print("Moved servo to neutral (0°)")
    sleep(1)
    servo.detach()
    print("Servo detached. Program terminated safely.")
