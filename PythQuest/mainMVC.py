from controller.Controller import Controller

""" 
A FAIRE :

Création de quete selon un monstre et donjon déjà créé
Création de quete après finir une quête
Gérer si un monstre de quete est mort sans choisir la quête associée
Ajouter recompense exp si pas déjà fait
Vérifier si l'exp gagnée est cohérente avec le niveau des monstres/de la quete
"""

def main():
    game_controller = Controller()
    game_controller.afficherMenuPrincipal()

if __name__ == "__main__":
    main()