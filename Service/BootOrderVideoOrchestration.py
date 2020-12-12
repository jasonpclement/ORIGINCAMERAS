from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

class BootOrderVideoOrchestration:
    def __init__(self):
        pass
        
    def RenderBootOrder(self, pBootOrder, pTargetDir):
        bootOrder = pBootOrder
        bootOrderConcat = None
        cameraConcat = None


        bootOrderClips = []
        #For each camera in this bootOrder
        for camera in bootOrder.Cameras:
            if camera.subCameraOnly == True:
                continue

            cameraClips = []
            subCameraClips = []

            #For each video in this camera
            for video in camera.Videos:
                videoClip = VideoFileClip(f"{video.GetFullPath()}").crossfadein(2.0).fadeout(2.0)
                cameraClips.append(videoClip)

            #concat all videos for this camera
            cameraConcat = concatenate_videoclips(cameraClips, method='compose')

            #append result to bootOrder clips
            bootOrderClips.append(cameraConcat)

            for subCamera in bootOrder.Cameras.subCameras:
                for video

        #Concat all bootorder clips
        bootOrderConcat = concatenate_videoclips(bootOrderClips, method='compose')

        fileName = f"{bootOrder.OrderId}.mp4"
        outputdir = os.path.join(pTargetDir, fileName)

        bootOrderConcat.write_videofile(outputdir)
        bootOrderConcat.close()

        