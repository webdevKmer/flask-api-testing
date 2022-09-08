#!/usr/bin/python3

from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Flask"

app.run(host="0.0.0.0", port=8080)