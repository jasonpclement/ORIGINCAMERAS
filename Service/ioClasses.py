from datetime import datetime
import json

class ClassEncoder(json.JSONEncoder):
        def default(self, o):
            return o.__dict__

def BootOrderLog(pLoggingDir, pBootOrder):
    #encodedBootOrder = ClassEncoder().encode(pBootOrder)

    logFilename = f"logging_{datetime.today().strftime('%Y%m%d')}.txt"
    fullPath = f"{pLoggingDir}/{logFilename}"
    text_file = open(fullPath, "a")

    outInfo = json.dumps(pBootOrder, indent=4, cls=ClassEncoder)
    #foo.__dict__
    #json.dumps({datetime.now().strftime("%m/%d/%Y, %H:%M:%S"):pStrToLog})

    n = text_file.write(outInfo)
    text_file.close()


