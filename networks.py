import yaml
import shutil


def getConfigFilePath():
    configFilePathMac = "/Users/imadhui/.brownie/network-config.yaml"
    return configFilePathMac


def getConfigFilePathModified():
    configFilePathMacModified = "/Users/imadhui/.brownie/network-config-modified.yaml"
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
        "chainid": 9999,
        "host": "http://64.227.142.218",
        "id": "globalGanache",
        "name": "globalGanache",
    }
    addNetworkIfItDoesntExist(localGanache)
    addNetworkIfItDoesntExist(globalGanache)


def getMyDeployments():
    myDeployments = {}
    myDeployments["localGanache"] = "0x64e12B3EB49A1684a108bF2C345D35badd45004A"
    myDeployments["globalGanache"] = "0xb68b1F43b4C4C85FDEA689432d643Dc469b309ec"
    return myDeployments
