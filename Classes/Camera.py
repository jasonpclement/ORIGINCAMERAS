from Classes import Video
import os

class Camera:
    def __init__(self, pCameraName, pCameraPath):
        self.CameraName = pCameraName
        self.CameraPath = pCameraPath
        self.Videos = []

    def SetVideos(self):
            videoFiles = [videoFile for videoFile in os.scandir(self.CameraPath) if videoFile.is_file()]
            for videoFile in videoFiles:
                self.Videos.append(Video.Video(videoFile.name, self.CameraPath))


