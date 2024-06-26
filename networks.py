import os
import yaml
import shutil
import platform

home_folder = os.path.expanduser("~")

def getConfigFilePath():
    configFilePathMac = f"{home_folder}/.brownie/network-config.yaml"  # change these paths to more generic ones
    configFilePathWindows = "C:\\Users\\Administrator\\.brownie\\network-config.yaml"
    if platform.system() == "Windows":
        return configFilePathWindows
    else:
        return configFilePathMac


def getConfigFilePathModified():
    configFilePathMacModified = f"{home_folder}/.brownie/network-config-modified.yaml"
    configFilePathWindowsModified = (
        "C:\\Users\\Administrator\\.brownie\\network-config-modified.yaml"
    )
    if platform.system() == "Windows":
        return configFilePathWindowsModified
    else:
        return configFilePathMacModified


def getGlobalConfig():
    data = None
    with open(getConfigFilePath(), "r") as f:  # change this for windows too
        data = yaml.safe_load(f)
    return data


def networkExists(networkName):
    data = getGlobalConfig()
    for network in data["live"][0]["networks"]:
        if network["id"] == networkName:
            return True
    return False


def getNetwork(networkName):
    data = getGlobalConfig()
    for network in data["live"][0]["networks"]:
        if network["id"] == networkName:
            return network
    return None


def addNetwork(networkDict):
    data = getGlobalConfig()
    data["live"][0]["networks"].append(networkDict)
    # Write the modified data back to the YAML file
    with open(getConfigFilePathModified(), "w") as f:  # change this for windows
        yaml.dump(data, f)
    shutil.move(getConfigFilePathModified(), getConfigFilePath())


def addNetworkIfItDoesntExist(networkDict):
    if not networkExists(networkDict["id"]):
        addNetwork(networkDict)


def setupNetworks():
    localGanache = {
        "chainid": 1337,
        "host": "http://127.0.0.1:7545",
        "id": "localGanache",
        "name": "localGanache",
    }

    globalGanache = {
        "chainid": 1338,
        "host": "http://159.65.146.245",
        "id": "globalGanache",
        "name": "globalGanache",
    }
    addNetworkIfItDoesntExist(localGanache)
    addNetworkIfItDoesntExist(globalGanache)

def read_2nd_line(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        second_line = file.readline().strip()
    return second_line

def getMyDeployments():
    myDeployments = {}
    myDeployments["localGanache"] = "0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87"
    # myDeployments["globalGanache"] = "0x761A4B1E2d7D2c6a7d14F1445C44C4636c055651"
    myDeployments["globalGanache"] = read_2nd_line("./deployment.txt")
    myDeployments["sepolia"] = "0xa341dC25792C79430E6973Db8915f7751001A262"
    return myDeployments
