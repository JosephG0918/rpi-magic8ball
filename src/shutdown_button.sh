#!/bin/bash

LOGFILE="/home/(user)/logs/shutdown_log.txt"
SCRIPT="/home/(user)/python_dir/shutdown_press_simple.py"

# Run once
sudo /usr/bin/python3 "$SCRIPT" > "$LOGFILE" 2>&1