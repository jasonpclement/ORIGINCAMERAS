from Classes import VideoClasses
import json
import os
import pprint

def main():

    ##Read in Configuration Data
    with open("Config/config.json") as json_data_file:
        configData = json.load(json_data_file)

    ##Input Dir
    inputDir = configData['CreationInputs']

    ##OutputDir
    outputDir = configData['CreationOutputs']

    ##initialize array for videos
    inputVideos = []
    processingItems = []

    ##Create a master dict to coordinate processing
    bootsToProcess = [subDir for subDir in os.scandir(inputDir) if subDir.is_dir()]
    for dir in bootsToProcess:
        processingItem = {}
        processingItem[dir.name] = {}
        processingItem[dir.name]['Path']= dir.path
        processingItem[dir.name]['Cameras']= []

        ##Get all the cameras
        cameraFolders = [subDir for subDir in os.scandir(dir) if subDir.is_dir()]
        for subdir in cameraFolders:
            #Get video files for each camera
            videoFiles = [videoFile.name for videoFile in os.scandir(subdir) if videoFile.is_file() and videoFile.name[-4:] == '.mp4']
            processingItem[dir.name]['Cameras'].append({subdir.name:{'Path':subdir.path,'Files':videoFiles}})
        processingItems.append(processingItem)



    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(processingItems)


    ##Create Video Compiler object and pass all input videos
    #vc = VideoClasses.VideoCompiler()
    #vc.setVideos(inputVideos)
    #vc.writeOutput(outputDir, 'Test.mp4')


    #####

if __name__ == "__main__": 
    main() 