from . import Container
import docker

buildargs = {
    "PASSWORD": "l",
}


def run():
    myClient = docker.from_env()
    repoLink = "https://github.com/s-madhu-v/Dockerf.git"
    # the image name should always be lowercase
    obj = Container.dContainer(myClient, repoLink, "maze")
    obj.createContainer(cores=1, memory="2g", storage="4G", buildArgs=buildargs)


def fakeRun():
    print("\n\nThis is a fake run function!!!\n\n")


def main():
    run()
