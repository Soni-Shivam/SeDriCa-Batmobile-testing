from gpiozero import Servo
from time import sleep

servo = Servo(20)

servo.detach()

while True:
    shoot = int(input("Enter 1 or 0"))
    if shoot == 1:
        servo.max()
        sleep(0.085)
        servo.detach()
