import ctypes
import datetime
import subprocess
import pyautogui
import time

directory = "c:\Wallpaper"
darkImagePath = directory + "\darkflower.jpg"
lightImagePath = directory + "\lightcar.jpg"

now = datetime.datetime.now()

def changeToDark(imagePath):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, imagePath, 3)
    return

def changeToLight(imagePath):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, imagePath, 3)
    return

print(now.hour)


while(True):
    if now.hour >= 8 and now.hour <= 17:
        changeToLight(lightImagePath)
    else:
        changeToDark(darkImagePath)

