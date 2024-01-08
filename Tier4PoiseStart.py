# Doney Tran
# A program that cycles through E.G.O gifts until the components for a tier 4 poise gift
# are found.

import pyautogui
import sys
import time
import psutil
pyautogui.PAUSE = .6
# MD3N stands for mirror dungeon 3 normal
# Region to select gifts (1148, 330) (1761, 814)
# Region to select mirror dungeon normal (130, 261) (555, 891)

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
        Refresh = pyautogui.locateOnScreen("Refresh.png",
                                           grayscale=True,
                                           confidence=.9)

        pyautogui.moveTo(Refresh)
        pyautogui.leftClick()
    except:
        print("Could not refresh the gifts")

def exitAndClear(MD3N):
    try:
        #goBack = pyautogui.locateOnScreen("exitArrow.png", grayscale=True, confidence=.9)
        pyautogui.press("escape")
        pyautogui.moveTo(MD3N)
        pyautogui.leftClick()
        Halt = pyautogui.locateOnScreen("Halt.png",
                                 grayscale=True,
                                 confidence=.9)
        pyautogui.moveTo(Halt)
        pyautogui.leftClick()
        pyautogui.press("enter")
        giveUp = pyautogui.locateOnScreen("GiveUp.png",
                                 grayscale=True,
                                 confidence=.9)
        pyautogui.moveTo(giveUp)
        pyautogui.leftClick()
        pyautogui.press("enter")
    except:
        print("Failed to exit E.G.O gift selection")

def enterDungeon(MD3N):


    try:
        pyautogui.moveTo(MD3N)
        pyautogui.leftClick()
        pyautogui.press("enter")
    except:
        print("Failed to click on Mirror Dungeon")


#Idk some recursion, maybe do something after returning to the first call of this function
def findPoiseGift(isRefreshed):
        foundClover = False
        foundHorseshoe = False
        foundGifts = False
        # Picking poise
        try:
            Poise = pyautogui.locateOnScreen("Poise.png",
                                             grayscale=True,
                                             confidence=.9)
            pyautogui.moveTo(Poise)
            pyautogui.leftClick()
        except:
            print("Failed to find poise")

        try:
            Clover = pyautogui.locateOnScreen("Clover.png", grayscale=True, confidence=.9)
            pyautogui.moveTo(Clover)
            pyautogui.leftClick()
            foundClover = True
        except:
            print("Failed to grab clover")
            if not isRefreshed:
                refreshGifts()
                isRefreshed = True
                findPoiseGift(isRefreshed)

        if foundClover == True:
            try:
                Horseshoe = pyautogui.locateOnScreen("Horseshoe.png",
                                                     grayscale=True,
                                                     confidence=.9,
                                                     region=(1148, 330, 613, 484))
                pyautogui.moveTo(Horseshoe)
                foundHorseshoe = True
            except:
                print("Failed to grab horseshoe")
                if not isRefreshed:
                    refreshGifts()
                    isRefreshed = True
                    findPoiseGift(isRefreshed)

        if (foundClover and foundHorseshoe):
            print("Success")
            foundGifts = True

        return foundGifts


def main():

    gameIsOpen = "LimbusCompany.exe" in (i.name() for i in psutil.process_iter())
    foundGift = False

    MD3N = pyautogui.locateOnScreen("MD3N.png",
                                    grayscale=True,
                                    confidence=.9,
                                    region=(130, 261, 425, 761))
    if gameIsOpen:
        print("Running Script")
        # TODO add key to exit the program whenever, keep track of how many times it takes to reroll and
        # TODO maybe do some averages
        # Entering mirror dungeon
        enterDungeon(MD3N)

        while not foundGift:
            enterDungeon(MD3N)
            isRefreshed = False
            foundGift = findPoiseGift(isRefreshed)
            if not foundGift:
                exitAndClear(MD3N)


    else:
        print("Could not find Limbus Company, Exiting")
        sys.exit()

main()

