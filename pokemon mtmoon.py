from pyautogui import *
import pyautogui
import time
import keyboard

orenum = input("What ore r u mining? r,b,g").lower()
stand = input("Where r u standing? u,d,l,r").lower()
if stand == "u":
    stand = (887, 561, 80, 80)
elif stand == "d":
    stand = (867, 420, 100, 100)
elif stand == "l":
    stand = (940, 501, 100, 100)
elif stand == "r":
    stand = (827, 501, 100, 100)

if orenum == "r":
    ore = "active.png"
if orenum == "b":
    ore = "active2.png"
if orenum == "g":
    ore = "active1.png"

broke = 0
counter = 0
print("getting ready...")
time.sleep(2)

while not keyboard.is_pressed("`"):
    if pyautogui.locateOnScreen(ore, region=stand, confidence=0.95) is not None and counter == 0:
        print("mine")
        pyautogui.press("SPACE")
        counter = 1
        broke = 0
    elif pyautogui.locateOnScreen("inactive.png", region=stand, confidence=0.95) is not None:
        print("cool")
        counter = 0
        broke = 0
    elif pyautogui.locateOnScreen("battle.png", grayscale=True, confidence=0.9) is not None:
        print("battle")
        counter = 0
        broke = 0
        for i in range(2):
            pyautogui.click(679, 668)
            time.sleep(1)
        time.sleep(2)
    elif pyautogui.locateOnScreen("learn.png", grayscale=True, confidence=0.9) is not None:
        print("learning")
        pyautogui.click(990, 639)

    elif pyautogui.locateOnScreen("evo.png", grayscale=True, confidence=0.9) is not None:
        print("evolve")
        pyautogui.click(825, 533)

    broke += 1
    if broke == 30:
        print("cooldown got skipped")
        counter = 0
    time.sleep(0.5)


# (x=679, y=668)
# (x=825, y=533)evo
# region=(827, 501, 100, 100) stand on the right of ore
# region=(887, 561, 80, 80) stand on top of ore
# region=(940, 501, 100, 100) stand on the left of ore
# region=(867, 420, 100, 100) stand on bottom of ore
