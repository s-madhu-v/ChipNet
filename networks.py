import yaml
import shutil

configFilePathMac = "/Users/imadhui/.brownie/network-config.yaml"
configFilePathMacModified = "/Users/imadhui/.brownie/network-config-modified.yaml"


def getGlobalConfig():
    data = None
    with open(configFilePathMac, "r") as f:  # change this for windows too
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
    with open(configFilePathMacModified, "w") as f:  # change this for windows
        yaml.dump(data, f)
    shutil.move(configFilePathMacModified, configFilePathMac)


def addNetworkIfItDoesntExist(networkDict):
    if not networkExists(networkDict["id"]):
        addNetwork(networkDict)


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


def setupNetworks():
    addNetworkIfItDoesntExist(localGanache)
    addNetworkIfItDoesntExist(globalGanache)
