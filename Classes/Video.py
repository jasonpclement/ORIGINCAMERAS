##This class is fairly incomplete, i have no actual concept of adding effects yet, but establishing the pattern now
class Video:
    def __init__(self, pFX):
        self.fx = []

        if isinstance(pFX, str):
            CameraFiles.append(pFX)
        elif isinstance(pFX, list):
            CameraFiles = pFX
        else
            ##probably need some more robust error handling - to do later?
            raise Exception("Invalid pFX Parameter")
