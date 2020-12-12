from moviepy.editor import VideoFileClip

##This class is fairly incomplete, i have no actual concept of adding effects yet, but establishing the pattern now
class Video:
    def __init__(self, pVideoName, pPath):
        self.VideoName = pVideoName
        self.Path = pPath
        self.Clip = VideoFileClip(f"{self.GetFullPath()}").crossfadein(2.0).fadeout(2.0)



    def GetFullPath(self):
        return f"{self.Path}/{self.VideoName}"

