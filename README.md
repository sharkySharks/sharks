# Getting Started
- [Sharks Repo](#random-shark-gifs)
- [RSI Onboarding](#rsi-onboarding)

***

## Random Shark Gifs
To get started you will need to make a free account with giphy in order to get an API key. More on that [here](https://developers.giphy.com/docs/).

Add your API key to your shell environment variables or to a `.env` file: 
`export GIPHY_API_KEY = your-api-key-from-giphy`

Start up a virtual environment and install dependencies:
```
python3 -m venv ENV
source ENV/bin/activate
pip3 install -r requirements.txt
```

Run the app with the following command:
`python3 app.py`

Go to localhost:5000 to see the app running in your local browser.

### Run with Docker
Install [Docker](https://docs.docker.com/engine/installation/).

Create an image from the Dockerfile and run the following commands to build the image:
```
docker build -t sharks:v1.0 .                          tag the image at version 1.0
docker images                                          list all your local images
docker run -d -p 5000:5000 sharks:v1.0 <image id>      run the app on port 5000
docker ps                                              check container is running app
```

Go to localhost:5000 to see the app running in your local browser.
