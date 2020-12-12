from .Video import Video
from moviepy.editor import vfx
from moviepy.editor import concatenate_videoclips, VideoFileClip
import os

class Camera:
    def __init__(self, pName, pSubcameraOnly = False):
        self.CameraName = pName
        self.CameraPath = ""
        self.Videos = []
        self.subCameras = []
        self.subCameraOnly = pSubcameraOnly
        self.CameraMontage = None

    def SetPath(self, pPath):
        self.CameraPath = pPath

    def SetVideos(self):
        videoFiles = [videoFile for videoFile in os.scandir(self.CameraPath) if videoFile.is_file()]
        for videoFile in videoFiles:
            self.Videos.append(Video(videoFile.name, self.CameraPath))

    def SetSubCameras(self, pSubCameras):
        self.subCameras = pSubCameras





class Camera001(Camera):
    def __init__(self, pName, pSubcameraOnly = False):
        super().__init__(pName, pSubcameraOnly)
        self.FXList = []

    def CreateMontage(self):
        allVideoClips = [video.Clip for video in self.Videos]
        montageRaw = (concatenate_videoclips(allVideoClips, method='compose'))
        montageProduced = (
                            montageRaw.fx(  VideoFileClip.subclip   ,  t_start=0, t_end=10      )
                                      .fx(  vfx.fadeout              ,  duration=2.0            )
                          )
        self.CameraMontage = montageProduced




class Camera002(Camera):
    def __init__(self, pName, pSubcameraOnly = False):
        super().__init__(pName, pSubcameraOnly)
        self.FXList = []

    def CreateMontage(self):
        allVideoClips = [video.Clip for video in self.Videos]
        montageRaw = (concatenate_videoclips(allVideoClips, method='compose'))
        montageProduced = (
                            montageRaw.fx(  vfx.rotate                  , angle=180     )
                                      .fx(  vfx.fadeout                 , duration=2.0  )
                          )
        self.CameraMontage = montageProduced




class Camera003(Camera):
    def __init__(self, pName, pSubcameraOnly = False):
        super().__init__(pName, pSubcameraOnly)
        self.FXList = []

    def CreateMontage(self):
        allVideoClips = [video.Clip for video in self.Videos]
        montageRaw = (concatenate_videoclips(allVideoClips, method='compose'))
        montageProduced = (
                            montageRaw.fx(  vfx.speedx                  ,   factor=3        )
                                      .fx(  vfx.fadeout                 ,   duration=2.0    )
                          )
        self.CameraMontage = montageProduced




class Camera004(Camera):
    def __init__(self, pName, pSubcameraOnly = False):
        super().__init__(pName, pSubcameraOnly)
        self.FXList = []

    def CreateMontage(self):
        allVideoClips = [video.Clip for video in self.Videos]
        montageRaw = (concatenate_videoclips(allVideoClips, method='compose'))
        montageProduced = (
                            montageRaw.fx( vfx.blackwhite                                   )                     
                                      .fx( vfx.fadeout                 ,   duration=2.0     )
                          )
        self.CameraMontage = montageProduced



