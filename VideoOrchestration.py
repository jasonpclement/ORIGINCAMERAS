from Classes import VideoClasses, BootOrder, Camera
import json
import os
import pprint

def main():
    ##This just makes visualizing complex dicts easier - no functional purpose
    pp = pprint.PrettyPrinter(indent=4)

    ##Read in Configuration Data
    with open("Config/config.json") as json_data_file:
        configData = json.load(json_data_file)

    ##Input Dir
    inputDir = configData['CreationInputs']

    ##OutputDir
    outputDir = configData['CreationOutputs']

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
        vc = VideoClasses.VideoCompiler()
        vc.setVideos(bootOrder.GetAllVideos())
        vc.writeOutput(outputDir, f'{bootOrder.OrderId}.mp4')


if __name__ == "__main__": 
    main() 