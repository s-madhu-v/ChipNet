import time
from scripts.service.run import run
import subprocess


def pollForAccessLink(args):
    link = ""
    while True:
        try:
            link = getAccessLink(args.containerName)
            print(f"Access Link: {link}")
            break
        except subprocess.CalledProcessError:
            print("Access Link not found yet")
            time.sleep(1)
    return link


def getAccessLink(containerName):
    containerPath = containerName + ":/access-link.txt"
    localPath = "."
    dockerCommand = ["docker", "cp", containerPath, localPath]
    subprocess.run(dockerCommand, check=True)
    link = ""
    with open("access-link.txt", "r") as f:
        for line in f:
            link = line
    return link


def endServiceIn(seconds, terminator):
    start_time = time.monotonic()  # get current time in seconds
    end_time = start_time + seconds  # calculate end time
    while time.monotonic() < end_time:  # loop until end time is reached
        time.sleep(1)  # wait for 5 second before next iteration
    terminator()


def runService(args):
    run()
    pollForAccessLink(args)
    sendAccessLink()
    endServiceIn()
