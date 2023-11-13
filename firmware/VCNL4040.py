import qwiic_proximity
from gpiozero import LED
from time import sleep

PROXIMITY_THRESHOLD = 2000  # Adjust this threshold based on your requirements

# Initialize the Qwiic Proximity sensor
proximity_sensor = qwiic_proximity.QwiicProximity()

if not proximity_sensor.begin():
    print("The Qwiic Proximity sensor isn't connected to the system. Please check your connection", file=sys.stderr)
else:
    print("Proximity sensor initialized.")

# Set up the LED
led = LED(17)  # Assuming the LED is connected to GPIO 17

try:
    while True:
        # Read proximity value
        proximity = proximity_sensor.get_proximity()
        print("Proximity:", proximity)

        # Control the LED based on proximity
        if proximity > PROXIMITY_THRESHOLD:
            led.on()
        else:
            led.off()

        sleep(1)  # Small delay to prevent excessive CPU usage

except KeyboardInterrupt:
    led.off()
    print("Program stopped")
