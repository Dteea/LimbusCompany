# Doney Tran
# A program that cycles through E.G.O gifts until the components for a tier 4 poise gift
# are found.

import pyautogui
import sys
import time
import psutil

# Region to select gifts (1148, 330) (1761, 814)
# Region to select mirror dungeon normal (130, 261) (555, 891)
# Region to select
def getMouseCoord():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr)
            print('\b' * (len(positionStr) + 2))
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        print('\n')

def main():
    gameIsOpen= "LimbusCompany.exe" in (i.name() for i in psutil.process_iter())
    if gameIsOpen:
        print("Running Script")


        try:
            MD3N = pyautogui.locateOnScreen("MD3N.png", grayscale=True, confidence=.9, region=(130, 261, 425, 761))
            pyautogui.moveTo(MD3N)
            pyautogui.leftClick()
        except:
            print("Failed to click on Mirror Dungeon")

        try:
            Horseshoe = pyautogui.locateOnScreen("Horseshoe.png", grayscale=True, confidence=.5, region=(1148, 330, 613, 484))
            pyautogui.moveTo(Horseshoe)
        except:
            print("Failed to grab horseshoe")



    else:
        print("Could not find Limbus Company, Exiting")
        sys.exit()

main()
