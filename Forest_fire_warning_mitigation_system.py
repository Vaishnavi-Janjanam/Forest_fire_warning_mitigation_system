import RPi.GPIO as GPIO
import time

# Define the flame sensor pins
flame_sensor_pins = [17, 27, 22, 23, 24]

# Define the relay control pin
relay_pin = 12

# Setup GPIO mode and warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup flame sensor pins as input
for pin in flame_sensor_pins:
    GPIO.setup(pin, GPIO.IN)

# Setup the relay pin as output
GPIO.setup(relay_pin, GPIO.OUT)

# Initialize relay to OFF state
GPIO.output(relay_pin, GPIO.LOW)

try:
    while True:
        flame_detected = False  # Flag to check if flame is detected

        for i, pin in enumerate(flame_sensor_pins):
            if GPIO.input(pin) == GPIO.HIGH:  # Flame detected (assuming active-high sensors)
                print(f"Flame detected on sensor {i + 1}")
                flame_detected = True
            else:
                print(f"No Flame detected on sensor {i + 1}")

        # Activate or deactivate the relay
        if flame_detected:
            GPIO.output(relay_pin, GPIO.HIGH)
            print("Relay activated: Pumping water!")
        else:
            GPIO.output(relay_pin, GPIO.LOW)
            print("Relay deactivated")

        time.sleep(1)

except KeyboardInterrupt:
    print("❌ Program terminated manually")

finally:
    GPIO.cleanup()
