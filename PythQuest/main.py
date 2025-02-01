from models.Combattant import Combattant
from models.Forgeron import Forgeron
from models.Medecin import Medecin
from models.Quete import Quete
from models.Donjon import Donjon
from models.exceptions import InsufficientFundsError, InventoryFullError, NoSuchItemError, QuestAlreadyAcceptedError, NoActiveQuestError
from models.GestionnaireDeQuetes import GestionnaireDeQuetes
import random

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
    forgeron = Forgeron("Robert")
    medecin = Medecin("Jean")
    return forgeron, medecin

def creerQuete():
    for i in range(random.randint(3, 5)):
        GestionnaireDeQuetes.creerQueteDonjonMonstres()
    

def choixConsole(message):
    return input(message)

def creerPersonnage():
    nomPersonnage = choixConsole("Entrez le nom de votre personnage : ")
    return Combattant(nomPersonnage, 100)

def afficherMenuPrincipal():
    print("Que voulez-vous faire ?")
    print("1. Faire des achats")
    print("2. Voir les quêtes")
    print("3. Voir les donjons")
    print("4. Informations sur le personnage")
    print("5. Quitter le jeu")

def afficherMenuAchats():
    print("Où voulez-vous aller ?")
    print("1. Visiter le Forgeron")
    print("2. Visiter le Médecin")
    print("3. Retour")
    
def afficherMenuPersonnage():
    print("Que voulez-vous faire ?")
    print("1. Changer d'arme")
    print("2. Abandonner la quête")
    print("3. Retour")

def main():
    print("Bienvenue dans le jeu !")

    # Création du personnage
    joueur = creerPersonnage()
    forgeron, medecin = initialiserInstances()

    while True:
        afficherMenuPrincipal()
        choix = choixConsole("Choix : ")

        if choix == "1":
            print("Vous arrivez dans la boutique.")
            while True:
                afficherMenuAchats()
                choixAchats = choixConsole("Choix : ")

                if choixAchats == "1":
                    print("Vous arrivez chez le forgeron.")
                    forgeron.afficherInventaire()
                    choix = choixConsole("Choix : ")
                    if choix == str(forgeron.getNbArmes() + 1):
                        break
                    elif choix.isdigit() and (int(choix) > 0 and int(choix) <= forgeron.getNbArmes()):
                        try:
                            arme = forgeron.getArmeIndex(int(choix) - 1)
                            joueur.acheterArme(forgeron, arme)
                            print(f"Vous avez acheté l'arme {arme.getNom()} pour {arme.getValeurOr()} or.")
                        except (InsufficientFundsError, NoSuchItemError) as e:
                            print(e)
                        except ValueError:
                            print("Choix invalide. Veuillez entrer un nombre.")
                    else:
                        print("Choix invalide.")
                            
                elif choixAchats == "2":
                    print("Vous arrivez chez", medecin)
                    medecin.afficherStockPotions()
                    choix = choixConsole("Choix : ")
                    if choix == 0:
                        break
                    elif choix.isdigit() and (int(choix) > 0 and int(choix) <= medecin.getStockPotions()):
                        for i in range(int(choix)):
                            nbAchetes = int(choix)
                            try:
                                joueur.acheterPotion(medecin)
                            except (InsufficientFundsError, NoSuchItemError, InventoryFullError) as e:
                                nbAchetes -= 1
                        print(f"Vous avez acheté {nbAchetes} potions.")
                        if nbAchetes != int(choix):
                            print(f"Vous n'avez pas pu acheter {int(choix)-nbAchetes} potion(s).")
                    else:
                        print("Choix invalide.")
                    
                elif choixAchats == "3":
                    print("Vous quittez la boutique.")
                    break
                
                else:
                    print("Choix invalide. Veuillez réessayer.")

        elif choix == "2":
            toutesLesQuetes = Quete.getToutesLesQuetes()
            print(toutesLesQuetes)

        elif choix == "3":
            tousLesDonjons = Donjon.getTousLesDonjons()
            print(tousLesDonjons)

        elif choix == "4":
            while True:
                print(joueur)
                afficherMenuPersonnage()
                choix = choixConsole("Choix : ")
                if choix == "1":
                    joueur.afficherArmes()
                    choix = choixConsole("Choix d'arme à porter : ")
                    if choix == str(joueur.getNbArmesInventaire() + 1):
                        break
                    else:
                        try:
                            arme = joueur.getArmeIndexInventaire(int(choix) - 1)
                            joueur.equiperArme(arme)
                            print(f"Vous avez équipé l'arme {arme.getNom()}.")
                        except (NoSuchItemError, IndexError) as e:
                            print(e)
                        except ValueError:
                            print("Choix invalide. Veuillez entrer un nombre.")
                elif choix == "2":
                    try:
                        joueur.abandonnerQuete()
                        print("Vous avez abandonné la quête.")
                    except NoActiveQuestError as e:
                        print(e)
                elif choix == "3":
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.")
            
        elif choix == "5":
            print("Merci d'avoir joué !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()