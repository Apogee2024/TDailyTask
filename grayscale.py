import cv2
import numpy as np
from pyautogui import typewrite,click, screenshot as screen, press
from time import sleep

 
def find_and_click_grayscale(filename):
    """ 
    locates a png on screen using grayscale, clicks, 
    return: bool
    """
    # Capture screen
    sleep(.1)
    screenCap = screen()
    screenShot = cv2.cvtColor(np.array(screenCap), cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray = cv2.cvtColor(screenShot, cv2.COLOR_BGR2GRAY)


    matchElement = cv2.imread(f"{filename}", 0)
    w, h = matchElement.shape[::-1]
    result = cv2.matchTemplate(gray, matchElement, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(result >= threshold)


    # Click on the center of the found element
    if loc[0].any():
        center_x = int(loc[1][0] + w // 2)
        center_y = int(loc[0][0] + h // 2)
        click(center_x, center_y)
        sleep(.2)
        return True

    else:

        return False

 

def find_and_click_complete(filename):
    """ 
    locates complete box on screen using grayscale, clicks, 
    return: bool
    """
    # Capture screen
    sleep(.1)
    screenCap = screen()
    screenShot = cv2.cvtColor(np.array(screenCap), cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray = cv2.cvtColor(screenShot, cv2.COLOR_BGR2GRAY)


    matchElement = cv2.imread(f"{filename}", 0)
    w, h = matchElement.shape[::-1]
    res = cv2.matchTemplate(gray, matchElement, cv2.TM_CCOEFF_NORMED)
    #increased threshold so it doesnt keep clickng same entry button
    threshold = 0.97
    loc = np.where(res >= threshold)


    # Click on the center of the found element

    if loc[0].any():
        center_x = int(loc[1][0] + w // 2)
        center_y = int(loc[0][0] + h // 2)
        click(center_x, center_y)
        sleep(.2)
        
        return True

    else:
        return False

def find_and_enter_grayscale(filename):
    """ 
    locates an entry box, enters text if found 
    return: bool
    """
    # Capture screen

    sleep(.1)
    screenCap = screen()
    screenShot = cv2.cvtColor(np.array(screenCap), cv2.COLOR_RGB2BGR)


    # Convert to grayscale
    gray = cv2.cvtColor(screenShot, cv2.COLOR_BGR2GRAY)


    entryBox = cv2.imread(f"{filename}", 0)
    w, h = entryBox.shape[::-1]
    res = cv2.matchTemplate(gray, entryBox, cv2.TM_CCOEFF_NORMED)
    threshold = 0.98
    loc = np.where(res >= threshold)


    # Click on the center of the entry box and enter ok
    if loc[0].any():
        center_x = int(loc[1][0] + w // 2)
        center_y = int(loc[0][0] + h // 2)
        click(center_x, center_y)
        typewrite('ok')
        return True
    else:
        return False

def autopm(count=0,trycount=0,downcounter=0):
    """completes form ensuring 100% completion"""
    
    if find_and_click_grayscale('pass.png'):
        trycount += 1
        count += 1

    if find_and_click_grayscale('pass(2).png'):
        trycount += 1
        count += 1


    if find_and_click_complete('empty_box(2).png'):
        trycount += 1
        count+=1

    if find_and_click_grayscale('empty_box.png'):
        trycount += 1
        count +=1

    if find_and_enter_grayscale('entry_box.png'):
        trycount += 1
        count += 1

    if find_and_click_grayscale('pass(3).png'):
        trycount += 1
        count +=1

    if find_and_click_complete('completed_box.png'):
        trycount += 1
        count +=1

    if find_and_click_complete('completed(5).png'):
        count +=1
        trycount +=1

    if find_and_click_complete('completed(6).png'):
        count +=1
        trycount +=1

    if find_and_click_complete('completed(7).png'):
        count +=1
        trycount +=1

    if find_and_click_complete('com(8).png'):
        count +=1
        trycount +=1

    if find_and_click_complete('yes(2).png'):
        count +=1
        trycount +=1

    trycount +=1

    #if it has done 6 actions on the page scroll down
    if trycount >= 6:
        press('pagedown')
        sleep(.4)
        #increase downcounter and reset trycount
        downcounter+=1
        trycount = 0

    if downcounter < 8:
        print((count,trycount,downcounter))
        autopm(count, trycount, downcounter)

    else:
        press('pageup',3)
        sleep(1)
 