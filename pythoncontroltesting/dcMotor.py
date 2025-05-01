from gpiozero import Motor
from time import sleep
motor = Motor(12, 13)
while True:
    motor.forward()
    print("moving forward")
    
    sleep(5)
    motor.backward()
    print("moving back")
    sleep(5)
