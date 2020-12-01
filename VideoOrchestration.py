from Classes import VideoClasses, BootOrder, Camera
from Defs import ioClasses as io
import json
import os
import pprint
import sys

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

    ##Create a master dict to coordinate processing, and for easy logging
    bootsToProcess = [subDir for subDir in os.scandir(inputDir) if subDir.is_dir()]
    bootOrders = []
    

    #foreach directory create a bootorder
    for dir in bootsToProcess:
        bootOrder = BootOrder.BootOrder(dir.name, dir.path)
        
        #foreach directory under the bootorder add cameras
        cameraDirs = [subDir for subDir in os.scandir(bootOrder.Path) if subDir.is_dir()]
        for cameraDir in cameraDirs:
            camera = Camera.Camera(cameraDir.name, cameraDir.path)
            camera.SetVideos()
            bootOrder.AddCamera(camera)

        ##add to bootOrders
        bootOrders.append(bootOrder)

    ##Begin Processing
    for bootOrder in bootOrders:
        #I Won't lie, I have very little concept try catch protocol in python - I'll throw in a div0 = 1/0 just to give this a poor test
        try:
            vc = VideoClasses.VideoCompiler()
            #div0 = 1/0

            vc.setVideos(bootOrder.GetAllVideos())
            vc.writeOutput(outputDir, f'{bootOrder.OrderId}.mp4')
        #Oh shh...
        except:
            e = sys.exc_info()[0]
            bootOrder.UpdateStatus('Error', e)
        #We good
        else:  
            bootOrder.UpdateStatus('Complete')
        #Log the bootOrder
        finally:
            #print(io.ClassEncoder().encode(bootOrder))
            io.BootOrderLog(loggingDir, bootOrder)


if __name__ == "__main__": 
    main() 