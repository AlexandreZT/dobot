import pyautogui
import time
from random import randint, uniform

class Poubelle(object):

    def check_pods(self):
        pyautogui.click(1224, 1071)
        check = True
        while check:
            try:
                if pyautogui.pixel(1224, 1071) == (96, 190, 53):
                    self.deposer_banque()
                check = False
            except:
                pass

    def charger(self):
        time.sleep(2)
        pyautogui.click(659, 156)
        time.sleep(2)
        pyautogui.click(772, 173)
        time.sleep(2)
        pyautogui.press('esc')
    
    def decharger(self):
        time.sleep(2)
        pyautogui.click(1276, 160)
        time.sleep(2)
        pyautogui.click(1391, 177)
        time.sleep(2)
        pyautogui.press('esc')
        
    def make_decision(self):
        """
        Quelle est la position de mon cursur ?
        Quelle est la couleur sous mon curseur ?
        """
        time.sleep(2)
        x, y = pyautogui.position()
        time.sleep(1)
        loop = True
        while loop:
            try:
                print((x, y),", ", pyautogui.pixel(x, y))
                loop =  False
            except:
                pass

class Astrub(Poubelle):
    def __init__(self):
        self.maps = [
            [1068, 943], # bas 
            [1712, 370], # droite x1
            [1296, 949], # bas
            [269, 681], # gauche
            [264, 770], # gauche x1
            [257, 706], # gauche
            [887, 33], # haut x1
            [664, 37], # haut
            [1118, 36], # haut
            [980, 37], # haut
            [1638, 344], # droite
            [617, 35], # haut
            [1670, 181], # droite x1
            [1071, 943], # bas
            [1251, 948], # bas x1
            [1028, 949], # banque x2
        ]
    

    def fouiller(self):    
        if self.map[0] == 1712 and self.map[1] == 370:
            pyautogui.click(938, 300)
            time.sleep(10)
            self.charger()

        elif self.map[0] == 264 and self.map[1] == 770:
            pyautogui.click(767, 667)
            time.sleep(10)
            self.charger()
        
        elif self.map[0] == 1118 and self.map[1] == 36:
            pyautogui.click(1186, 795)
            time.sleep(10)
            self.charger()
        
        elif self.map[0] == 1670 and self.map[1] == 181:            
            pyautogui.click(1378, 846)
            time.sleep(10)
            self.charger()  

        elif self.map[0] == 1028 and self.map[1] == 949: # banque
            pyautogui.click(self.map[0], self.map[1])
            time.sleep(10)
            self.charger()
            pyautogui.click(self.map[0], self.map[1])
            time.sleep(10)
            self.charger()
            self.check_pods()
            
    def change_map(self):
        for self.map in self.maps:
            pyautogui.click(self.map[0], self.map[1])
            self.check_map(self.map)
            # time.sleep(8)
            # poubelle.make_decision()
            
            self.fouiller()

    def check_map(self, map):
            check = True
            while check:
                try:
                    poubelle.make_decision()
                    if ( 
                        (self.map[0] == 1068 and self.map[1] == 943 and pyautogui.pixel(self.map[0], self.map[1]) == (58, 46, 17)) or 
                        (self.map[0] == 1712 and self.map[1] == 370 and pyautogui.pixel(self.map[0], self.map[1]) == (77, 53, 9)) or
                        (self.map[0] == 1296 and self.map[1] == 949 and pyautogui.pixel(self.map[0], self.map[1]) == (130, 122, 86)) or
                        (self.map[0] == 269 and self.map[1] == 681 and pyautogui.pixel(self.map[0], self.map[1]) == (116, 111, 65)) or
                        (self.map[0] == 264 and self.map[1] == 770 and pyautogui.pixel(self.map[0], self.map[1]) == (81, 50, 4)) or
                        (self.map[0] == 257 and self.map[1] == 706 and pyautogui.pixel(self.map[0], self.map[1]) == (37, 37, 38)) 
                    ):
                        print("map changed")
                        check = False
                    elif (
                        (self.map[0] == 887 and self.map[1] == 33) or
                        (self.map[0] == 664 and self.map[1] == 37) or
                        (self.map[0] == 1118 and self.map[1] == 36) or
                        (self.map[0] == 980 and self.map[1] == 37) or
                        (self.map[0] == 1638 and self.map[1] == 344) or
                        (self.map[0] == 617 and self.map[1] == 35) or
                        (self.map[0] == 1670 and self.map[1] == 181) or
                        (self.map[0] == 1071 and self.map[1] == 943) or
                        (self.map[0] == 1251 and self.map[1] == 948) or
                        (self.map[0] == 1028 and self.map[1] == 949)
                    ):
                        print("color map todo")
                        check = False
                except:
                    time.sleep(1)
                    print("kéblo")
        
    def deposer_banque(self):
        pyautogui.click(1143, 344)
        pyautogui.click(1114, 449)
        pyautogui.click(905, 791)
        self.decharger()
        
if __name__ == "__main__":
    poubelle = Poubelle()
    astrub = Astrub()
    time.sleep(5)
    astrub.change_map()
    