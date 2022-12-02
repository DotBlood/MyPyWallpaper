from src.Module import MStart, MWallpaper
from src.Module.db import MDataBase as db

import time


def Start():
    if MStart().FindFolder():
        Connection = MStart().ChekConection()
        if Connection == False:
            while True:
                if Connection == True:
                    break
                else:
                    time.sleep(5)
                    Connection = MStart().ChekConection()
        else:
            pass


if __name__ == "__main__":
    Start()
