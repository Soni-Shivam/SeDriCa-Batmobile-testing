import rospy
from std_msgs.msg import Float32, Bool
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO
import time
from gpiozero import Servo

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motor Pins (BCM pin numbers)
D0 = 17  # Left motor A (PWM)
D1 = 27  # Left motor B (PWM)
D2 = 22  # Right motor A (PWM)
D3 = 23  # Right motor B (PWM)
pos_pin = 24  # Position servo pin
cont_pin = 25  # Continuous servo pin

# Initialize servo objects
p_servo = Servo(pos_pin)
c_servo = Servo(cont_pin)

# Global Variables
orient = 90.0
shoot = False

# Setup Motor Pins as OUTPUT
GPIO.setup(D0, GPIO.OUT)
GPIO.setup(D1, GPIO.OUT)
GPIO.setup(D2, GPIO.OUT)
GPIO.setup(D3, GPIO.OUT)

# Setup PWM for motor control (duty cycle)
pwm_left_a = GPIO.PWM(D0, 100)  # 100Hz frequency
pwm_left_b = GPIO.PWM(D1, 100)
pwm_right_a = GPIO.PWM(D2, 100)
pwm_right_b = GPIO.PWM(D3, 100)

pwm_left_a.start(0)
pwm_left_b.start(0)
pwm_right_a.start(0)
pwm_right_b.start(0)

# Motor control function
def controlMotors(speed_L, speed_R, dir_L, dir_R):
    if dir_L:
        pwm_left_a.ChangeDutyCycle(speed_L)
        pwm_left_b.ChangeDutyCycle(0)
    else:
        pwm_left_a.ChangeDutyCycle(0)
        pwm_left_b.ChangeDutyCycle(speed_L)

    if dir_R:
        pwm_right_a.ChangeDutyCycle(speed_R)
        pwm_right_b.ChangeDutyCycle(0)
    else:
        pwm_right_a.ChangeDutyCycle(0)
        pwm_right_b.ChangeDutyCycle(speed_R)

# Callback function for velocity command
def cmdVelCallback(msg):
    global orient, shoot

    linear = msg.linear.x  # Forward (+) or Backward (-)
    angular = msg.angular.z  # Left (+) or Right (-)

    speed_L = 0
    speed_R = 0
    dir_L = True
    dir_R = True

    base_speed = min(abs(linear) * 255, 255)
    turn_factor = min(abs(angular) * 150, 255)

    if linear > 0:  # Moving Forward
        dir_L = True
        dir_R = True
        speed_L = base_speed
        speed_R = base_speed
    elif linear < 0:  # Moving Backward
        dir_L = False
        dir_R = False
        speed_L = base_speed
        speed_R = base_speed

    if angular > 0:  # Turning Left
        speed_L = max(speed_L - turn_factor, 0)
        speed_R = min(speed_R + turn_factor, 255)
    elif angular < 0:  # Turning Right
        speed_L = min(speed_L + turn_factor, 255)
        speed_R = max(speed_R - turn_factor, 0)

    if linear == 0 and angular != 0:  # In-place rotation
        dir_L = angular < 0  # Right spin -> Left motors backward
        dir_R = angular > 0  # Left spin -> Right motors backward
        speed_L = speed_R = turn_factor

    if linear == 0 and angular == 0:  # Stop
        speed_L = 0
        speed_R = 0

    controlMotors(speed_L, speed_R, dir_L, dir_R)

# Callback functions for orientation and shooting
def orient_callback(gear):
    global orient
    orient = gear.data
    # Update the positional servo angle (0-180 degrees)
    p_servo.value = (orient - 90) / 90  # Convert to servo range (-1 to 1)

def shoot_callback(key):
    global shoot
    shoot = key.data
    if shoot:
        # Activate the continuous servo for shooting
        c_servo.value = -1  # Move servo to shoot position
        time.sleep(1)  # Adjust the time based on the shooting mechanism
        c_servo.value = 1  # Reset servo position

# ROS Node Setup
def setup():
    rospy.init_node('robot_control', anonymous=True)
    rospy.Subscriber('/cmd_vel', Twist, cmdVelCallback)
    rospy.Subscriber('/orient', Float32, orient_callback)
    rospy.Subscriber('/shoot', Bool, shoot_callback)

    # Set initial servo positions and motor states
    p_servo.value = 0  # Initial position for positional servo (neutral position)
    c_servo.value = 1  # Initial position for continuous servo (neutral)
    controlMotors(0, 0, True, True)  # Stop motors initially

if __name__ == '__main__':
    setup()
    rospy.spin()
