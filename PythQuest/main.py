from models.Combattant import Combattant
from models.Forgeron import Forgeron
from models.Medecin import Medecin

def choixConsole(message):
    return input(message)

def creerPersonnage():
    nomPersonnage = choixConsole("Entrez le nom de votre personnage : ")
    return Combattant(nomPersonnage)

def afficherMenuPrincipal():
    print("\nQue voulez-vous faire ?")
    print("1. Faire des achats")
    print("2. Voir les quêtes")
    print("3. Voir les donjons")
    print("4. Quitter")

def afficherMenuAchats():
    print("\nOù voulez-vous aller ?")
    print("1. Visiter le Forgeron")
    print("2. Visiter le Médecin")
    print("3. Retour")

def gererAchats(player):
    while True:
        afficherMenuAchats()
        choixAchat = input("Entrez votre choix (1-3) : ")
        
        if choixAchat == '1':
            forgeron = Forgeron("Forgeron")
            print(f"\nBienvenue chez le {forgeron.nom}. Voici vos armes :")
            for arme in forgeron.getInventaireArmes():
                print(arme)
        elif choixAchat == '2':
            medecin = Medecin("Médecin")
            print(f"\nBienvenue chez le {medecin.nom}. Vous pouvez acheter des potions pour {medecin.getPrixPotion()} pièces d'or.")
        elif choixAchat == '3':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def main():
    print("Bienvenue dans le jeu !")
    
    # Création du personnage
    player = creerPersonnage()
    
    while True:
        afficherMenuPrincipal()
        choix = input("Entrez votre choix (1-4) : ")
        
        if choix == '1':
            gererAchats(player)
        elif choix == '2':
            print("\nVoici vos quêtes :")
            # Logique pour afficher les quêtes peut être ajoutée ici
        elif choix == '3':
            print("\nVoici les donjons :")
            # Logique pour afficher les donjons peut être ajoutée ici
        elif choix == '4':
            print("Merci d'avoir joué !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()