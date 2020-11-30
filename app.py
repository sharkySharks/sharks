import os

import requests
from flask import Flask, render_template

app = Flask(__name__, template_folder='.')


@app.route('/', methods=["GET", "POST"])
def index():
    params = {
        "api_key": os.environ.get("GIPHY_API_KEY"),
        "tag": "shark",
        "rating": "g",
        "fmt": "json"
    }
    r = requests.get("https://api.giphy.com/v1/gifs/random", params=params)
    return render_template('index.html', image_url=r.json()['data']['image_url'])

if __name__ == "__main__":
    app.run(host="0.0.0.0")
