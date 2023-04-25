import yaml
import shutil
import platform


def getConfigFilePath():
    configFilePathMac = "/Users/imadhui/.brownie/network-config.yaml"  # change these paths to more generic ones
    configFilePathWindows = "C:\\Users\\Administrator\\.brownie\\network-config.yaml"
    if platform.system() == "Windows":
        return configFilePathWindows
    else:
        return configFilePathMac


def getConfigFilePathModified():
    configFilePathMacModified = "/Users/imadhui/.brownie/network-config-modified.yaml"
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
    myDeployments["localGanache"] = "0x93C07782D5bd0Ce6E118d72a2d212B4A97FAE857"
    myDeployments["globalGanache"] = "0x1c1887c59BB35F8Bf10A9A8aC675f4fff8244d5e"
    myDeployments["sepolia"] = "0xa341dC25792C79430E6973Db8915f7751001A262"
    return myDeployments
