#!/bin/bash
ngrok http 5000 &
python3 ./webhook_handler.py
