import pyautogui
import time
from random import randint, uniform
class combat(object):
    """
    Le script doit être au moins capable de gérer les combats contre les protecteurs de ressources.
    Pour détecter s'il est en combat, il se réfère au pixel de couleur du mode combat.
    """
    def find_enemies(self):
        """
        Parcours toutes les cases du jeu à la recherche de : (46, 54, 61) => couleur ennemie en mode créature
        """
        for y in range (50, 965, 45):
            for x in range (345, 1530, 91): 
                test = True
                while test:
                    try:
                        pyautogui.click(x+45, y-22)
                        color = pyautogui.pixel(x+45, y-22)
                        test = False
                    except:
                        pass
                if color == (46, 54, 61):
                    print("got ya")
                    return x+45, y-22
            for x in range (345, 1530, 91):
                test = True
                while test:
                    try:
                        pyautogui.click(x, y)
                        color = pyautogui.pixel(x, y)
                        test = False
                    except:
                        pass
                if color == (46, 54, 61):
                    print("got ya")
                    return x, y
    
    def attack(self, x, y):
        pass

    def check_aggression(self):
        for x in range (384, 1920, 384):
            for y in range(270, 1080, 270):
                test = True
                while test:
                    try:
                        battle_color = pyautogui.pixel(x, y)
                        print(battle_color)
                        if ( # le mode cellule n'a pas toujours lemême code couleur, à compléter si de nouveaux trouvé
                            battle_color == (199, 197, 102) or battle_color == (185, 183, 89) or 
                            battle_color ==  (138, 93, 40) or battle_color == (148, 103, 50) or
                            battle_color == (154, 144, 85) or battle_color == (164, 154, 94) or
                            battle_color == (167, 160, 137) or battle_color == (158, 150, 127)     
                        ):
                            # ou couleur case rouge ou bleu ou cas où
                            return True
                        else:
                            print("rien détecté")
                        test=False
                    except Exception as e:
                        print(e)
        return False
    
    def fight(self):
        """
        Vous devez activer les raccourcis US
        """
        pyautogui.press('f1') # raccourci prêt 
        in_fight = True
        while in_fight:
            # if couleur c'est mon tour alors fight sinon tu fais rien
            try:
                color = pyautogui.pixel(874, 1063)
                if color == (252, 200, 0) or color == (255, 91, 61): # orange / rouge
                    # time.sleep(1)
                    # pyautogui.press('num1') # spell num1 to num0 then ctrl+num1 to ctrl+num0
                    # time.sleep(1)
                    # pyautogui.click(1818, 111)
                    time.sleep(1)
                    pyautogui.press('num1')
                    time.sleep(1)
                    pyautogui.click(1753, 108)
                    # x1
                    time.sleep(1)
                    pyautogui.press('num1')
                    time.sleep(1)
                    pyautogui.click(1753, 108)
                    # x2
                    time.sleep(1)
                    pyautogui.press('num1')
                    time.sleep(1)
                    pyautogui.click(1753, 108)
                    # x3
                    time.sleep(1)
                    pyautogui.click(874, 1063)
                    time.sleep(1)
                    combat.check_aggression()
                    time.sleep(5)
                if combat.check_aggression() == True:
                    pyautogui.press('f1')
                else:
                    in_fight = False
            except Exception as e:
                print(e)
class mine(object):
    def __init__(self):
        pass

    def getMinePosition(self):
        return self.mine_position

    def getOreList(self, level):
        # Les minerais doivent être trié par ordre de prix décroissant
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

    def decision(self, pos, empty_color):
        pyautogui.click(pos[0], pos[1])
        # mine.make_decision() # Sert à vérifier le code couleur de la ressource
        if empty_color != mine.can_recolt():
            time.sleep(uniform(9, 10)) # temps pour déplacement et recolte # breakpoint permet aussi de voir où ça bug
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
class astrub(mine):
    def __init__(self):
        self.mine_position = [10, -19]
        self.path = [
            [1340, 370], # entrer dans la mine
            [1470, 250], # nouvelle salle
            [1617, 389], # salle à droite
            [335, 805], # retour à gauche
            [1043, 168], # je monte
            [725, 137], # je monte
            [1623, 903],# je redescent
            [597, 945], # je redescent
            [365, 851], # retour première salle
            [300, 715], # sortir de la mine
            [1457, 949], # en bas
            [220, 158], # gauche
            [1288, 37], # monter
            [254, 304], # gauche
            [1511, 955], # bas
            [1511, 955], # bas
            [1648, 422], # droite (recolte) 
            [205, 494], # gauche    
            [939, 950], # bas
            [1658, 482], # droite
            [1646, 531], # droite (recolte)
            [412, 956], # bas 10 -15
            [148, 467], # gauche
            [148, 467], # gauche    
            [148, 467], # gauche
            [148, 467], # gauche
            [148, 467], # gauche
            [148, 467], # gauche
            [148, 467], # gauche
            [148, 467], # gauche
            [148, 467], # gauche
            [1567, 36], # haut
            [821, 39], # haut
            [1152, 567], # entrer mine
            [1604, 295], # salle droite
            [1518, 689], # salle droite
            [380, 293], # retour gauche
            [336, 844], # retour gauche
            [261, 979], # sortie mine
            [666, 37], # haut
            [940, 43], # haut
            [1025, 41], # haut
            [979, 38], # haut
            [1697, 338], # droite (1,-21)
            [1697, 338], # droite 2,-21)
            [1697, 600], # droite 3,-21)
            [1697, 600], # droite 4,-21)
            [1697, 600], # droite 5,-21)
            [1697, 600], # droite 6,-21)    
            [1697, 600], # droite 7,-21)
            [1728, 247], # droite (mine) 8,-21)
            [694, 949], # bas
            [795, 945], # bas
            [1568, 257], # droite (mine)
            [482, 303], # descendre           
        ]
        self.availableOre = ["Kobalte", "Bronze", "Cuivre", "Fer"] # Y'en a d'autres mais le reste faut être abonné
    
    def getAvailableOre(self):
        return self.availableOre

    def get_pos_recolt(self):
        if self.path == [1470, 250]:
            print("bingo")
    
    def miner(self):
        for room in self.path: # pour chaque pièce
            self.mouvement(room) # changement de pièce
            # mine.make_decision() # Sert pour recupérer des infos pour vérifier si la pièce à changé
            for Ore in mine.getOreList(metier_level): # pour toutes les ressouces récoltables (par ordre de niveau)
                if Ore in self.availableOre: # les récolter par priorité
                    astrub.take_resources(room, Ore) # clique pour récolter
                    if combat.check_aggression() == True:
                        combat.fight()
                    
            if room == [261, 979]:
                astrub.check_pods()

    def mouvement(self, room):
        pyautogui.click(room) # clique pour bouger
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
        time.sleep(uniform(8, 9)) # temps pour changer de pièce

    def check_pods(self):
        pyautogui.click(1224, 1071)
        check = True
        while check:
            try:
                if pyautogui.pixel(1224, 1071) == (96, 190, 53):
                    self.go_bank()
                check = False
            except:
                pass

    def go_bank(self):
        print("ressources déposé")
        self.back_mine_hable()

    def back_mine_hable(self):
        print("me revoilà")

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
        if room == [1568, 257]:
            mine.decision((721, 93), (187, 182, 137))
            mine.decision((752, 130), (163, 158, 118))

        elif room == [1340, 370] or room == [365, 851]:
            mine.decision((661, 460), (63, 50, 18))
            
        elif room == [1470, 250] or room == [597, 945] or room == [335, 805]:
            mine.decision((694, 634), (80, 68, 41))

        elif room == [1617, 389]:
            pass

        elif room == [1043, 168] or room == [1623, 903]:
            mine.decision((763, 754), (157, 134, 63))
            mine.decision((1233, 591), (34, 26, 11))

        elif room == [300, 715]:
            pass

        elif room == [1288, 37] or room == [795, 945]:
            mine.decision((1228, 526), (110, 97, 55))
            mine.decision((1175, 560), (96, 87, 55))
            mine.decision((538, 395),(115, 113, 80))
            mine.decision((1060, 229), (86, 77, 49))
            mine.decision((1108, 188), (72, 73, 55))

        elif room == [1763, 540]:
            pass

        elif room == [1457, 949] or room == [795, 945]:
            mine.decision((829, 143), (131, 127, 22))

        elif room == [1648, 422]:
            mine.decision((424, 328), (144, 142, 104))
            mine.decision((616, 267), (204, 198, 144))
            mine.decision((665, 294), (122, 120, 88))
            mine.decision((714, 309), (182, 179, 126))
            mine.decision((731, 574), (114, 110, 86))

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
            mine.decision((646, 335), (43, 35, 19))
            mine.decision((925, 145), (10, 8, 4)) # refait
            mine.decision((1167, 237), (40, 33, 0)) # refait
            mine.decision((1270, 159), (15, 18, 6))
            mine.decision((1421, 311), (25, 27, 4))
            mine.decision((1091, 524), (67, 56, 0))

        elif room == [1518, 689]:
            mine.decision((1009, 183), (57, 43, 11))
            mine.decision((674, 502), (12, 9, 2)) 
            mine.decision((919, 450), (102, 96, 4))
            
    def take_cuivre(self, room):
        if room == [1340, 370] or room == [365, 851]:
            mine.decision((340, 543), (151, 122, 39))
            mine.decision((608, 474), (72, 57, 20))

        elif room == [1470, 250] or room == [597, 945] or room == [335, 805]:
            mine.decision((800, 602), (63, 52, 24))

        elif room == [1617, 389]:
            mine.decision((926, 155), (88, 66, 20))
            mine.decision((866, 133), (95, 78, 38))

        elif room == [1043, 168] or room == [1623, 903]:
            mine.decision((1163, 297), (68, 58, 30))
            mine.decision((1171, 596), (33, 26, 12))

        elif room == [725, 137]:
            mine.decision((1028, 337), (157, 136, 70))
            mine.decision((1080, 351), (147, 128, 64))
            
        elif room == [300, 715] or room == [482, 303]:
            mine.decision((633, 499), (158, 149, 111))
            mine.decision((672, 512), (159, 153, 115))

        elif room == [1288, 37] or room == [795, 945]:
            mine.decision((596, 374), (124, 124, 90))
            mine.decision((1161, 178), (85, 85, 63))

        elif room == [1648, 422]:
            mine.decision((519, 278), (136, 134, 98))
            mine.decision((757, 342), (191, 182, 132))

        elif room == [1646, 531]:
            mine.decision((1499, 433), (198, 189, 141))
        
        elif room == [1152, 567] or room == [336, 844]:
            mine.decision((479, 646), (42, 34, 17))
            mine.decision((978, 362), (35, 30, 14))

        elif room == [1604, 295] or room == [380, 293]:
            mine.decision((464, 409), (90, 71, 36))

        elif room == [1518, 689]:
            mine.decision((1047, 260), (44, 35, 14))
            mine.decision((1291, 384), (45, 35, 11))

        elif room == [1728, 247]:
            mine.decision((1407, 420) ,  (87, 86, 63))
            mine.decision((1142, 284), (80, 76, 58))
            mine.decision((1092, 308), (80, 75, 59))
            
    def take_bronze(self, room):
        if room == [1340, 370] or room == [365, 851]:
            mine.decision((1483, 662), (50, 40, 17))

        elif room == [1470, 250] or room == [597, 945] or room == [335, 805]:
            mine.decision((618, 353), (92, 83, 40))
            mine.decision((673, 326), (79, 60, 17))

        elif room == [1288, 37] or room == [795, 945]:
            mine.decision((998, 234), (87, 86, 68))

        elif room == [1648, 422]:
            mine.decision((1063, 756), (160, 156, 122))
            mine.decision((1108, 776), (168, 164, 121))

        elif room == [1646, 531]:
            mine.decision((1085, 571), (191, 182, 140))

        elif room == [1152, 567] or room == [336, 844]:
            mine.decision((1127, 231), (22, 18, 9))

        elif room == [1604, 295] or room == [380, 293]:
            mine.decision((607, 403), (63, 48, 26))
            mine.decision((1161, 495), (31, 28, 0))

        elif room == [1728, 247]:
            mine.decision((646, 417), (113, 110, 78))
            mine.decision((682, 398), (120, 118, 85))
            mine.decision((731, 364), (110, 107, 76))

        elif room == [1568, 257]:
            mine.decision((819, 127), (173, 164, 123))
            mine.decision((862, 147), (148, 140, 104)) 
            mine.decision((905, 165), (165, 157, 115))

    def take_kobalte(self, room):
        if room == [300, 715] or room == [482, 303]:
            mine.decision((875, 401) ,  (60, 62, 46))

        elif room == [1648, 422]:
            mine.decision((1404, 803), (92, 90, 69))

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
        combat = combat()        
        while developing:
            x, y = combat.find_enemies()
            combat.attack(x, y)
            # écran dofus : (300, 30) sur (1620, 965)
            # dimension des cases (+45, +20)
            # pyautogui.click(345, 50)  # milieu première case
            #                   
            # pyautogui.click(390, 70)  # 390, 70 # milieu diagonal (+45, +20)
            # mine.make_decision()
            # if combat.check_aggression() == True:
            #     combat.fight()

    metier_level = eval(input("Donne-moi le niveau de ton métier : "))
    aller_retour = eval(input("Donne-moi le nombre d'aller-retour à effecter : "))

    print("Retourne sur ton écran dofus")
    time.sleep(uniform(4, 6))

    mine = mine()
    astrub = astrub()
    combat = combat() 

    récolter = True
    
    while récolter and aller_retour > 0:
        astrub.miner()
        aller_retour-=1
        print(aller_retour, "aller-retour restant")

#                       (936, 187)
#           (891, 209)              (981, 208)
#                       (938, 231)


# x : 936 et 938 (187 | 231) => env 44
# y : 208 et 209 (891 <-> 981) => env 90


# dernière pos (1620, 965)