  # Projet expérimental de création de bot sur dofus

Quelques scripts pour automatiser des tâches sur le jeu dofus.

## dobot_miner.py (facilement extensible à d'autres mines)

Script qui permet de miner les minerais de la zone d'Astrub (Fer, cuivre, bronze et kobalte)
1) Vous devez être à l'entrer de "Mine Hable"
2) Il suffit de renseigner le niveau de votre métier et le nombre d'aller-retour à effectuer
3) Directement retourner sur la fenêtre dofus, le script va se lancer.

D'autres mines pourront seront peut-être développé.

module : pyautogui

TODO :
• Le passage à la banque est encore à faire
• Une version plus rapide (et donc plus intelligente) en évitantles time.sleep()
• Gestion des combats