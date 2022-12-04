from pathlib import Path
import datetime


class LError:

    def __init__(self) -> None:
        self.date = datetime.datetime.strptime('2018-01-01', '%Y-%m-%d').date()
        self.dirLog = f"{Path.home()}\\documents\\MyPyWallpaper\\Log\\"

    def Logger(self, msg, ltype, critical) -> None:
        print(critical)
        if ltype == 0:
            sufix = "Error"
        if ltype == 1:
            sufix = "Log"
        if msg:
            try:
                file = open(self.dirLog + str(self.date) +
                            sufix + ".log", 'w+')
                file.write(msg)
                file.close()
                if critical:
                    print('отработал')
                    return exit()
            except:
                pass
        else:
            try:
                file = open(self.dirLog + str(self.date) +
                            sufix + ".log", 'w+')
                file.write('неизвестная ошибка.')
                file.close()
                if critical:
                    return exit()
            except:
                pass


LError().Logger(msg="test", ltype=0, critical=0)
