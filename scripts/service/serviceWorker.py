import time
import base64
import docker
from scripts.service.run import run
from scripts.service.encrypt import encryptCredentials, readPublicKeyFromString
from scripts.data import deployedChipnet, sellAccount, buyAccount
import subprocess


def pollForAccessLink(containerName):
    link = ""
    while True:
        try:
            link = getAccessLink(containerName)
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


def theTerminator():
    print("Terminating the service")


def endServiceIn(seconds, terminator):
    start_time = time.monotonic()  # get current time in seconds
    end_time = start_time + seconds  # calculate end time
    while time.monotonic() < end_time:  # loop until end time is reached
        time.sleep(1)  # wait for 1 second before next iteration
    terminator()


def postCredentials(serviceIndex, accessLink, password):
    service = deployedChipnet.getService(serviceIndex)
    bid = deployedChipnet.getBid(service["bidIndex"])
    publicKey = readPublicKeyFromString(bid["publicKey"])
    encryptedAccessLink = encryptCredentials(accessLink, publicKey)
    encryptedPassword = encryptCredentials(password, publicKey)
    # change the sellAccount to sellerAccount
    deployedChipnet.postCredentials(
        serviceIndex, encryptedAccessLink, encryptedPassword, {"from": sellAccount}
    )


def runService(serviceIndex):
    try:
        run(f"service-{serviceIndex}")
        accessLink = pollForAccessLink(f"service-{serviceIndex}" + "-container")
        postCredentials(serviceIndex, accessLink, generateRandomPassword(10))
        endServiceIn(60 * 60, theTerminator)  # change this to time in the bid
    except docker.errors.DockerException:
        print("Error: Docker is not running?")
