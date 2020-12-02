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
            time.sleep(uniform(9, 10))
            loop=False
    
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

class astrub(mine):
    def __init__(self):
        self.mine_position = [10, -19]
        self.path = [
            [
                [1340, 370], # entrer dans la mine
                (153, 133, 16),
            ],
            [
                [1470, 250], # nouvelle salle
                (51, 39, 20)
            ],
            [    
                [1617, 389], # salle à droite (todo 2 cuivre)
                (22, 19, 8)
            ],
            [
                [335, 805], # retour à gauche
                (156, 116, 32)
            ],
            [
                [1043, 168], # je monte
                (85, 69, 37)
            ],  
            [
                [725, 137], # je monte
                (146, 122, 34)
            ],    
            [
                [1623, 903],# je redescent
            ],  
            [
                [597, 945], # je redescent    
            ],    
            [
                [365, 851], # retour première salle
            ],  
            [
                [300, 715], # sortir de la mine
            ],
            [
                [1457, 949], # en bas
            ],
            [
                [220, 158], # gauche
            ],
            [
                [1288, 37], # monter
            ],
            [
                [254, 304], # gauche
            ],
            [
                [1511, 955], # bas
            ],
            [
                [1511, 955], # bas
            ],   
            [
                [1648, 422], # droite (recolte) 
            ],   
            [
                [205, 494], # gauche   
            ], 
            [
                [939, 950], # bas
            ], 
            [
                [1658, 482], # droite
            ], 
            [
                [1646, 531], # droite (recolte)
            ], 
            [
                [412, 956], # bas 10 -15
            ], 
            [
                [148, 467], # gauche
            ],
            [
                [148, 467], # gauche   
            ],
            [
                [148, 467], # gauche
            ],
            [
                [148, 467], # gauche
            ],
            [
                [148, 467], # gauche
            ],
            [
                [148, 467], # gauche
            ],     
            [
                [148, 467], # gauche
            ],    
            [
                [148, 467], # gauche
            ],    
            [
                [148, 467], # gauche
            ],    
            [
                [1567, 36], # haut
            ],    
            [
                [821, 39], # haut
            ],    
            [
                [1152, 567], # entrer mine
            ],    
            [
                [1604, 295], # salle droite
            ],    
            [
                [1518, 689], # salle droite
            ],    
            [
                [380, 293], # retour gauche
            ],    
            [
                [336, 844], # retour gauche
            ],    
            [
                [261, 979], # sortie mine
            ],    
            [
                 [666, 37], # haut
            ],    
            [
                [940, 43], # haut
            ],
            [
                [940, 43], # haut
            ], 
            [
                [1025, 41], # haut
            ], 
            [
                [979, 38], # haut
            ],  
            [
                [1697, 338], # droite (1,-21)
            ],    
            [
                [1697, 338], # droite 2,-21)
            ],    
            [
                [1697, 600], # droite 3,-21)
            ],   
            [
                [1697, 600], # droite 5,-21)
            ],
            [
                [1697, 600], # droite 6,-21)
            ], 
            [
                [1697, 600], # droite 6,-21)   
            ],   
            [
                [1697, 600], # droite 7,-21) 
            ],
            [
                [1697, 600], # droite 8,-21)
            ],
            [
                [1728, 247], # droite (mine) 9,-21)
            ], 
            [
                [694, 949], # bas
            ], 
            [
                [795, 945], # bas
            ], 
            [
                [1568, 257], # droite (mine)
            ], 
            [
                 [482, 303], # descendre  
            ],     
        ]
        self.availableOre = ["Kobalte", "Bronze", "Cuivre", "Fer"] # Y'en a d'autres mais le reste faut être abonné
    
    def getAvailableOre(self):
        return self.availableOre

    def get_pos_recolt(self):
        if self.path == [1470, 250]:
            print("bingo")
    
    def miner(self):
        for room in self.path: # pour chaque pièce
            self.mouvement(room[0], room[1]) # changement de pièce
            # mine.make_decision()
            for Ore in mine.getOreList(metier_level): # pour toutes les ressouces récoltables (par ordre de niveau)
                if Ore in self.availableOre: # les récolter par priorité
                    astrub.take_resources(room[0], Ore) # clique pour récolter

    def mouvement(self, room, color):
        pyautogui.click(room) # clique pour bouger
        if room == [1340, 370]:
            wait = True
            while wait:
                try:
                    test = pyautogui.pixel(room[0], room[1])
                    print("test")
                    if test == color:
                        print("nice")
                        wait = False
                    else:
                        time.sleep(0.25)
                except:
                    print("no pain no gain")
        # else:
        #     time.sleep(uniform(8, 9)) # temps pour changer de pièce

    def take_resources(self, room, Ore):
        """
        Si click ressource correspond au bon pixel, alors time.sleep pour la récolter,
        sinon next
        """
        if Ore == "Fer":
            astrub.take_fer(room)
        
        elif Ore == "Cuivre":
            astrub.take_cuivre(room)

        elif Ore == "Bronze":
            astrub.take_bronze(room)

    def take_fer(self, room):
        """
        Si pixel pour vide alors next test
        Sinon si pixel pour recoltable alors click et time.sleep()
        Sinon (autre pixel) alors je peux next ou attendre qu'il se déplace # quelque chose bloque l'accès (attention combat ou joueur)
        S'il y a plusieurs room, c'est pcq parfois il revient sur ses pas durant sa tournée
        """
        if room == [475, 435] or room == [1568, 257]:
            mine.decision((721, 93), (187, 182, 137))
            mine.decision((752, 130), (163, 158, 118))

        elif room == [482, 303]:
            pass

        elif room == [1340, 370] or room == [365, 851]:
            mine.decision((661, 460), (63, 50, 18))
            
        elif room == [1470, 250] or room == [597, 945] or room == [335, 805]:
            mine.decision((694, 634), (80, 68, 41))

        elif room == [1617, 389]:
            pass
        elif room == [1043, 168]:
            mine.decision((775, 750), (84, 69, 32))
            mine.decision((1239, 579), (35, 28, 13))
        elif room == [300, 715]:
            pass
        elif room == [1288, 37] or room == [795, 945]:
            mine.decision((1228, 526), (110, 97, 55))
            mine.decision((1175, 560), (96, 87, 55))
            mine.decision((538, 395),(115, 113, 80))
            mine.decision((1060, 229), (86, 77, 49))
        elif room == [1763, 540]:
            pass
        elif room == [1457, 949] or room == [795, 945]:
            mine.decision((829, 143), (131, 127, 22))
        elif room == [1648, 422]:
            mine.decision((424, 328), (144, 142, 104))
            mine.decision((616, 267), (204, 198, 144))
            mine.decision((665, 294), (122, 120, 88))
            mine.decision((714, 309), (182, 179, 126))
        elif room == [1646, 531]:
            mine.decision((1296, 385), (113, 107, 86))
            mine.decision((1546, 453), (199, 190, 140))
            mine.decision((616, 444), (185, 182, 133))
            mine.decision((947, 347), (200, 192, 140))
        elif room == [1152, 567] or room == [336, 844]:
            mine.decision((392, 618), (64, 55, 27))
            mine.decision((637, 508), (33, 28, 15))
            mine.decision((683, 461), (39, 33, 18))
            mine.decision((1021, 303), (23, 20, 10))
            mine.decision((1306, 443) , (70, 57, 1))
        elif room == [1604, 295] or room == [380, 293]:
            mine.decision((506, 424), (95, 77, 37))
            mine.decision((646, 335) ,  (43, 35, 19))
            mine.decision((937, 195), (13, 10, 5))
            mine.decision((1270, 159) ,  (15, 18, 6))
            mine.decision((1421, 311), (25, 27, 4))
            mine.decision((1091, 524), (67, 56, 0))
        elif room == [1518, 689]:
            mine.decision((1009, 183), (57, 43, 11))
            mine.decision((674, 502), (12, 9, 2))

    def take_cuivre(self, room):
        print("tu ne peux pas miner le cuivre")
    
    def take_bronze(self, room):
        print("tu ne peux pas miner le bronze")

    def take_kobalte(self, room):
        print("tu ne peux pas miner le kobalte")

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
        while developing:
            mine.make_decision()

    metier_level = eval(input("Donne-moi le niveau de ton métier : "))
    aller_retour = eval(input("Donne-moi le nombre d'aller-retour à effecter : "))

    print("Retourne sur ton écran dofus")
    time.sleep(uniform(4, 6))

    mine = mine()
    astrub = astrub()

    récolter = True
    
    while récolter and aller_retour > 0:
        astrub.miner()
        aller_retour-=1
        print(aller_retour, "aller-retour restant")