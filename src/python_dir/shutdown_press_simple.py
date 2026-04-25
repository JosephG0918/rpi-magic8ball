from gpiozero import Button
import os
import time
import sys

from PIL import ImageFont, ImageDraw
sys.path.append('/home/<user>/python_dir/m8ball_proj/lib_oled96')

from lib_oled96 import ssd1306
from smbus2 import SMBus

# OLED setup first
i2cbus_oled = SMBus(3)
oled = ssd1306(i2cbus_oled)
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 13)

# Wait for button press on GPIO 21
Button(21).wait_for_press()

# Kill m8ball.py process
os.system("/usr/bin/pkill -f m8ball.py")

# Draw shutdown message
draw = oled.canvas
draw.text((1, 1), 'Goodbye!', font=font, fill=1)
oled.display()
time.sleep(4)
oled.cls()

time.sleep(3)

# Shutdown
os.system("/usr/sbin/shutdown -h now")