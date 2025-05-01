import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO
from gpiozero import Servo
import time

class RobotControlNode(Node):
    def __init__(self):
        super().__init__('robot_control')

        # Motor Pins
        D0 = 17  # Left motor A
        D1 = 27  # Left motor B
        D2 = 22  # Right motor A
        D3 = 23  # Right motor B
        self.pos_pin = 24
        self.cont_pin = 25

        # Setup GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(D0, GPIO.OUT)
        GPIO.setup(D1, GPIO.OUT)
        GPIO.setup(D2, GPIO.OUT)
        GPIO.setup(D3, GPIO.OUT)

        # Initialize PWM
        self.pwm_left_a = GPIO.PWM(D0, 100)
        self.pwm_left_b = GPIO.PWM(D1, 100)
        self.pwm_right_a = GPIO.PWM(D2, 100)
        self.pwm_right_b = GPIO.PWM(D3, 100)

        self.pwm_left_a.start(0)
        self.pwm_left_b.start(0)
        self.pwm_right_a.start(0)
        self.pwm_right_b.start(0)

        # Initialize servos
        self.p_servo = Servo(self.pos_pin)
        self.c_servo = Servo(self.cont_pin)

        # Internal state
        self.orient = 90.0
        self.shoot = False

        # ROS 2 subscriptions
        self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)
        self.create_subscription(Float32, '/orient', self.orient_callback, 10)
        self.create_subscription(Bool, '/shoot', self.shoot_callback, 10)

        # Initial setup
        self.p_servo.value = 0
        self.c_servo.value = 1
        self.control_motors(0, 0, True, True)

        self.get_logger().info("Robot control node initialized")
        
        
      
    def control_motors(self, speed_L, speed_R, dir_L, dir_R):
        # Motor control logic
        if dir_L:
            self.pwm_left_a.ChangeDutyCycle(speed_L)
            self.pwm_left_b.ChangeDutyCycle(0)
        else:
            self.pwm_left_a.ChangeDutyCycle(0)
            self.pwm_left_b.ChangeDutyCycle(speed_L)

        if dir_R:
            self.pwm_right_a.ChangeDutyCycle(speed_R)
            self.pwm_right_b.ChangeDutyCycle(0)
        else:
            self.pwm_right_a.ChangeDutyCycle(0)
            self.pwm_right_b.ChangeDutyCycle(speed_R)

    def cmd_vel_callback(self, msg):
        linear = msg.linear.x
        angular = msg.angular.z

        speed_L = 0
        speed_R = 0
        dir_L = True
        dir_R = True

        base_speed = min(abs(linear) * 100, 100)
        turn_factor = min(abs(angular) * 50, 100)

        if linear > 0:
            dir_L = True
            dir_R = True
            speed_L = base_speed
            speed_R = base_speed
        elif linear < 0:
            dir_L = False
            dir_R = False
            speed_L = base_speed
            speed_R = base_speed

        if angular > 0:
            speed_L = max(speed_L - turn_factor, 0)
            speed_R = min(speed_R + turn_factor, 100)
        elif angular < 0:
            speed_L = min(speed_L + turn_factor, 100)
            speed_R = max(speed_R - turn_factor, 0)

        if linear == 0 and angular != 0:
            dir_L = angular < 0
            dir_R = angular > 0
            speed_L = speed_R = turn_factor

        if linear == 0 and angular == 0:
            speed_L = 0
            speed_R = 0

        self.control_motors(speed_L, speed_R, dir_L, dir_R)

    def orient_callback(self, msg):
        self.orient = msg.data
        self.p_servo.value = (self.orient - 90) / 90

    def shoot_callback(self, msg):
        self.shoot = msg.data
        if self.shoot:
            self.c_servo.value = -1
            time.sleep(1)
            self.c_servo.value = 1

def main(args=None):
    rclpy.init(args=args)
    node = RobotControlNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

