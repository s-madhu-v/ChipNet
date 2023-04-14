from . import Container
import docker

buildargs = {
    "PASSWORD": "l",
    "NGROK_AUTH_KEY": "2JVJ2QX6ten3b2UofO5a1RFZqL1_7NU96eFBqcWLP2KogBWAk"
}


def run(imageName):
    myClient = docker.from_env()
    repoLink = "https://github.com/s-madhu-v/Dockerf.git"
    # the image name should always be lowercase
    obj = Container.dContainer(myClient, repoLink, imageName)
    obj.createContainer(cores=1, memory="2g", storage="4G", buildArgs=buildargs)


def fakeRun():
    print("\n\nThis is a fake run function!!!\n\n")


def main():
    run()
