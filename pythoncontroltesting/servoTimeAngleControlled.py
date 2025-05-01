from gpiozero import PWMOutputDevice
import time

# Change GPIO pin number as per your connection
servo_pin = PWMOutputDevice(21, frequency=50)

def run_motor_for(duration):
    print(f"Running motor for {duration} seconds...")
    servo_pin.value = 0.5
    time.sleep(duration)
    servo_pin.value = 0.18
    print("Motor stopped.")

def main():
    servo_pin.value = 0.18
    while True:
        try:
            user_input = input("Enter angle to run motor (in degrees), or 'q' to quit: ")
            if user_input.lower() == 'q':
                print("Exiting.")
                break
            duration = float(user_input)
            if duration > 0:
                run_motor_for(duration)
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

