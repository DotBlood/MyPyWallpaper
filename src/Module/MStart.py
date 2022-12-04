import os
from pathlib import Path
import time
import subprocess


class MStart:

    def __init__(self) -> None:
        pass

    def FindFolder(self):
        dirname = str(Path.home())+'\\documents\\MyPyWallpaper\\'
        print(dirname)
        if not (os.path.exists(dirname) and os.path.exists(dirname+'Log') and os.path.exists(dirname+'Img')):
            print('s1 - Не найдены файлы')
            try:
                os.makedirs(dirname+'Log')
                os.makedirs(dirname+'Img')
                print('s1 Init Reload')
                print('s1 ok')
                return True
            except OSError:
                return False # ошибка [создания папок]
        else:
            print('s1 ok')
            return True

    def ChekConection(self):
        CInternet = self.Ping()
        if not CInternet:
            while not CInternet:
                if CInternet:
                    print('s2 ok')
                    break
                else:
                    time.sleep(5)
                    CInternet = self.Ping()
        else:
            print('s2 ok')
            return True

    def Ping(self):
        while True:
            try:
                subprocess.check_output(["ping", "www.ya.ru"])
                return True
            except subprocess.CalledProcessError:
                print('s2 - Error')
                return False
