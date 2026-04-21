# Magic Eight Ball – Raspberry Pi Project

## Project Overview
A handheld **Magic Eight Ball** built using a **Raspberry Pi Zero W**, accelerometer, and OLED display.  
The device detects a shake motion and displays a random eight-ball response, all housed inside a custom **3D-printed shell** and powered by a rechargeable battery.

Detailed documentation can be found in [docs folder](./docs/).

---

## Key Features
- Shake detection using a 3-axis accelerometer
- OLED display for responses and splash screen
- Battery-powered via PiSugar S UPS
- Fully enclosed 3D-printed Magic Eight Ball shell
- Soft shutdown button and hard power cutoff switch
- External USB-C charging port

---

## Hardware Summary
- Raspberry Pi Zero W
- ADXL345 Accelerometer
- 0.96" I2C OLED Display
- PiSugar S 1200mAh Battery
- Momentary push button (soft shutdown)
- Rocker switch (hard power)
- Custom USB-C charging port

---

## Software Summary
- Python 3
- Motion-based triggering logic
- Randomized Magic Eight Ball responses
- Software I2C (bit-banging) for sensor to avoid GPIO conflicts
- Safe shutdown handling to prevent SD card corruption

---

## 3D Printing
- Printed on a **Bambu Lab P1S**
- Modified pre-existing Magic Eight Ball model (two halves)
- Custom internal layout for electronics
- Twist-lock mechanism secures both halves

---

## Power Notes
> ⚠️ Always use the soft shutdown button before turning off the hard power switch to avoid SD card corruption.

---

![Alt text](./img/IMG_0549.png)
![Alt text](./img/IMG_0550.png)