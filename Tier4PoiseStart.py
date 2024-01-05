# Doney Tran
# A program that cycles through E.G.O gifts until the components for a tier 4 poise gift
# are found.

import pyautogui
import cv2
import sys
import time

# Region to select gifts (1148, 330) (1761, 814)

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
    Horseshoe = pyautogui.locateOnScreen("Horseshoe.png", confidence=.5, region=(1148, 330, 613, 484))
    print(Horseshoe)
    pyautogui.moveTo(Horseshoe)
main()
