#!/bin/bash
ngrok http 5000 > /dev/null &
python3 ./webhook_handler.py
