# Doney Tran
# A program that cycles through E.G.O gifts until the components for a tier 4 poise gift
# are found.

import pyautogui
import sys
import time
import psutil

# MD3N stands for mirror dungeon 3 normal
# Region to select gifts (1148, 330) (1761, 814)
# Region to select mirror dungeon normal (130, 261) (555, 891)
# Region to select

# Future, use pictures of gifts instead of the name
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



def refreshGifts():
    try:
        Refresh = pyautogui.locateOnScreen("Refresh.png", grayscale=True, confidence=.9)
        pyautogui.moveTo(Refresh)
        time.sleep(1)

    except:
        print("Could not refresh the gifts")


def main():
    foundClover, foundHorseshoe = False
    gameIsOpen = "LimbusCompany.exe" in (i.name() for i in psutil.process_iter())
    if gameIsOpen:
        print("Running Script")

        # Entering mirror dungeon
        try:
            MD3N = pyautogui.locateOnScreen("MD3N.png", grayscale=True, confidence=.9, region=(130, 261, 425, 761))
            pyautogui.moveTo(MD3N)
            pyautogui.leftClick()
            pyautogui.sleep(.5)
            pyautogui.press("enter")
            time.sleep(1)
        except:
            print("Failed to click on Mirror Dungeon")

        # Picking poise
        try:
            Poise = pyautogui.locateOnScreen("Poise.png", grayscale=True, confidence=.9)
            pyautogui.moveTo(Poise)
            pyautogui.leftClick()
            time.sleep(.5)
        except:
            print("Failed to find poise")

        # while(!foundClover && !foundHorseshoe):
        try:
            Clover = pyautogui.locateOnScreen("Clover.png", grayscale=True, confidence=.9)
            pyautogui.moveTo(Clover)
            pyautogui.leftClick()
            foundClover = True
        except:
            print("Failed to grab clover")
            refreshGifts()

        try:
            Horseshoe = pyautogui.locateOnScreen("Horseshoe.png", grayscale=True, confidence=.9, region=(1148, 330, 613, 484))
            pyautogui.moveTo(Horseshoe)
            foundHorseshoe = True
        except:
            print("Failed to grab horseshoe")
            refreshGifts()




    else:
        print("Could not find Limbus Company, Exiting")
        sys.exit()

main()

