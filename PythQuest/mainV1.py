from models.Combattant import Combattant
from models.Forgeron import Forgeron
from models.Medecin import Medecin
from models.Quete import Quete
from models.Donjon import Donjon
from models.Arme import Arme
from models.exceptions import (
    InsufficientFundsError,
    InventoryFullError,
    NoSuchItemError,
    QuestAlreadyAcceptedError,
    NoActiveQuestError,
)
from models.GestionnaireDeQuetes import GestionnaireDeQuetes
import random


def creerQuete(joueur: Combattant):
    for i in range(random.randint(7, 12)):
        GestionnaireDeQuetes.creerQueteDonjonMonstres(joueur.getNiveau())


def choixConsole(message):
    return input(message)


def creerPersonnage() -> "Combattant":
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
    creerQuete(joueur)

    while True:
        afficherMenuPrincipal()
        choix = choixConsole("Choix : ")

        if choix == "1":  # Faire des achats
            print("Pas encore implémenté.")

        elif choix == "2":  # Voir les quêtes
            Quete.afficherToutesLesQuetesEnCours()
            choix = choixConsole("Choix d'une quête à accepter : ")
            if choix == str(Quete.getNbQuetesEnCours() + 1):
                continue
            elif choix.isdigit() and (
                int(choix) > 0 and int(choix) <= Quete.getNbQuetesEnCours()
            ):
                try:
                    quete = Quete.getQueteIndexEnCours(int(choix) - 1)
                    joueur.accepterQuete(quete)
                    print(f"Vous avez accepté la quête {quete.getNom()}.")
                except (QuestAlreadyAcceptedError, IndexError) as e:
                    print(e)
                except ValueError:
                    print("Choix invalide. Veuillez entrer un nombre.")
            else:
                print("Choix invalide. Veuillez réessayer.")

        elif choix == "3":  # Voir les donjons
            Donjon.afficherTousLesDonjonsActifs()
            choix = choixConsole("Choix d'un donjon à explorer : ")
            if choix == str(Donjon.nbDonjons + 1):  # Retour
                continue
            elif choix.isdigit() and (  # Vérifie si le choix est un nombre et s'il est dans la plage des donjons
                int(choix) > 0 and int(choix) <= Donjon.nbDonjons
            ):
                donjon = Donjon.getDonjonIndexActif(int(choix) - 1)
                print(f"Vous entrez dans le {donjon.getNom()}.")
                while not donjon.estVide(): # Boucle d'apparition des monstres
                    monstre = donjon.getMonstreAleatoire()
                    print(f"Vous rencontrez un {monstre.getNom()} !")
                    while not joueur.estMort() and not monstre.estMort(): # Boucle de combat
                        print(f"Vous avez {joueur.getVie()} points de vie.")
                        print(
                            f"Le {monstre.getNom()} a {monstre.getVie()} points de vie."
                        )
                        choix = choixConsole(
                            "1. Attaquer\n2. Boire une potion\n3. Fuir\nChoix : "
                        )
                        if choix == "1":  # Attaquer
                            print(f"Vous attaquez {monstre.getNom()} !")
                            joueur.attaquer(monstre)
                            if not monstre.estMort():
                                print(f"{monstre.getNom()} vous attaque !")
                                monstre.attaquer(joueur)
                        elif choix == "2":  # Boire une potion
                            try:
                                joueur.boirePotion()
                                print("Vous avez bu une potion.")
                            except NoSuchItemError as e:
                                print(e)
                        elif choix == "3":  # Fuir
                            print("Vous avez fui.")
                            break
                        else:  # Choix invalide
                            print("Choix invalide. Veuillez réessayer.")
                            continue
                    if joueur.estMort():
                        joueur.resetApresMort()
                        break
                    elif monstre.estMort():
                        try:
                            joueur.battreMonstre(monstre, donjon)
                        except NoActiveQuestError:
                            pass
                    else :
                        break
                if donjon.estVide():
                    donjon.setInactif()

            else:  # Choix invalide
                print("Choix invalide. Veuillez réessayer.")

        elif choix == "4":  # Informations sur le personnage
            while True:
                print(joueur)
                afficherMenuPersonnage()
                choix = choixConsole("Choix : ")
                if choix == "1":  # Changer d'arme
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
                elif choix == "2":  # Abandonner la quête
                    try:
                        joueur.abandonnerQuete()
                        print("Vous avez abandonné la quête.")
                    except NoActiveQuestError as e:
                        print(e)
                elif choix == "3":  # Retour
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.")

        elif choix == "5":  # Quitter le jeu
            print("Merci d'avoir joué !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
