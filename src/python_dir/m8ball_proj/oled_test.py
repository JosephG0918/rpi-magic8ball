import os
import psutil
from time import sleep
from datetime import datetime
from PIL import ImageFont, ImageDraw, Image
# font = ImageFont.load_default()

import sys
sys.path.append('/home/<user>/python_dir/m8ball_proj/lib_oled96')

from lib_oled96 import ssd1306

from smbus2 import SMBus
i2cbus = SMBus(3)
oled = ssd1306(i2cbus)

import socket

draw = oled.canvas
# set font to 13 for yellow area
font = ImageFont.truetype('FreeSans.ttf', 13)

# show splash screen
draw.text((1, 1), 'RASPBIAN SYSMON', font=font, fill=1)

oled.display()
sleep(3)
oled.cls()

while True:
    draw = oled.canvas
    font = ImageFont.truetype('FreeSans.ttf', 13)

    # get, display date and time
    draw.text((1, 1), str(datetime.now().strftime('%a  %b  %d  %H:%M:%S')), font=font, fill=1)

    # get, return CPU's current temperature
    def cpu_temp():
        tempF = (((int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1000)*9/5)+32)
        return "CPU TEMP: %sF" % str(round(tempF, 2))

    # display CPU temp
    draw.text((1, 15),    cpu_temp(),  font=font, fill=1)

    def wlan_ip():
        try:
            # This creates a dummy socket to connect to an external server
            # and gets the IP of the interface used for the connection.
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return f"IP: {ip}"
        except:
            return "No IP Found"

    # Display the IP address
    draw.text((1, 28), wlan_ip(), font=font, fill=1)

    # get disk usage
    def disk_usage(dir):
       usage = psutil.disk_usage(dir)
       return "SD CARD USE: %.0f%%" % (usage.percent)

    # display disk usage
    draw.text((1, 41), disk_usage('/'),  font=font, fill=1)

    oled.display()
    sleep(10)
    oled.cls()