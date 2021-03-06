# Docker Commander
A simple docker dashboard, where you can start or stop the containers remotely

## Preview
![preview image](https://raw.githubusercontent.com/dofun12/docker-commander/master/preview-images/preview.JPG)

## Requirements

 - Docker
 - Git
 - Python 3.7
 - Pipenv

After having all the requirements, you must start the docker service.

Clone the project:

    git clone https://github.com/dofun12/docker-commander

Go to the directory

    cd docker-commander

Then install the dependencies:

    pipenv install

Running:

    pipenv run python main.py
Now open your browser at:
    http://localhost:5050/gui

You can also configure the server port at **config.ini**

# Service
Running as service on debian or ubuntu:

    ./create-service.sh

