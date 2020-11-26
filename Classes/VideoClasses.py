class VideoOrchestrator:
    def __init__(self):
        self.videoClips = None

    def setVideos(self, pVideoList):
        self.videoClips = pVideoList

    def addVideos(self, pVideo):
        self.videoClips.append(pVideo)

    def getVideos(self):
        return self.videoClips

###



