import pyautogui
from pyfiglet import Figlet
import os
import time
import math

def setting_before_checking():
    """
    merchants = {} # dict pos and color
        for i in range (0, 6, 1):
        print position your mouse before 3s
        time.sleep(3)
        pos+= take mouse position

    return merchants
    """
    pass

def check_availability_place(): #
    """
    searching = True
    while searching:
        for merchant in merchants
            if l'une des couleurs à changé:
                searching = False        
    """
    pass

def activate_merchant_mode():
    pyautogui.press('v')
    time.sleep(1)
    pyautogui.click(970, 890)
    time.sleep(1)
    pyautogui.press('enter')

def loading():
    # loadind ~10s
    for i in range (1, 101, 1):
        os.system("cls")
        f = Figlet(font='slant')
        print (f.renderText('Tracker Loading'))
        print("["+"="*int(math.ceil(i/5))+"]", "{0}%".format(i,))
        time.sleep(0.1)

if __name__ == "__main__":
    loading()
    merchants = setting_before_checking()
    check_availability_place(merchants)
    activate_merchant_mode()
