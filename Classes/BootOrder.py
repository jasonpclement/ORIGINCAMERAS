from datetime import datetime

class BootOrder:
    def __init__(self, pID, pPath):
        self.OrderId = pID
        self.Path = pPath
        self.Cameras = []
        self.Status = "Ready"
        self.StatusMessage = ""
        self.StartTime = str(datetime.now())    ##I don't love this, but right now I can't serialize a raw datetime - i know there's a better way.  More to come.
        self.EndTime = None

    def AddCamera(self, pCamera):
        self.Cameras.append(pCamera)

    def GetAllVideos(self):
        videoOutput = []
        for camera in self.Cameras:
            for video in camera.Videos:
                videoOutput.append(video)
        return videoOutput

    def UpdateStatus(self, pStatus, pMessage=""):
        self.Status = pStatus 
        self.StatusMessage = pMessage
        self.EndTime = str(datetime.now()) 