from Domain.Camera import Camera
from Domain.BootOrder import BootOrder
from Domain.Video import Video
from Service.CameraFactory import CameraFactory
from Service.BootOrderFactory import BootOrderFactory
#from Service.BootOrderVideoOrchestration import BootOrderVideoOrchestration


#from Defs import ioClasses as io
import json
import os
import pprint
import sys
import importlib

def main():
    ##Read in Configuration Data
    with open("Config/config.json") as json_data_file:
        configData = json.load(json_data_file)

    ##Input Dir
    inputDir = configData['CreationInputs']

    ##OutputDir
    outputDir = configData['CreationOutputs']

    ##LoggingDir
    loggingDir = configData['Logging']

    ##CamerasConfig
    cameraConfigList = configData['Cameras']

    ##Use CameraFact Class to build our cameras
    cameraFactoryObj = CameraFactory(cameraConfigList)
    cameraObjs = cameraFactoryObj.ReturnCameras()

    #Use BootOrderFact Class to build yield our boot orders
    BootOrderFactoryObj = BootOrderFactory(inputDir)
    bootOrderObjs = BootOrderFactoryObj.ReturnBootOrders()



    #Assign Cameras to each bootOrder
    #Renderer = BootOrderVideoOrchestration()
    for bootOrder in bootOrderObjs:
        bootOrder.AssignCameras(cameraObjs)
        bootOrder.CreateMontage()
        bootOrder.WriteMontage(outputDir)
        
        #Renderer.RenderBootOrder(bootOrder, outputDir)        


    

if __name__ == "__main__": 
    main() 