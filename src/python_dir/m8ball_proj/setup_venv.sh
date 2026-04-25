#!/usr/bin/env bash

set -e

echo "Creating Pipenv environment..."

# Initialize pipenv (uses current Python)
pipenv --python 3

echo "Installing dependencies..."

pipenv install \
    pillow \
    adafruit-gpio \
    adafruit-ssd1306 \
    psutil \
    spidey \
    adafruit-circuitpython-adxl34x \
    smbus2 \
    adafruit-circuitpython-bitbangio \
    adafruit-blinka

echo "Generating lockfile..."

pipenv lock --clear

echo "Done!"
echo "To enter the environment, run: pipenv shell"