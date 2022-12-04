import platform
import random
import requests
import ctypes

from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By


class MWallpaper:
    def __init__(self) -> None:
        self.platformX = platform.architecture()[0]
        self.dImg = str(Path.home())+'\\documents\\MyPyWallpaper\\Img\\'
        self.ua = dict(DesiredCapabilities.CHROME)
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.browser = webdriver.Chrome(chrome_options=self.options)

    def getImmage(self):
        serch = ['минимализм', 'собаки', 'кошки', 'животные',
                 'архетектура']  # добавить json файл с разными запросами

        # открыие браузера
        try:
            self.browser.get(
                f"https://yandex.ru/images/search?text= {random.choice(serch)} HD обои")
            imgSerch = self.browser.find_elements(
                By.CLASS_NAME, "serp-item__link")
            self.browser.get(imgSerch[random.randint(
                0, len(imgSerch))].get_attribute('href'))
            url = self.browser.find_element(
                By.CLASS_NAME, "MMImage-Origin").get_attribute('src')
        except:
            return False  # ошибка в логи + добавить обработку всех ошибок

        # Скачака обоев
        try:
            img = requests.get(url)
        except requests.exceptions.RequestException as e:
            return False  # ошибка в логи

        # записывание файла
        try:
            img_options = open(self.dImg+"img1.jpg", 'wb')
            img_options.write(img.content)
            img.close()
            return self.setWallpaper()
        except OSError:
            return False  # ошибка в логи + добавить обработку всех ошибок

    def setWallpaper(self):
        SPI_SETDESKWALLPAPER = 20
        SPIF_UPDATEINIFILE = 1

        # 64bit
        if (self.platformX == "64bit"):
            try:
                ctypes.windll.user32.SystemParametersInfoW(
                    SPI_SETDESKWALLPAPER, 0, self.dImg+"img1.jpg", SPIF_UPDATEINIFILE)
                return True
            except OSError:
                return False  # ошибка в логи

        # 32bit
        elif (self.platformX == "32bit"):
            try:
                ctypes.windll.user32.SystemParametersInfoA(
                    SPI_SETDESKWALLPAPER, 0, self.dImg+"img1.jpg", SPIF_UPDATEINIFILE)
                return True
            except OSError:
                return False  # ошибка в логи

        else:
            return False
