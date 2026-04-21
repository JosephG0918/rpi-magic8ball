#!/bin/bash

SCRIPT="/home/(user)/python_dir/m8ball_proj/m8ball.py"
VENV="/home/(user)/.local/share/virtualenvs/(venv)/bin/python"
LOGFILE="/home/(user)/logs/m8ball_log.txt"

# Run once
sudo "$VENV" "$SCRIPT" > "$LOGFILE" 2>&1