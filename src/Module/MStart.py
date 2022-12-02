import os
import subprocess
import platform
from .db import MDataBase as db


class MStart:

    def __init__(self) -> None:
        pass

    def FindFolder(self):
        dirname = 'C:\\MyWallpaper\\'
        if ((os.path.exists(dirname) and os.path.exists(dirname+'favorite') and os.path.exists(dirname+'core') and os.path.exists(dirname+'Img')) != True):
            try:
                os.makedirs(dirname+'Favorite')
                os.makedirs(dirname+'Core')
                os.makedirs(dirname+'Logs')
                os.makedirs(dirname+'Img')
                db().dbInit()

            except OSError:
                return False

        return db().dbInit()

    def ChekConection(self):
        while True:
            try:
                subprocess.check_output(["ping", "www.ya.ru"])
                return True
            except subprocess.CalledProcessError:
                return False

    def getPlatform(self):
        checker = platform.architecture()[0]
        return True
