from Classes import VideoClasses
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

    ##initialize array for videos
    inputVideos = []
    processingItems = {}

    ##Create a master dict to coordinate processing, and for easy logging
    bootsToProcess = [subDir for subDir in os.scandir(inputDir) if subDir.is_dir()]
    for dir in bootsToProcess:
        processingItems[dir.name] = {}
        processingItems[dir.name]['Path']= dir.path
        processingItems[dir.name]['Cameras']= {}

        ##Get all the cameras
        cameraFolders = [subDir for subDir in os.scandir(dir) if subDir.is_dir()]
        for subdir in cameraFolders:
            #Get video files for each camera
            videoFiles = [videoFile.name for videoFile in os.scandir(subdir) if videoFile.is_file() and videoFile.name[-4:] == '.mp4']
            processingItems[dir.name]['Cameras'][subdir.name] = {'Path':subdir.path, 'Files':videoFiles}



    ##Begin Processing
    vc = VideoClasses.VideoCompiler()


    for bootOrder in processingItems.keys(): 
        allVideos = []
        print(f"Begin Processing Video for BootOrder:{bootOrder}")
        for camera in processingItems[bootOrder]['Cameras'].keys():
            #print(processingItems[bootOrder]['Cameras'][camera])
            path = processingItems[bootOrder]['Cameras'][camera]['Path']
            cameraVideos = [path + '/' + videoFile for videoFile in processingItems[bootOrder]['Cameras'][camera]['Files']]
            allVideos = allVideos + cameraVideos

        vc.setVideos(allVideos)
        vc.writeOutput(outputDir, f'{bootOrder}.mp4')

    #print(allVideos)

    #print(pp.pprint(processingItems))


    ##Create Video Compiler object and pass all input videos
    #vc = VideoClasses.VideoCompiler()
    #vc.setVideos(inputVideos)
    #vc.writeOutput(outputDir, 'Test.mp4')


    #####

if __name__ == "__main__": 
    main() 