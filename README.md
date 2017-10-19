# Getting Started
- [Sharks Repo](#random-shark-gifs)
- [RSI Onboarding](#rsi-onboarding)

***

## Random Shark Gifs
To get started you will need to make a free account with giphy in order to get an API key. More on that [here](https://developers.giphy.com/docs/).

Add your API key to your shell environment variables: 
`export GIPHY_API_KEY = your-api-key-from-giphy`

Start up a virtual environment and install dependencies:
```
virtualenv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

Run the app with the following command:
`python app.py`

Go to localhost:5000 to see the app running in your local browser.

##### Run with Docker
Install [Docker](https://docs.docker.com/engine/installation/).

Create an image from the Dockerfile and run the following commands to build the image:
```
docker build -t sharks:v1.0                            tag the image at version 1.0
docker images                                          list all your local images
docker run -d -p 5000:5000 sharks:v1.0 <image id>      run the app on port 5000
docker ps                                              check container is running app
```

Go to localhost:5000 to see the app running in your local browser.

***

## RSI Onboarding
Rackspace Service Infrastructure (RSI) is a common internal platform for automating deployment, scaling, and management of containerized applications. The system is built using [OpenShift](https://docs.openshift.org/latest/welcome/index.html), [Kubernetes](https://kubernetes.io/docs/home/), and [Docker](https://docs.docker.com/).

### Getting Started
If you are not familiar with [Docker](https://docs.docker.com/), start learning how Docker works. There are tutorial resources below. Create your own simple app or fork this repo to deploy to RSI. Get the app running in a Docker container, put your app in the internal Github, and then go to RSI to setup your RSI app.

**NOTE:** SSH is not enabled for authenticating your app between GitHub and RSI, so use a [personal access token](https://github.com/blog/1509-personal-api-tokens) instead.

Once you have your app running in RSI, you can play around with different configurations, either changing them via the [web console](https://docs.openshift.org/latest/getting_started/developers_console.html#getting-started-developers-console), the [oc cli tool](https://docs.openshift.org/latest/getting_started/developers_cli.html), or the [API](https://docs.openshift.org/latest/rest_api/index.html).

Understanding how [Kubernetes](https://github.com/kubernetes) works is fundamental to understanding OpenShift, so read the docs or go through the Kubernetes tutorial in the resource list below. Once you have a basic understanding of Kubernetes, you can dive into [OpenShift](https://docs.openshift.org/latest/getting_started/index.html) to specifically see how RSI is working. There is a pdf version of a book for devs learning OpenShift listed in the resource list below.

The RSI team is using [Helm charts](https://docs.helm.sh/developing_charts/) to manage different build packages. From a QE perspective, we are looking to create Helm charts for automating different types of test builds and CICD pipelines. So become familiar with how Helm charts are built and organized.

This will be enough to get you started and exploring RSI.

### Resources
- [Docker Tutorials](https://www.youtube.com/playlist?list=PLkA60AVN3hh_6cAz8TUGtkYbJSL2bdZ4h)
- [Kubernetes Tutorials](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [Helm Docs](https://docs.helm.sh/using_helm/#quickstart-guide)
- [OpenShift](https://docs.openshift.org/latest/getting_started/index.html)
- Books: _DevOps With OpenShift_ & _OpenShift for Developers_
