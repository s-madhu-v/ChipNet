from . import Image
import platform


class dContainer:
    def __init__(self, client, repo, name):
        # One name for both image and container
        self.imgName = name
        self.containerName = name + "-container"
        self.client = client
        self.repo = repo

    def createContainer(self, cores, memory, storage, buildArgs):
        img = Image.dImage(self.client, self.repo, self.imgName)
        img = img.buildImage(buildArgs)
        if platform.system() == "Windows":
            c = self.runContainerOnWindows(img, cores, memory, storage)
        else:
            c = self.runContainerOnUNIX(img, cores, memory, storage)
        print(f"Container runs with ID: {c.id}")

    def runContainerOnUNIX(self, img, cores, memory, storage):
        container = self.client.containers.run(
            image=img,
            name=self.containerName,
            detach=True,
            cpuset_cpus=f"0-{cores-1}",
            mem_limit=memory,
            # storage_opt={ 'size': storage }
        )
        return container

    def runContainerOnWindows(self, img, cores, memory, storage):
        container = self.client.containers.run(
            image=img,
            name=self.containerName,
            detach=True,
            cpus=cores,
            mem_limit=memory,
            # storage_opt={ 'size': storage }
        )
        return container
