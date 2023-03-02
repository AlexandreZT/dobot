import pyautogui
import time
from random import randint, uniform


class Foret(object):
    def __init__(self):
        pass

    def getcouperPosition(self):
        return self.couper_position

    def getWoodList(self, level):
        # Les couperrais doivent être trié par ordre de prix décroissant
        if level == 200:
            WoodList = ["Tremble"]

        elif level >= 180:
            WoodList = []

        elif level >= 160:
            WoodList = []

        elif level >= 140:
            WoodList = []

        elif level >= 120:
            WoodList = []

        elif level >= 100:
            WoodList = []

        elif level >= 80:
            WoodList = []

        elif level >= 60:
            WoodList = []

        elif level >= 40:
            WoodList = []

        elif level >= 20:
            WoodList = []
        else:
            WoodList = []

        return WoodList

    def couper(self):
        print("Je ne connais pas encore cette forêt")

    def can_recolt(self):  # peut-être résolvable avec un time.sleep()
        force = True
        while force:
            try:
                x, y = pyautogui.position()
                color = pyautogui.pixel(x, y)
                force = False
            except:
                pass
        return color

    def dev_can_recolt(self):  # peut-être résolvable avec un time.sleep()
        force = True
        while force:
            try:
                x, y = pyautogui.position()
                print(pyautogui.pixel(x, y))
                force = False
            except:
                pass

    def decision(self, pos, empty_color):
        pyautogui.click(pos[0], pos[1])
        # couper.make_decision() # Sert à vérifier le code couleur de la ressource
        if empty_color != foret.can_recolt():
            time.sleep(
                uniform(9, 10)
            )  # temps pour déplacement et recolte # breakpoint permet aussi de voir où ça bug
            loop = False

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
                print((x, y), ", ", pyautogui.pixel(x, y))
                loop = False
            except:
                pass


class Frigost(Foret):
    def __init__(self):
        self.couper_position = [10, -19]
        self.path = [
            [221, 585],  # entrer de la fôret (1er arbre)
            [1097, 37],  # monte
            [1097, 37],  # monte
            [928, 33],  #  monte-tremble
            [147, 435],  # gauche
            [117, 460],  # gauche  # gauche-tremble
        ]
        self.availableWood = [
            "Tremble"
        ]  # Y'en a d'autres mais le reste faut être abonné

    def getAvailableWood(self):
        return self.availableWood

    def get_pos_recolt(self):
        if self.path == [1470, 250]:
            print("bingo")

    def couper(self):
        for room in self.path:  # pour chaque pièce
            self.mouvement(room)  # changement de pièce
            # couper.make_decision() # Sert pour recupérer des infos pour vérifier si la pièce à changé
            for Wood in foret.getWoodList(
                metier_level
            ):  # pour toutes les ressouces récoltables (par ordre de niveau)
                if Wood in self.availableWood:  # les récolter par priorité
                    frigost.take_resources(room, Wood)  # clique pour récolter
                    # if combat.check_aggression() == True:
                    #     combat.fight()

            if room == [261, 979]:
                frigost.check_pods()

    def mouvement(self, room):
        pyautogui.click(room)  # clique pour bouger
        # if room == [1340, 370]:
        #     wait = True
        #     while wait:
        #         try:
        #             if pyautogui.pixel(room[0], room[1]) == (153, 133, 16):
        #                 print("nice")
        #                 wait = False
        #             else:
        #                 time.sleep(0.25)
        #         except:
        #             print("no painno gain")
        # else:
        time.sleep(uniform(8, 9))  # temps pour changer de pièce

    # def check_pods(self):
    #     pyautogui.click(1224, 1071)
    #     check = True
    #     while check:
    #         try:
    #             if pyautogui.pixel(1224, 1071) == (96, 190, 53):
    #                 self.go_bank()
    #             check = False
    #         except:
    #             pass

    # def go_bank(self):
    #     print("ressources déposé")
    #     self.back_couper_hable()

    # def back_couper_hable(self):
    #     print("me revoilà")

    def take_resources(self, room, Wood):
        """
        Si click ressource correspond au bon pixel, alors time.sleep pour la récolter,
        sinon next
        """
        if Wood == "Tremble":
            frigost.take_tremble(room)

    def take_tremble(self, room):
        """
        Si pixel pour vide alors next test
        Sinon si pixel pour recoltable alors click et time.sleep()
        Sinon (autre pixel) alors je peux next ou attendre qu'il se déplace # quelque chose bloque l'accès (attention combat ou joueur)
        S'il y a plusieurs room, c'est pcq parfois il revient sur ses pas durant sa tournée
        """
        if room == [221, 585]:
            foret.decision((1304, 581), (217, 233, 239))

        elif room == [928, 33]:
            foret.decision((1390, 162), (121, 144, 144))

        elif room == [117, 460]:
            foret.decision((442, 839), (134, 134, 134))


if __name__ == "__main__":
    developing = False
    if developing == True:
        foret = Foret()
        # combat = combat()
        while developing:
            # écran dofus : (300, 30) sur (1620, 965)
            # dimension des cases (+45, +20)
            # pyautogui.click(345, 50)  # milieu première case
            #
            # pyautogui.click(390, 70)  # 390, 70 # milieu diagonal (+45, +20)
            foret.make_decision()

    metier_level = eval(input("Donne-moi le niveau de ton métier : "))
    aller_retour = eval(input("Donne-moi le nombre d'aller-retour à effecter : "))

    print("Retourne sur ton écran dofus")
    time.sleep(uniform(4, 6))

    foret = Foret()
    frigost = Frigost()

    récolter = True

    while récolter and aller_retour > 0:
        frigost.couper()
        aller_retour -= 1
        print(aller_retour, "aller-retour restant")

#                       (936, 187)
#           (891, 209)              (981, 208)
#                       (938, 231)


# x : 936 et 938 (187 | 231) => env 44
# y : 208 et 209 (891 <-> 981) => env 90


# dernière pos (1620, 965)
