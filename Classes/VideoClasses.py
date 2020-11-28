from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

class VideoCompiler:
    def __init__(self):
        self.videoClips = []

    def setVideos(self, pClips):
        for clip in pClips:
            videoClip = VideoFileClip(clip)
            videoClip = videoClip.subclip(0, 5) 
            videoClip = videoClip.crossfadein(2.0) 
            videoClip = videoClip.fadeout(2.0)
            self.videoClips.append(videoClip)

    def addVideos(self, pClip):
        self.videoClips.append(VideoFileClip(clip))

    def getVideos(self):
        return self.videoClips

    def writeOutput(self, pTargetDir, pTargetFileName):
        concatVideos = concatenate_videoclips(self.videoClips, method='compose')


        outputdir = os.path.join(pTargetDir, pTargetFileName)
        concatVideos.write_videofile(outputdir)
            

###



