from models.Combattant import Combattant
from models.Forgeron import Forgeron
from models.Medecin import Medecin
from models.Quete import Quete
from models.Donjon import Donjon

""" 

Etapes :
1. Créer un personnage (si ce n'est pas déjà fait (lors de sauvegarde))
1.1. Demander le nom du personnage
1.2. Créer un objet Combattant avec le nom du personnage
--- Boucle principale ---
2. Afficher le menu principal
2.1. Demander le choix de l'utilisateur
(
    Choix :
    1. Faire des achats (
        1.1. Afficher le menu des achats
        1.2. Demander le choix de l'utilisateur (
            Choix :
            1. Visiter le Forgeron (
                1.1. Afficher les armes du forgeron
                1.2. Demander le choix de l'utilisateur (
                    Choix :
                    1. Acheter une arme
                    2. Retour
                )
                1.x. Vendre une arme (Plus tard)
            )
            2. Visiter le Médecin (
                2.1. Afficher les potions du médecin
                2.2. Demander le choix de l'utilisateur (
                    Choix :
                    1. Acheter une potion (si assez d'or)
                    2. Retour
                )
            )
            3. Retour
        )
    )
    2. Voir les quêtes (
        2.1. Afficher les quêtes
        2.2. Demander le choix de l'utilisateur (
            Choix :
            1. Choisir une quête en tant que principale
            2. Retour
        )
    )
    3. Voir les donjons ( /!\ POSSIBILITE DE CHANGER D'ARME A TOUT MOMENT (après combat, laisser un choix ?) /!\ 
        3.1. Afficher les donjons
        3.2. Demander le choix de l'utilisateur (
            Choix :
            1. Choisir un donjon à explorer (
                Choix :
                1. Menu des monstres (venue aléatoire ou choix ?) (
                    Implémentation du combat :
                    1. Attaquer
                    2. Utiliser une potion (si achetée)
                    3. Fuir
                )
                2. Fuire (que en combat ?)
            )
            2. Retour
        )
    )
    4. Quitter
)

"""

def initialiserInstances():
    # Création des instances des différents personnages
    forgeron = Forgeron("Forgeron")
    medecin = Medecin("Medecin")
    return forgeron, medecin

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

def main():
    print("Bienvenue dans le jeu !")
    
    # Création du personnage
    player = creerPersonnage()
    
    while True:
        afficherMenuPrincipal()
        choix = choixConsole("Choix : ")
        
        if choix == '1':
            while True:
                afficherMenuAchats()
                choixAchats = choixConsole("Choix : ")
                
                if choixAchats == '1':
                    print("Forgeron")
                elif choixAchats == '2':
                    print("Medecin")
                elif choixAchats == '3':
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.")
            
        elif choix == '2':
            toutesLesQuetes = Quete.getToutesLesQuetes()
            print(toutesLesQuetes)
            
            
        elif choix == '3':
            tousLesDonjons = Donjon.getTousLesDonjons()
            print(tousLesDonjons)
            
            
        elif choix == '4':
            print("Merci d'avoir joué !")
            break
        
        
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()