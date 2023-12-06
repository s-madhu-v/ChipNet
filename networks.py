import yaml
import shutil
import platform


def getConfigFilePath():
    configFilePathMac = "/Users/madhu/.brownie/network-config.yaml"  # change these paths to more generic ones
    configFilePathWindows = "C:\\Users\\Administrator\\.brownie\\network-config.yaml"
    if platform.system() == "Windows":
        return configFilePathWindows
    else:
        return configFilePathMac


def getConfigFilePathModified():
    configFilePathMacModified = "/Users/madhu/.brownie/network-config-modified.yaml"
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
        "chainid": 9999,
        "host": "http://64.227.142.218",
        "id": "globalGanache",
        "name": "globalGanache",
    }
    addNetworkIfItDoesntExist(localGanache)
    addNetworkIfItDoesntExist(globalGanache)


def getMyDeployments():
    myDeployments = {}
    myDeployments["localGanache"] = "0x7a27BBE09b6159e1F4EF1B40e690d61c6F92C65C"
    myDeployments["globalGanache"] = "0xB98Eb6326901980Fd7eB94D9bd70902Add0b8317"
    myDeployments["sepolia"] = "0xa341dC25792C79430E6973Db8915f7751001A262"
    return myDeployments
