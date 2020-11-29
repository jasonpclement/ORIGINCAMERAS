class Camera:
    def __init__(self, pCameraName, pCameraPath, pCameraVideos)
        self.CameraName = pCameraName
        self.CameraPath = pCameraPath
        self.CameraVideos = []

        if isinstance(pCameraVideos, Video):
            CameraVideos.append(pCameraFiles)
        elif isinstance(pCameraVideos, list):
            CameraVideos = pCameraFiles
        else
            ##probably need some more robust error handling - to do later?
            raise Exception("Invalid pCameraVideos Parameter")
