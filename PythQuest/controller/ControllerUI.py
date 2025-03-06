import tkinter as tk
from models.Combattant import Combattant
from models.Forgeron import Forgeron
from models.Medecin import Medecin
from models.Quete import Quete
from models.Donjon import Donjon
from models.Monstre import Monstre
from models.Arme import Arme
from models.GestionnaireDeQuetes import GestionnaireDeQuetes
from models.exceptions import InsufficientFundsError, InventoryFullError, NoSuchItemError, QuestAlreadyAcceptedError, NoActiveQuestError
from view.ViewUI import ViewUI
import random
import time
from typing import Tuple

class ControllerUI:
    def __init__(self, root):
        self.view = ViewUI(root)
        self.joueur = Combattant("Joueur") # a faire : demander le nom du joueur
        self.forgeron, self.medecin = self.initialiserInstances()
        self.creerQuete(self.joueur, 2, 4)
        self.updateStats()
        self.afficherMenuPrincipal()

    def initialiserInstances(self) -> Tuple[Forgeron, Medecin]:
        forgeron = Forgeron("Robert")
        medecin = Medecin("Jean")
        return forgeron, medecin

    def creerQuete(self, joueur: Combattant, minQuete: int, maxQuete: int) -> None:
        for _ in range(random.randint(minQuete, maxQuete)):
            GestionnaireDeQuetes.creerQueteDonjonMonstres(joueur.getNiveau())

    def updateStats(self) -> None:
        self.view.updateVie(self.joueur.getVie())
        self.view.updatePiece(self.joueur.getOr())
        self.view.updateNiveau(self.joueur.getNiveau(), self.joueur.getExperience())

    def afficherMenuPrincipal(self) -> None:
        self.view.showChoices([
            {"text": "Faire des achats", "command": self.gestionAchats},
            {"text": "Voir les quêtes", "command": self.gestionQuetes},
            {"text": "Voir les donjons", "command": self.gestionDonjons},
            {"text": "Informations sur le personnage", "command": self.gestionPersonnage},
            {"text": "Quitter le jeu", "command": self.quitterJeu}
        ])

    def quitterJeu(self) -> None:
        self.view.showMessage("Merci d'avoir joué !")
        self.view.root.quit()

    def gestionAchats(self):
        self.view.showChoices([
            {"text": "Visiter le Forgeron", "command": self.gestionForgeron},
            {"text": "Visiter le Médecin", "command": self.gestionMedecin},
            {"text": "Retour", "command": self.afficherMenuPrincipal}
        ])

    def gestionForgeron(self) -> None:
        armes = self.forgeron.getInventaireArmes()
        choices = [{"text": f"{arme}", "command": lambda arme=arme: self.acheterArme(arme)} for arme in armes]
        choices.append({"text": "Retour", "command": self.gestionAchats})
        self.view.showChoices(choices)

    def acheterArme(self, arme: Arme) -> None:
        try:
            self.joueur.acheterArme(self.forgeron, arme)
            self.view.showMessage(f"Vous avez acheté l'arme {arme.getNom()} pour {arme.getValeurOr()} or.")
            self.updateStats()
        except (InsufficientFundsError, NoSuchItemError) as e:
            self.view.showMessage(str(e))
        self.gestionForgeron()

    def gestionMedecin(self) -> None:
        stock = self.medecin.getStockPotions()
        choices = [{"text": f"Acheter {i} potion(s)", "command": lambda i=i: self.acheterPotion(i)} for i in range(1, stock + 1)]
        choices.append({"text": "Retour", "command": self.gestionAchats})
        self.view.showChoices(choices)

    def acheterPotion(self, quantite: int) -> None:
        try:
            for _ in range(quantite):
                self.joueur.acheterPotion(self.medecin)
            self.view.showMessage(f"Vous avez acheté {quantite} potion(s).")
            self.updateStats()
        except (InsufficientFundsError, NoSuchItemError, InventoryFullError) as e:
            self.view.showMessage(str(e))
        self.gestionMedecin()

    def gestionQuetes(self) -> None:
        quetes = Quete.getToutesLesQuetesEnCours()
        choices = [{"text": f"{quete}", "command": lambda quete=quete: self.accepterQuete(quete)} for quete in quetes]
        choices.append({"text": "Retour", "command": self.afficherMenuPrincipal})
        self.view.showChoices(choices)

    def accepterQuete(self, quete: Quete) -> None:
        try:
            self.joueur.accepterQuete(quete)
            self.view.showMessage(f"Vous avez accepté la quête {quete.getNom()}.")
        except (QuestAlreadyAcceptedError, IndexError) as e:
            self.view.showMessage(str(e))
        self.gestionQuetes()

    def gestionDonjons(self) -> None:
        donjons = Donjon.getTousLesDonjonsActifs()
        choices = [{"text": f"{donjon}", "command": lambda donjon=donjon: self.explorerDonjon(donjon)} for donjon in donjons]
        choices.append({"text": "Retour", "command": self.afficherMenuPrincipal})
        self.view.showChoices(choices)

    def explorerDonjon(self, donjon: Donjon) -> None:
        self.view.showMessage(f"Vous entrez dans le {donjon.getNom()}.")
        self.combatDonjon(donjon)

    def combatDonjon(self, donjon: Donjon) -> None:
        if donjon.estVide():
            donjon.setInactif()
            self.creerQuete(self.joueur, 1, 2)
            self.view.showMessage(f"Vous avez vidé le {donjon.getNom()} ! Retour au village.")
            self.afficherMenuPrincipal()
            return

        monstre = donjon.getMonstreAleatoire()
        self.view.showMessage(f"Vous rencontrez un {monstre.getNom()} !")
        self.combatMonstre(monstre, donjon)

    def combatMonstre(self, monstre: Monstre, donjon: Donjon) -> None:
        if self.joueur.estMort():
            messages = self.joueur.resetApresMort()
            for message in messages:
                self.view.showMessage(message)
            self.updateStats()
            self.afficherMenuPrincipal()
            return

        if monstre.estMort():
            messages = self.joueur.battreMonstre(monstre, donjon)
            for message in messages:
                if message.startswith("Félicitations ! Vous avez terminé la") or message.startswith("Félicitations ! Vous avez atteint le niveau"):
                    self.creerQuete(self.joueur, 1, 2)
                self.view.showMessage(message)
            self.updateStats()
            self.combatDonjon(donjon)
            return

        self.view.showChoices([
            {"text": "Attaquer", "command": lambda: self.attaquerMonstre(monstre, donjon)},
            {"text": "Boire une potion", "command": lambda: self.boirePotion(monstre, donjon)},
            {"text": "Fuir", "command": self.afficherMenuPrincipal}
        ])

    def attaquerMonstre(self, monstre: Monstre, donjon: Donjon) -> None:
        self.view.showMessage(f"Vous attaquez {monstre.getNom()} !")
        self.view.showMessage(f"Le {monstre.getNom()} a {monstre.getVie()} points de vie.")
        self.joueur.attaquer(monstre)
        self.updateStats()
        if not monstre.estMort():
            self.view.showMessage(f"{monstre.getNom()} vous attaque !")
            monstre.attaquer(self.joueur)
            self.updateStats()
        self.combatMonstre(monstre, donjon)

    def boirePotion(self, monstre: Monstre, donjon: Donjon) -> None:
        try:
            self.joueur.boirePotion()
            self.view.showMessage("Vous avez bu une potion.")
            self.updateStats()
        except NoSuchItemError as e:
            self.view.showMessage(str(e))
        self.combatMonstre(monstre, donjon)

    def gestionPersonnage(self) -> None:
        self.view.showChoices([
            {"text": "Changer d'arme", "command": self.changerArme},
            {"text": "Abandonner la quête", "command": self.abandonnerQuete},
            {"text": "Retour", "command": self.afficherMenuPrincipal}
        ])

    def changerArme(self) -> None:
        armes = self.joueur.getInventaireArmes()
        choices = [{"text": f"{arme}", "command": lambda arme=arme: self.equiperArme(arme)} for arme in armes]
        choices.append({"text": "Retour", "command": self.gestionPersonnage})
        self.view.showChoices(choices)

    def equiperArme(self, arme: Arme) -> None:
        try:
            self.joueur.equiperArme(arme)
            self.view.showMessage(f"Vous avez équipé l'arme {arme.getNom()}.")
        except NoSuchItemError as e:
            self.view.showMessage(str(e))
        self.gestionPersonnage()

    def abandonnerQuete(self) -> None:
        try:
            self.joueur.abandonnerQuete()
            self.view.showMessage("Vous avez abandonné la quête.")
        except NoActiveQuestError as e:
            self.view.showMessage(str(e))
        self.gestionPersonnage()