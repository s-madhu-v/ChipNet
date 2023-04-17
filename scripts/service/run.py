from . import Container
import docker
import random
import string


def generateRandomPassword(length):
    characters = string.ascii_letters + string.digits  # + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password


def getBuildArgs():
    buildargs = {
        "PASSWORD": generateRandomPassword(15),
        "NGROK_AUTH_KEY": "2JVJ2QX6ten3b2UofO5a1RFZqL1_7NU96eFBqcWLP2KogBWAk",
    }
    return buildargs


def run(imageName):
    myClient = docker.from_env()
    repoLink = "https://github.com/s-madhu-v/Dockerf.git"
    # the image name should always be lowercase
    obj = Container.dContainer(myClient, repoLink, imageName)
    obj.createContainer(cores=1, memory="2g", storage="4G", buildArgs=getBuildArgs())


def main():
    run()
