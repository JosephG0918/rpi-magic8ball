import time
import board
import busio
import adafruit_adxl34x
import math


# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

# Enable motion detection with a threshold of 18 (units: approx. 62.5 mg per LSB)
# Now changed to 34
accelerometer.enable_motion_detection(threshold=34)

# Main loop
while True:
    if accelerometer.events["motion"]:
        print("Motion detected.")
