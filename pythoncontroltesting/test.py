from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero import AngularServo
from time import sleep

factory = LGPIOFactory()
servo = AngularServo(21, min_angle=-1, max_angle=1, pin_factory=factory)

for speed in [1, 0.15, -1, 0.15,1, 0.15, -1, 0.15,1, 0.15, -1, 0.15,1, 0.15, -1, 0.15,1, 0.15, -1, 0.15,1, 0.15, -1, 0.15]:
    servo.angle = speed
    print("Speed:", speed)
    sleep(1)
