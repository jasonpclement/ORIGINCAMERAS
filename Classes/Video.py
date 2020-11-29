##This class is fairly incomplete, i have no actual concept of adding effects yet, but establishing the pattern now
class Video:
    def __init__(self, pVideoName, pPath):
        self.VideoName = pVideoName
        self.Path = pPath
        self.fx = []

    def GetFullPath(self):
        return f"{self.Path}/{self.VideoName}"

