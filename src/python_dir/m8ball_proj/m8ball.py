import adafruit_adxl34x
import adafruit_bitbangio as bitbangio
import board
import time
import math
import random
from PIL import ImageFont
import sys

# Magic Eight Ball outputs
answers = [
    "It is certain.", "As I see it, yes.", "Reply hazy, try\nagain.", "Don't count on it.",
    "My sources say\nno.", "Outlook not\nso good.", "My reply\nis no.", "It is\ndecidedly so.",
    "Without a doubt.", "Yes definitely.", "Signs point to\nyes.", "Very doubtful.", "Not likely.",
    "No.", "Most likely.", "Outlook good.", "Yes.", "All signs\npoint to yes.", "Reply not clear.",
    "Better not tell\nyou now.", "I can smell you."
]

""" Accessing lib_oled96 library  """
sys.path.append('/home/(user)/python_dir/m8ball_proj/lib_oled96')
from lib_oled96 import ssd1306
from smbus2 import SMBus

""" Oled setup """
i2cbus_oled = SMBus(3)
oled = ssd1306(i2cbus_oled)
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 13)

""" Accelerometer sensor setup """
i2cbus_acc = bitbangio.I2C(scl=board.D27, sda=board.D17)
accelerometer = adafruit_adxl34x.ADXL345(i2cbus_acc)

THRESHOLD_G = 2                     # Minimum acceleration spike to count as a shake (g)
THRESHOLD_MS2 = THRESHOLD_G * 9.81  # m/s squared

print(f"Monitoring acceleration above {THRESHOLD_G}g...")

# Splash screen
draw = oled.canvas
draw.text((1, 1), 'Magic Eight Ball', font=font, fill=1)
oled.display()
time.sleep(5)
oled.cls()

""" Start of the program. Main.  """
try:
    while True:
        x, y, z = accelerometer.acceleration
        total_acc = (x**2 + y**2 + z**2)**0.5

        if total_acc > THRESHOLD_MS2:
            print(f"*** Peak detected! {total_acc/9.81:.2f} g ***")
            time.sleep(2)
            response = random.choice(answers)
            draw = oled.canvas  # <- Get a fresh canvas each time
            draw.text((1, 15), response, font=font, fill=1)
            oled.display()
            time.sleep(5)
            oled.cls()

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Interrupted by user.")
finally:
    oled.cls()
    print("Cleaned up.")