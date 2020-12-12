from Domain import Camera
from Domain.Camera import Camera001
from inspect import isclass

class CameraFactory:
    def __init__(self, pCamerasConfig: dict):
        self.CamerasConfig = pCamerasConfig
        self.CameraObjs = []

        #loop through camera config and get all cameras
        for cameraDefinition in self.CamerasConfig:
            cameraName = cameraDefinition
            subCameraOnly = self.CamerasConfig[cameraDefinition]['subCameraOnly']

            #if Camera File has an attribute (subclass in this case) with the name coming off the config file then create an object, else blowup
            if hasattr(Camera, cameraName):
                cameraCandidate = getattr(Camera, cameraName)
                if isclass(cameraCandidate):
                    cameraObj = cameraCandidate(cameraName, subCameraOnly)
                else:
                    raise Exception(f"{cameraName} is not a class")
            else:
                raise Exception(f"{cameraName} Class Doesn't Exist")

            self.CameraObjs.append(cameraObj)

        #Set SubCameras:  loop through list of camera objects
        for cameraObj in self.CameraObjs:
            thisCamerasConfig = self.CamerasConfig[cameraObj.CameraName]
            configuredSubCameraNames = thisCamerasConfig['subCameras']

            if len(configuredSubCameraNames) > 0:
                subCameraObjs = [cam for cam in self.CameraObjs if cam.CameraName in configuredSubCameraNames]
                cameraObj.SetSubCameras(subCameraObjs)

    def GetCameraConfig(self):
        return self.CamerasConfig

    def ReturnCameras(self):
        return self.CameraObjs




    

