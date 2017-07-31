import os

import requests
from flask import Flask, render_template


app = Flask(__name__, template_folder='.', instance_relative_config=True)
app.config.from_pyfile('config.py')


@app.route('/')
def index():
    params = {
        "api_key": os.environ.get("GIPHY_API_KEY") if os.environ.get("GIPHY_API_KEY") else app.config["GIPHY_API_KEY"],
        "tag": "sharks",
        "rating": "g",
        "fmt": "json"
    }
    r = requests.get("https://api.giphy.com/v1/gifs/random", params=params)
    return render_template('index.html', image_url=r.json()['data']['image_url'])


if __name__ == "__main__":
    app.run(host="0.0.0.0")
