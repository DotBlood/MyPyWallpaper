import os
from time import sleep
import getpass


USER_NAME = getpass.getuser()


def InitProject():
    try:
        file_path = os.path.dirname(
            os.path.realpath(__file__))+'\MyPyWallpaper.exe'
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "MyPyWallpaper.bat", "w+") as bat_file:
            bat_file.write(r'start "" %s' % file_path)
            bat_file.close()

    except OSError as e:
        print(e)

    return exit(0)


InitProject()
