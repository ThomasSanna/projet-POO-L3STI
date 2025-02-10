from models.Combattant import Combattant
from models.Forgeron import Forgeron
from models.Medecin import Medecin
from models.Quete import Quete
from models.Donjon import Donjon
from models.GestionnaireDeQuetes import GestionnaireDeQuetes
from models.exceptions import InsufficientFundsError, InventoryFullError, NoSuchItemError, QuestAlreadyAcceptedError, NoActiveQuestError
from view.View import View
import random

class Controller:
    def __init__(self):
        self.view = View()
        self.joueur = self.creerPersonnage()
        self.forgeron, self.medecin = self.initialiserInstances()
        self.creerQuete(self.joueur)

    def initialiserInstances(self):
        forgeron = Forgeron("Robert")
        medecin = Medecin("Jean")
        return forgeron, medecin

    def creerQuete(self, joueur: Combattant):
        for i in range(random.randint(3, 5)):
            GestionnaireDeQuetes.creerQueteDonjonMonstres(joueur.getNiveau())

    def creerPersonnage(self) -> Combattant:
        nomPersonnage = self.view.choixConsole("Entrez le nom de votre personnage : ")
        return Combattant(nomPersonnage, 100)

    def afficherMenuPrincipal(self):
        while True:
            self.view.afficherMenuPrincipal()
            choix = self.view.choixConsole("Choix : ")

            if choix == "1":
                self.gestionAchats()
            elif choix == "2":
                self.gestionQuetes()
            elif choix == "3":
                self.gestionDonjons()
            elif choix == "4":
                self.gestionPersonnage()
            elif choix == "5":
                self.view.afficherMessage("Merci d'avoir joué !")
                break
            else:
                self.view.afficherMessage("Choix invalide. Veuillez réessayer.")

    def gestionAchats(self):
        self.view.afficherMessage("Vous arrivez dans la boutique.")
        while True:
            self.view.afficherMenuAchats()
            choixAchats = self.view.choixConsole("Choix : ")

            if choixAchats == "1":
                self.gestionForgeron()
            elif choixAchats == "2":
                self.gestionMedecin()
            elif choixAchats == "3":
                self.view.afficherMessage("Vous quittez la boutique.")
                break
            else:
                self.view.afficherMessage("Choix invalide. Veuillez réessayer.")

    def gestionForgeron(self):
        self.view.afficherMessage("Vous arrivez chez le forgeron.")
        self.forgeron.afficherInventaire()
        choix = self.view.choixConsole("Choix : ")
        if choix.isdigit() and int(choix) == self.forgeron.getNbArmes() + 1:
            return
        elif choix.isdigit() and (int(choix) > 0 and int(choix) <= self.forgeron.getNbArmes()):
            try:
                arme = self.forgeron.getArmeIndex(int(choix) - 1)
                self.joueur.acheterArme(self.forgeron, arme)
                self.view.afficherMessage(f"Vous avez acheté l'arme {arme.getNom()} pour {arme.getValeurOr()} or.")
            except (InsufficientFundsError, NoSuchItemError) as e:
                self.view.afficherMessage(str(e))
            except ValueError:
                self.view.afficherMessage("Choix invalide. Veuillez entrer un nombre.")
        else:
            self.view.afficherMessage("Choix invalide.")

    def gestionMedecin(self):
        self.view.afficherMessage("Vous arrivez chez le médecin.")
        self.view.afficherMessage(self.medecin.afficherStockPotions())
        choix = self.view.choixConsole("Choix : ")
        if choix.isdigit() and int(choix) == 0:
            return
        elif choix.isdigit() and (int(choix) > 0 and int(choix) <= self.medecin.getStockPotions()):
            nbAchetes = 0
            for i in range(int(choix)):
                try:
                    self.joueur.acheterPotion(self.medecin)
                    nbAchetes += 1
                except (InsufficientFundsError, NoSuchItemError, InventoryFullError) as e:
                    self.view.afficherMessage(str(e))
                    break
            self.view.afficherMessage(f"Vous avez acheté {nbAchetes} potions.")
        else:
            self.view.afficherMessage("Choix invalide.")

    def gestionQuetes(self):
        self.view.afficherMessage(Quete.afficherToutesLesQuetesEnCours())
        choix = self.view.choixConsole("Choix d'une quête à accepter : ")
        if choix.isdigit() and int(choix) == Quete.getNbQuetesEnCours() + 1:
            return
        elif choix.isdigit() and (int(choix) > 0 and int(choix) <= Quete.getNbQuetesEnCours()):
            try:
                quete = Quete.getQueteIndexEnCours(int(choix) - 1)
                self.joueur.accepterQuete(quete)
                self.view.afficherMessage(f"Vous avez accepté la quête {quete.getNom()}.")
            except (QuestAlreadyAcceptedError, IndexError) as e:
                self.view.afficherMessage(str(e))
            except ValueError:
                self.view.afficherMessage("Choix invalide. Veuillez entrer un nombre.")
        else:
            self.view.afficherMessage("Choix invalide. Veuillez réessayer.")

    def gestionDonjons(self):
        self.view.afficherMessage(Donjon.afficherTousLesDonjonsActifs())
        choix = self.view.choixConsole("Choix d'un donjon à explorer : ")
        if choix.isdigit() and int(choix) == Donjon.nbDonjons + 1:
            return
        elif choix.isdigit() and (int(choix) > 0 and int(choix) <= Donjon.nbDonjons):
            donjon = Donjon.getDonjonIndexActif(int(choix) - 1)
            self.view.afficherMessage(f"Vous entrez dans le {donjon.getNom()}.")
            while not donjon.estVide():
                monstre = donjon.getMonstreAleatoire()
                self.view.afficherMessage(f"Vous rencontrez un {monstre.getNom()} !")
                while not self.joueur.estMort() and not monstre.estMort():
                    self.view.afficherMessage(f"Vous avez {self.joueur.getVie()} points de vie.")
                    self.view.afficherMessage(f"Le {monstre.getNom()} a {monstre.getVie()} points de vie.")
                    choix = self.view.choixConsole("1. Attaquer\n2. Boire une potion\n3. Fuir\nChoix : ")
                    if choix == "1":
                        self.view.afficherMessage(f"Vous attaquez {monstre.getNom()} !")
                        self.joueur.attaquer(monstre)
                        if not monstre.estMort():
                            self.view.afficherMessage(f"{monstre.getNom()} vous attaque !")
                            monstre.attaquer(self.joueur)
                    elif choix == "2":
                        try:
                            self.joueur.boirePotion()
                            self.view.afficherMessage("Vous avez bu une potion.")
                        except NoSuchItemError as e:
                            self.view.afficherMessage(str(e))
                    elif choix == "3":
                        self.view.afficherMessage("Vous avez fui.")
                        break
                    else:
                        self.view.afficherMessage("Choix invalide. Veuillez réessayer.")
                        continue
                if self.joueur.estMort():
                    self.joueur.resetApresMort()
                    break
                elif monstre.estMort():
                    try:
                        self.joueur.battreMonstre(monstre, donjon)
                    except NoActiveQuestError:
                        pass
            if donjon.estVide():
                donjon.setInactif()
        else:
            self.view.afficherMessage("Choix invalide. Veuillez réessayer.")

    def gestionPersonnage(self):
        while True:
            self.view.afficherMessage(str(self.joueur))
            self.view.afficherMenuPersonnage()
            choix = self.view.choixConsole("Choix : ")
            if choix == "1":
                self.view.afficherMessage(self.joueur.afficherArmes())
                choix = self.view.choixConsole("Choix d'arme à porter : ")
                if choix.isdigit() and int(choix) == self.joueur.getNbArmesInventaire() + 1:
                    break
                elif choix.isdigit():
                    try:
                        arme = self.joueur.getArmeIndexInventaire(int(choix) - 1)
                        self.joueur.equiperArme(arme)
                        self.view.afficherMessage(f"Vous avez équipé l'arme {arme.getNom()}.")
                    except (NoSuchItemError, IndexError) as e:
                        self.view.afficherMessage(str(e))
                    except ValueError:
                        self.view.afficherMessage("Choix invalide. Veuillez entrer un nombre.")
            elif choix == "2":
                try:
                    self.joueur.abandonnerQuete()
                    self.view.afficherMessage("Vous avez abandonné la quête.")
                except NoActiveQuestError as e:
                    self.view.afficherMessage(str(e))
            elif choix == "3":
                break
            else:
                self.view.afficherMessage("Choix invalide. Veuillez réessayer.")