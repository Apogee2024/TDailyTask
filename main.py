import time
import pyautogui
PORTAL ='insertYourPortalHere'
from grayscale import autopm,find_and_click_grayscale


def page_down():
    """function for pressing page down"""
    pyautogui.press("pagedown")
    time.sleep(.2)


def move_and_click(x,y):
    """moves to entered coordinates and clicks"""
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(.05)


def findandclick(img_name, ConfidLvL=.7, MouseSpeedTime=.01, PriorLoadingTime=.5):
    """finds and clicks image """
    time.sleep(PriorLoadingTime)
    x,y = pyautogui.locateCenterOnScreen(img_name, confidence=ConfidLvL)
    pyautogui.moveTo(x+(x1/100), y, MouseSpeedTime)
    pyautogui.click()
    time.sleep(1)


def mouse_click_UPM():
    """completes UPM using captured mouse coordinates"""
    time.sleep(1)
    x_list = [399, 397, 402]
    y_list=[647, 777, 909]
    #check off first 3 items
    for _ in range(0,3):
        move_and_click(x_list[_],y_list[_])

    page_down()

    #click 4 to 9
    x_list = [403, 405, 399, 410, 398, 396]
    y_list = [991, 332, 858, 458, 727, 586]

    #click next set of elements
    for _ in range(0,6):
        move_and_click(x_list[_],y_list[_])

    page_down()
    x_list = [415, 401, 404, 399]
    y_list= [551, 952, 680, 819]

    #click next set of elements
    for _ in range(0,4):
        move_and_click(x_list[_],y_list[_])

    #scroll page up so button is visible
    pyautogui.press('pageup',3)
    time.sleep(1)
    findandclick("complete.png")


def full():
    """opens chrome navigates to task page, opens tasks and completes."""
    #open the chrome app on winows
    pyautogui.keyDown('winleft')
    pyautogui.press('r')
    pyautogui.keyUp('winleft')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(3)

    #complete 4 daily tasks defined by images
    for _ in range(0, 4):
        #open new tab
        pyautogui.hotkey('ctrl', 't')
        pyautogui.write(PORTAL)
        pyautogui.press('enter')
        # wait for page to load after writing url
        time.sleep(5)
        
        #open the task which opens in a new tab
        findandclick(f"task{_}.png")
        
        time.sleep(5)
        findandclick("start_button.png")

        time.sleep(1)
        findandclick("procedures.png")

        time.sleep(1)
        findandclick('procedures(2).png')
        
        #complete the form
        autopm()

        findandclick("complete.png")

 


def in_tabs_any():
    """completes forms for the 4 open tabs"""
    # 5 sec wait time to switch to correct window
    time.sleep(5)
    for _ in range(0, 4):
        #start task
        find_and_click_grayscale("start_button.png")
        
        time.sleep(2)
        find_and_click_grayscale('taskTag.png')
        #complete the checklist
        autopm()
        #complete current task
        find_and_click_grayscale("complete.png")
        time.sleep(1)
        
        #go over to next tab
        pyautogui.hotkey('ctrl', 'tab')
 

if __name__ == "__main__":
    in_tabs_any()

 

 

 

