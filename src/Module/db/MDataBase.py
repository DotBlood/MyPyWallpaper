import sqlite3


class MDataBase:
    def __init__(self) -> None:
        self.connect = sqlite3.connect('C:\\MyWallpaper\\Core\\db.sqlite')
        self.cur = self.connect.cursor()

    def dbInit(self):
        self.cur.execute("""CREATE TABLE TEST (id int)""")
        return True

    def get(self):
        pass

    def create(self):
        pass

    def uppdate(self):
        pass

    def remove(self):
        pass
