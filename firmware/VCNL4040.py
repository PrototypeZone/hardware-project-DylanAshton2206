import qwiic_proximity
from sense_hat import SenseHat
from time import sleep

# Initialize Sense HAT and Proximity sensor
sense = SenseHat()
proximity_sensor = qwiic_proximity.QwiicProximity()

#had to add a layer of cusion +6000 to avoid crash
MAX_PROXIMITY = 26000  # Maximum expected proximity value


if not proximity_sensor.begin():
    print("The Qwiic Proximity sensor isn't connected to the system. Please check your connection", file=sys.stderr)
else:
    print("Proximity sensor initialized.")

def get_exponential_color(proximity):
    # Apply an exponential transformation to the proximity value
    # The exponent value determines the rate of change in color
    exponent = 0.15  # You can adjust this exponent to change the rate of color change
    ratio = (proximity / MAX_PROXIMITY) ** exponent

    red = int(ratio * 255)
    green = 255 - red
    blue = 0  # Keeping blue at 0
    return (red, green, blue)

try:
    while True:
        proximity = proximity_sensor.get_proximity()
        print("Proximity:", proximity)
         # Read ambient light value
        ambient_light = proximity_sensor.get_ambient()
        print("Ambient Light:", ambient_light)

        # Get the color based on the exponentially transformed proximity value
        color = get_exponential_color(proximity)
        sense.clear(color)

        sleep(0.1)  # Small delay to prevent excessive CPU usage

except KeyboardInterrupt:
    sense.clear()  # Clear the LED matrix
    print("Program stopped")

