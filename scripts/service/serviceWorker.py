import time
import base64
from scripts.service.run import run
from scripts.service.encrypt import encryptMsg
from Crypto.PublicKey import RSA
from scripts.data import deployedChipnet, sellAccount, buyAccount
import subprocess
import random
import string

def generateRandomPassword(length):
    # Define the character set to use for the password
    characters = string.ascii_letters + string.digits # + string.punctuation
    # Generate a password of the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    return password


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
    publicKey = RSA.import_key(bid["publicKey"].encode('utf-8'))
    encryptedAccessLink = encryptMsg(accessLink.encode('utf-8'), publicKey)
    encodedAccessLink = base64.b64encode(encryptedAccessLink).decode('utf-8')
    encryptedPassword = encryptMsg(password.encode('utf-8'), publicKey)
    encodedPassword = base64.b64encode(encryptedPassword).decode('utf-8')
    # change the sellAccount to sellerAccount
    deployedChipnet.postCredentials(serviceIndex, encodedAccessLink, encodedPassword, {"from": sellAccount})

def runService(serviceIndex):
    run(f"service-{serviceIndex}")
    accessLink = pollForAccessLink(f"service-{serviceIndex}" + "-container")
    postCredentials(serviceIndex, accessLink, generateRandomPassword(10))
    endServiceIn(60*60, theTerminator) # change this to time in the bid