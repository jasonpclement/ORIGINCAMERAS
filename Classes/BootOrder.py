class BootOrder:
    def __init__(self, pID, pPath):
        self.OrderId = pID
        self.Path = pPath
        self.Cameras = []
        self.Videos = []

    def AddCamera(self, pCamera):
        self.Cameras.append(pCamera)

    def GetAllVideos(self):
        videoOutput = []
        for camera in self.Cameras:
            for video in camera.Videos:
                videoOutput.append(video)
        return videoOutput