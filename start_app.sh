#!/bin/bash
source venv/bin/activate;
export FLASK_APP=app.py;
flask run --host 127.0.0.1
