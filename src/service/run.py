from . import Container
import docker
import random
import string

repoLink = "https://github.com/s-madhu-v/Dockerf.git"


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


def runCmdInContainer(cmd, containerName):
    myClient = docker.from_env()
    container = myClient.containers.get(containerName)
    container.exec_run(cmd)


def createServiceContainer(imageName, cores, memory):
    args = getBuildArgs()
    myClient = docker.from_env()
    # the image name should always be lowercase
    obj = Container.dContainer(myClient, repoLink, imageName)
    # TODO: enforce limits
    obj.createContainer(cores=int(cores), memory=memory, storage="4G", buildArgs=args)
    return args["PASSWORD"]
