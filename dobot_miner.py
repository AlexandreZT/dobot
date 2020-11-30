import pyautogui
import time
from random import randint, uniform

class mine(object):
    def __init__(self):
        pass

    def getMinePosition(self):
        return self.mine_position

    def getOreList(self, level):
        if level ==200:
            OreList=["Écume de mer", "Obsidienne", "Dolomite", "Or", "Bauxite", "Argent", "Silicate", "Etain", "Manganèse", "Kobalte", "Bronze", "Cuivre", "Fer"]

        elif level >=180:
            OreList=["Dolomite", "Or", "Bauxite", "Argent", "Silicate", "Etain", "Manganèse", "Kobalte", "Bronze", "Cuivre", "Fer"]

        elif level >=160:
            OreList=["Or", "Bauxite", "Argent", "Silicate", "Etain", "Manganèse", "Kobalte", "Bronze", "Cuivre", "Fer"]
        
        elif level >=140:
            OreList=["Bauxite", "Argent", "Silicate", "Etain", "Manganèse", "Kobalte", "Bronze", "Cuivre", "Fer"]
                 
        elif level >=120:
            OreList=["Argent", "Silicate", "Etain", "Manganèse", "Kobalte", "Bronze", "Cuivre", "Fer"]
                    
        elif level >=100:
            OreList=["Silicate", "Etain", "Manganèse", "Kobalte", "Bronze", "Cuivre", "Fer"]
        
        elif level >=80:
            OreList=["Manganèse", "Kobalte", "Bronze", "Cuivre", "Fer"]
        
        elif level >=60:
            OreList=["Kobalte", "Bronze", "Cuivre", "Fer"]
        
        elif level >=40:
            OreList=["Bronze", "Cuivre", "Fer"]
        
        elif level >=20:
            OreList=["Cuivre", "Fer"]
        else:
            OreList=["Fer"]
        
        return OreList
    
    def miner(self):
        print("Je ne connais pas encore cette mine")

    def can_recolt(self): # peut-être résolvable avec un time.sleep()
        fuck = True
        while fuck:
            try:
                x, y = pyautogui.position()
                color = pyautogui.pixel(x, y)
                fuck = False
            except:
                pass
        return color
    
    def dev_can_recolt(self): # peut-être résolvable avec un time.sleep()
        fuck = True
        while fuck:
            try:
                x, y = pyautogui.position()
                print(pyautogui.pixel(x, y))
                fuck = False
            except:
                pass
    
    def bank(self):
        pass

    def changer_mine(self):
        pass

    def decision(self, pos, empty_color):
        pyautogui.click(pos[0], pos[1])
        if empty_color != mine.can_recolt():
            time.sleep(uniform(8, 9))
            loop=False
    
    def make_decision(self):
        """
        Quelle est la position de mon cursur ?
        Quelle est la couleur sous mon curseur ?
        """
        time.sleep(2)
        x, y = pyautogui.position()
        time.sleep(1)
        while True:
            try:
                print((x, y),", ", pyautogui.pixel(x, y))
                exit(0)
            except:
                pass

class astrub_centre_ville(mine):
    def __init__(self):
        self.mine_position = [1, -17]
        self.path = [
            
        ]

class astrub_souterrains_profonds(mine):
    def __init__(self):
        self.mine_position = [5, -17]
        self.path = [
            
        ]

class astrub_mine_hable(mine):
    def __init__(self):
        self.mine_position = [10, -19]
        self.path = [
            [475, 435], # monter
            [482, 303], # descendre
            [1340, 370], # entrer dans la mine
            [1470, 250], # nouvelle salle
            [1617, 389], # salle à droite (todo 2 cuivre)
            [335, 805], # retour à gauche
            [1043, 168], # je monte
            [725, 137], # je monte
            [1623, 903],# je redescent
            [597, 945], # je redescent
            [365, 851], # retour première salle
            [300, 715], # sortir de la mine
            [265, 635], # voir à gauche
            [1763, 540], # revenir à droite
        ]
        self.availableOre = ["Cuivre", "Fer"] # etc. Y'en a d'autres
    
    def getAvailableOre(self):
        return self.availableOre

    def get_pos_recolt(self):
        if self.path == [1470, 250]:
            print("bingo")
    
    def miner(self):
        for room in self.path: # pour chaque pièce
            pyautogui.click(room) # changement de pièce
            time.sleep(uniform(7, 8)) # temps pour changer de pièce
            for Ore in mine.getOreList(metier_level): # pour toutes les ressouces récoltables (par ordre de niveau)
                if Ore in self.availableOre: # les récolter par priorité
                    astrub_mine_hable.take_resources(room, Ore) # clique pour récolter

    def take_resources(self, room, Ore):
        """
        Si click ressource correspond au bon pixel, alors time.sleep pour la récolter,
        sinon next
        """
        if Ore == "Fer":
            astrub_mine_hable.take_fer(room)
        
        elif Ore == "Cuivre":
            astrub_mine_hable.take_cuivre(room)

        elif Ore == "Bronze":
            astrub_mine_hable.take_bronze(room)

    def take_fer(self, room):
        """
        Si pixel pour vide alors next test
        Sinon si pixel pour recoltable alors click et time.sleep()
        Sinon (autre pixel) alors je peux next ou attendre qu'il se déplace # quelque chose bloque l'accès (attention combat ou joueur)
        S'il y a plusieurs room, c'est pcq parfois il revient sur ses pas durant sa tournée
        """
        if room == [475, 435]:
            mine.decision((721, 93), (187, 182, 137))
            mine.decision((752, 130), (163, 158, 118))

        elif room == [482, 303]:
            pass

        elif room == [1340, 370] or room == [365, 851]:
            mine.decision((661, 460), (63, 50, 18))
            
        elif room == [1470, 250] or room == [597, 945] or room == [335, 805]:
            mine.decision((694, 634), (80, 68, 41))

        elif room == [1617, 389]: # salle à droite (todo 2 cuivre)
            pass
        elif room == [1043, 168]: # je monte
            mine.decision((775, 750), (84, 69, 32))
            mine.decision((1239, 579), (35, 28, 13))
        elif room == [300, 715]:
            pass
        elif room == [265, 635]:
            mine.decision((1228, 526), (110, 97, 55))
            mine.decision((1175, 560), (96, 87, 55))
            mine.decision((538, 395),(115, 113, 80))
            mine.decision((1060, 229), (86, 77, 49))
            pyautogui.click(1106, 207) # end
        elif room == [1763, 540]:
            pass

    def take_cuivre(self, room):
        print("tu ne peux pas miner le cuivre")
    
    def take_bronze(self, room):
        print("tu ne peux pas miner le bronze")

class combat(object):
    """
    Le script doit être capable de gérer les combats contre les épouvantails.
    Pour détecter s'il est en combat, il se réfère au pixel de couleur du mode combat.
    Fait un test en ligne à partir du milieu de la carte (en diagonal)
        ex : 500, 500 et 505, 500, et 510, 500, etc.
    Si plusieurs d'entre eux sont bien la couleur recherché, alors on est bien en combat
    """
    def __init__(self):
        pass

class attrapé(object):
    """
    Mode solo doit être activé => contre le dérangement échange/défis etc.
    Le script doit être capable de réagir s'il se fait attraper par un modérateur
    Ainsi il comprend qu'il ne peut plus continuer ses tâches
    Pour détecter s'il n'est pas à sa place, 
    il va avoir un point de repère sur chacune des cartes pour déterminer s'il est sur la bonne map
    """
    pass  

if __name__ == "__main__":
    developing = False
    if developing == True:
        mine = mine()
        mine.make_decision()

    metier_level = eval(input("Donne-moi le niveau de ton métier : "))
    aller_retour = eval(input("Donne-moi le nombre d'aller-retour à effecter : "))

    print("Retourne sur ton écran dofus")
    time.sleep(uniform(4, 6))

    mine = mine()
    astrub_mine_hable = astrub_mine_hable()

    récolter = True
    
    while récolter and aller_retour > 0:
        astrub_mine_hable.miner()
        aller_retour-=1