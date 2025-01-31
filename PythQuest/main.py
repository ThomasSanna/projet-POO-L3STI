from models.Combattant import Combattant
from models.Forgeron import Forgeron
from models.Donjon import Donjon
from models.GestionnaireDeQuetes import GestionnaireDeQuetes
from models.Monstre import Monstre

while True:
    print("1. Créer un personnage")
    print("2. Créer un forgeron")
    print("3. Créer un donjon")
    print("4. Créer un gestionnaire de quêtes")
    print("5. Quitter")
    choix = input("Choix: ")
    
    if choix == "1":
        nom = input("Nom du personnage: ")
        personnage = Combattant(nom)
        print(personnage)
    elif choix == "2":
        nom = input("Nom du forgeron: ")
        forgeron = Forgeron(nom)
        print(forgeron)
    elif choix == "3":
        nom = input("Nom du donjon: ")
        difficulte = input("Difficulté du donjon: ")
        monstre = Monstre("Monstre", 100, 10)
        donjon = Donjon(nom, difficulte, monstre)
        print(donjon)
    elif choix == "4":
        gestionnaire = GestionnaireDeQuetes()
        print(gestionnaire)
    elif choix == "5":
        break
    else:
        print("Choix invalide")