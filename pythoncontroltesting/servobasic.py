from gpiozero import PWMOutputDevice
import time

# Initialize the servo pin
servo_pin = PWMOutputDevice(21, frequency=50)

# Set servo position (0.0 = min, 1.0 = max)
for i in range(10):
    print(i)
    servo_pin.value = i/10
    
    # Keep the servo in place for 2 seconds
    time.sleep(0.1)




servo_pin.value = 0.5


# Clean up
servo_pin.close()
