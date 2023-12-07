import time
import json
import docker
from src.service.encrypt import encryptString, readPublicKeyFromString
from src.app import getTheApp
import subprocess
from src.service.command_generators import execute_docker_template
import threading


def pollForComments(containerName):
    comments = ""
    while True:
        try:
            comments = getComments(containerName)
            print(f"Comments: {comments}")
            break
        except subprocess.CalledProcessError:
            print("Comments File not found yet")
            time.sleep(1)
    return comments


def getComments(containerName):
    containerPath = containerName + ":/chipnet_comments.txt"
    localPath = "."
    dockerCommand = ["docker", "cp", containerPath, localPath]
    subprocess.run(dockerCommand, check=True)
    comments = ""
    with open("chipnet_comments.txt", "r") as f:
        for line in f:
            comments += (line + "\n")
    return comments


def endServiceIn(seconds, terminator):
    start_time = time.monotonic()  # get current time in seconds
    end_time = start_time + seconds  # calculate end time
    while time.monotonic() < end_time:  # loop until end time is reached
        time.sleep(1)  # wait for 1 second before next iteration
    terminator()


def postCredentials(serviceIndex, accessLink, password):
    deployedChipnet = getTheApp().deployedChipnet
    myAccount = getTheApp().myAccount
    service = deployedChipnet.getService(serviceIndex)
    bid = deployedChipnet.getBid(service["bidIndex"])
    publicKey = readPublicKeyFromString(bid["publicKey"])
    encryptedAccessLink = encryptString(accessLink, publicKey)
    encryptedPassword = encryptString(password, publicKey)
    deployedChipnet.postCredentials(
        serviceIndex, encryptedAccessLink, encryptedPassword, {"from": myAccount}
    )

def postComments(serviceIndex, comments):
    deployedChipnet = getTheApp().deployedChipnet
    myAccount = getTheApp().myAccount
    service = deployedChipnet.getService(serviceIndex)
    bid = deployedChipnet.getBid(service["bidIndex"])
    publicKey = readPublicKeyFromString(bid["publicKey"])
    encryptedComments = encryptString(comments, publicKey)
    deployedChipnet.postComments(
        serviceIndex, encryptedComments, {"from": myAccount}
    )

def setupServiceFromTemplate(serviceIndex, bidIndex):
    try:
        bid = getTheApp().contractData.allBids[bidIndex]
        template = bid.encryptedTemplate
        # Create a new thread and start it
        thread = threading.Thread(target=lambda: execute_docker_template(template))
        thread.start()
        print("posting credentials")
        template = json.loads(template)
        postComments(serviceIndex, pollForComments(template["name"]))
    except docker.errors.DockerException:
        print("Error: Docker is not running???")