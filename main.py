import schedule
from time import sleep
from src.Module import MStart
from src.Module.MWallpaper import MWallpaper


def main():
    if (MStart().FindFolder() and MStart().ChekConection()):
        wp()

        # я хочу спать и кушать ;c


def wp():
    MWallpaper().getImmage()
    print('я отработал')
    return True


if __name__ == "__main__":
    main()

    schedule.every().day.at("20:30").do(wp)

    while True:
        schedule.run_pending()
        print('Проверка времени')
        sleep(30)
