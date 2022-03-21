from pyautogui import *
import pyautogui
import time
import keyboard

broke = 0
counter = 0
print("getting ready...")
time.sleep(1)

while not keyboard.is_pressed("`"):
    if pyautogui.locateOnScreen("fish.png", region=(755, 573, 350, 30), confidence=0.7) is not None:
        print("fish")
        pyautogui.press("SPACE")
        broke = 0

    elif pyautogui.locateOnScreen("learn.png", grayscale=True, confidence=0.9) is not None:
        print("learning")
        pyautogui.click(990, 639, clicks=2, interval=0.1)
        broke = 0

    elif pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.9) is not None:
        print("battle")
        pyautogui.click(679, 668, clicks=3, interval=1)
        time.sleep(5)
        broke = 0

    elif pyautogui.locateOnScreen("evo.png", grayscale=True, confidence=0.9) is not None:
        print("evolve")
        pyautogui.click(825, 533, clicks=2, interval=0.1)
        broke = 0

    elif broke == 25:
        print('reel')
        pyautogui.click(x=196, y=580, clicks=3, interval=0.1)
        time.sleep(3)
        broke = 0

    broke += 1
