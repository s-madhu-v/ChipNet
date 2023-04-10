from urllib.parse import urlparse
import shutil
import docker
import git
import os

# client = docker.from_env()

class dImage:
    def __init__(self, client, repo, imgName):
        # Link for the github repository containing the dockerfile
        self.repo = repo
        self.client = client
        self.imgName = imgName
        # path where all cloned github repos are stored
        self.clonesPath = "./cloned"
        self.repoName = urlparse(repo).path.split('/')[-1].split('.')[0]
        self.localPath = f"{self.clonesPath}/{self.repoName}"
        self.dfilePath = "./Dockerfile"
        self.buildLogs = ""

    def cloneRepo(self):
        print(f"Cloning the repository: {self.repoName}")
        git.Repo.clone_from(self.repo, self.localPath)
        print(f"Cloned To: {self.localPath}")

    def deleteClone(self):
        try:
            shutil.rmtree(self.localPath)
            print(f"Folder {self.localPath} deleted successfully!")
        except OSError as e:
            print(f"Error deleting folder: {e.strerror}")

    def buildImage(self, args):
        self.cloneRepo()
        image, logs = self.client.images.build(path=self.localPath, dockerfile=self.dfilePath, tag=self.imgName, buildargs=args)
        self.buildLogs = logs
        self.deleteClone()
        print(f"Image is Built from {self.repo} with name: {self.imgName}")
        return image

    def printLogs(self):
        for line in self.buildLogs:
            print(line.get('stream', '').strip())
