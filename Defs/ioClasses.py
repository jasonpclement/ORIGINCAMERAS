from datetime import datetime
import json

def LogProcessing(pLoggingDir, pStrToLog):
    logFilename = f"logging_{datetime.today().strftime('%Y%m%d')}.txt"
    fullPath = f"{pLoggingDir}/{logFilename}"
    text_file = open(fullPath, "a")

    outInfo = json.dumps({datetime.now().strftime("%m/%d/%Y, %H:%M:%S"):pStrToLog})


    n = text_file.write(outInfo)
    text_file.close()


##Just for quick testing
if __name__ == "__main__": 
    LogProcessing("C:/Users/jason/OneDrive/Documents/repos/OriginCameras/Logging/", 'bleh')