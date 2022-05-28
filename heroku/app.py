import os
import json
from os import environ
from flask import Flask, request


app = Flask(__name__)



@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        return "Hello, It Works"
    


if __name__ == "__main__":
    app.run(debug=True)