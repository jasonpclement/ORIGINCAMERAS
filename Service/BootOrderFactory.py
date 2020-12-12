import os
from Domain.BootOrder import BootOrder

class BootOrderFactory:
    def __init__(self, pBootOrderDir: str):
        self.BootOrderDir = pBootOrderDir
        self.BootOrderObj = []

        bootDirectories = [subDir for subDir in os.scandir(pBootOrderDir) if subDir.is_dir()]


        for dir in bootDirectories:
            bootOrder = BootOrder(dir.name, dir.path)
            self.BootOrderObj.append(bootOrder)


    def ReturnBootOrders(self):
        return self.BootOrderObj