from datetime import datetime
from Domain.Camera import Camera
from moviepy.editor import concatenate_videoclips
import os

class BootOrder:
    def __init__(self, pID, pPath):
        self.OrderId = pID
        self.Path = pPath
        self.Cameras = []
        self.Status = "Ready"
        self.StatusMessage = ""
        self.StartTime = str(datetime.now())    ##I don't love this, but right now I can't serialize a raw datetime - i know there's a better way.  More to come.
        self.EndTime = None
        self.BootOrderMontage = None

    # def AddCamera(self, pCamera):
    #     self.Cameras.append(pCamera)

    def AssignCameras(self, pCameraList):
        for camera in pCameraList:
            camera.SetPath(f"{self.Path}/{camera.CameraName}")
            camera.SetVideos()
            self.Cameras.append(camera)

    def CreateMontage(self):
        for camera in self.Cameras:
            camera.CreateMontage()

        allCameraMontages = [camera.CameraMontage for camera in self.Cameras]
        self.BootOrderMontage = concatenate_videoclips(allCameraMontages, method='compose')

    def WriteMontage(self, pOutputDirectory):
        fileName = f"{self.OrderId}.mp4"
        outputdir = os.path.join(pOutputDirectory, fileName)

        with self.BootOrderMontage as b:
            b.write_videofile(outputdir)
        



    #there's kind of a lot here... this really probably needs to be factored out a bit
    # def ConfigToCameras(self, pCameraConfig):
    #     cameraConfigs = pCameraConfig
    #     cameraObjs = []

    #     #For each subdirectory in my boot order, make a camera object if the directory name matches our list of configured cameras
    #     for subDir in os.scandir(self.Path): 
    #         if (subDir.is_dir() and subDir.name in cameraConfigs.keys()):
    #             cameraName = subDir.name
    #             cameraObj = Camera(cameraName)
    #             cameraObjs.append(cameraObj)

    #     #for each of our camera objects
    #     for cameraObj in cameraObjs:
    #         cameraName = cameraObj.CameraName
    #         subCameraCandidateList = cameraConfigs[cameraName]['subCameras']

    #         #Assign subcameras if there are some
    #         if len(subCameraCandidateList) > 0:
    #             for subCameraCandidate in subCameraCandidateList:
    #                 if subCameraCandidate in [subDir.name for subDir in os.scandir(self.Path)]:
    #                     subCameraObj = Camera(subCameraCandidate)
    #                     subCameraObj
    #                     cameraObj.subCameras.append(Camera(subCameraCandidate))
                
    #         #S

            

    #         self.Cameras.append(cameraObj)


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