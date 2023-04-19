import time
import docker
from scripts.service.run import createServiceContainer, runCmdInContainer
from scripts.service.encrypt import encryptCredentials, readPublicKeyFromString
from scripts.contract.getters import getNoOfHours
from scripts.data import deployedChipnet, myAccount
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
    deployedChipnet.postCredentials(
        serviceIndex, encryptedAccessLink, encryptedPassword, {"from": myAccount}
    )


def newService(serviceIndex):
    def theTerminator():
        runCmdInContainer(["killall ngrok"], f"service-{serviceIndex}" + "-container")

    try:
        password = createServiceContainer(f"service-{serviceIndex}")
        accessLink = pollForAccessLink(f"service-{serviceIndex}" + "-container")
        postCredentials(serviceIndex, accessLink, password)
        timeSpan = int(getNoOfHours(serviceIndex)) * 60 * 60
        endServiceIn(timeSpan, theTerminator)
    except docker.errors.DockerException:
        print("Error: Docker is not running???")
