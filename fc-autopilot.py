from time import sleep
import glob
import os
import getpass
import keyboard as kb
import threading
import pyautogui

sysFile = open("itinerary.txt","r")

def getCurrSys():
    list_of_files = glob.glob(f"C:\\Users\\{getpass.getuser()}\\Saved Games\\Frontier Developments\\Elite Dangerous\\Journal.*")
    latestJournal = open(max(list_of_files,key=os.path.getmtime),'r')
    currSys = ""
    for line in latestJournal:
        if line.count('StarSystem')>0:
            currSys = line
    currSys = currSys.split('"StarSystem":"')[1].split('"')[0]
    return currSys

def getCoords(image):
    set1 = pyautogui.locateOnScreen(image,confidence=0.75)
    if set1 == None: return None
    else: return set1.left+set1.width//2,set1.top+set1.height//2

def press_and_release(key):
    kb.press(key)
    sleep(0.1)
    kb.release(key)
    pass

def oneJump(sysName):
    press_and_release('w')
    sleep(0.1)
    press_and_release('w')
    sleep(0.1)
    press_and_release('s')
    sleep(0.1)
    press_and_release('s')
    sleep(0.1)
    press_and_release('w')
    sleep(0.1)
    press_and_release('space')
    sleep(6)
    press_and_release('s')
    sleep(0.1)
    press_and_release('s')
    sleep(0.1)
    press_and_release('s')
    sleep(0.1)
    press_and_release('s')
    sleep(0.1)
    press_and_release('w')
    sleep(0.1)
    press_and_release('space')
    sleep(2)
    press_and_release('space')
    kb.press('d')
    sleep(5)
    kb.release('d')
    press_and_release('w')
    sleep(0.25)
    press_and_release('space')
    sleep(2)
    press_and_release('\b')
    sleep(1)
    press_and_release('\b')
    sleep(1.2)
    press_and_release('d')
    sleep(0.1)
    press_and_release('d')
    sleep(0.1)
    press_and_release('space')
    sleep(2.5)
    press_and_release('s')
    sleep(0.5)
    press_and_release('space')
    sleep(0.5)
    press_and_release('space')
    sleep(3)
    x,y = getCoords('images/galmapnav.png')
    pyautogui.moveTo(x,y,1)
    pyautogui.click()
    sleep(0.2)
    x,y = getCoords('images/galmapsearchbar.png')
    pyautogui.moveTo(x,y,1)
    sleep(0.1)
    press_and_release('space')
    sleep(0.2)
    kb.write(sysName)
    sleep(0.5)
    press_and_release('enter')
    sleep(7)
    press_and_release('space')
    sleep(2)
    press_and_release('\b')
    sleep(2)
    press_and_release('\b')
    sleep(0.5)
    press_and_release('\b')
    sleep(0.5)
    press_and_release('4')
    sleep(0.5)
    while pyautogui.locateOnScreen('images/inventory.png',confidence=0.75) == None:
        press_and_release('e')
    sleep(0.5)
    press_and_release('d')
    sleep(0.5)
    press_and_release('d')
    sleep(0.5)
    press_and_release('space')
    sleep(2)
    kb.press('w')
    sleep(3)
    kb.release('w')
    while pyautogui.locateOnScreen('images/trititem.png',confidence=0.75) == None:
        press_and_release('s')
    kb.press('a')
    sleep(30)
    kb.release('a')
    press_and_release('space')
    sleep(0.5)
    press_and_release('space')
    sleep(3)
    press_and_release('\b')
    sleep(0.5)
    press_and_release('\b')
    sleep(0.5)
    press_and_release('\b')
    sleep(0.5)
    sleep(1200)
    pass

def mainLoop():
    ok = 0
    currSys = getCurrSys()
    for line in sysFile.readlines():
        if currSys == line: 
            ok = 1
            continue
        if ok == 1: oneJump(line)
        pass

def listenStop():
    while True:
        if kb.is_pressed('F12'): raise KeyboardInterrupt
            
            
stopThread = threading.Thread(target=listenStop)
stopThread.run()

while True:
    if kb.is_pressed('F11'): mainLoop()