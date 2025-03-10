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
from view.View import View
import random
import time
from typing import Tuple

class Controller:
    """
    Classe représentant le contrôleur principal du jeu
    Cette classe gère la logique du jeu et les interactions entre la vue (View) et les modèles.

    Attributs:
        view (View): Interface graphique du jeu
        joueur (Combattant): Instance du joueur principal
        forgeron (Forgeron): Instance du forgeron pour acheter des armes
        medecin (Medecin): Instance du médecin pour acheter des potions
    """

    def __init__(self, root):
        """
        Initialise le contrôleur avec la fenêtre principale et configure les instances de base.

        :param root: Fenêtre principale de l'application Tkinter
        """
        self.view = View(root)
        self.joueur = Combattant("Joueur")  # TODO: Demander le nom du joueur
        self.forgeron, self.medecin = self.initialiserInstances()
        self.creerQueteArme(self.joueur, 4, 6)
        self.updateStats()
        self.afficherMenuPrincipal()

    def initialiserInstances(self) -> Tuple[Forgeron, Medecin]:
        """
        Crée et initialise les instances du forgeron et du médecin.

        :return: Tuple contenant l'instance du forgeron et du médecin
        """
        forgeron = Forgeron("Robert")
        medecin = Medecin("Jean")
        return forgeron, medecin

    def creerQueteArme(self, joueur: Combattant, minQuete: int, maxQuete: int) -> None:
        """
        Crée un nombre aléatoire de quêtes et d'armes pour le joueur.

        :param joueur: Instance du joueur (Combattant)
        :param minQuete: Nombre minimum de quêtes à créer
        :param maxQuete: Nombre maximum de quêtes à créer
        """
        for _ in range(random.randint(minQuete, maxQuete)):
            GestionnaireDeQuetes.creerQueteDonjonMonstres(joueur.getNiveau())
        for _ in range(random.randint(1, 2)):
            self.forgeron.forgerArme()

    def updateStats(self) -> None:
        """
        Met à jour les statistiques du joueur dans l'interface graphique (vie, pièces, niveau, arme équipée).
        """
        self.view.updateVie(self.joueur.getVie())
        self.view.updatePiece(self.joueur.getOr())
        self.view.updateNiveau(self.joueur.getNiveau(), self.joueur.getExperience())
        armeEquippee = self.joueur.getArmeEquipee()
        self.view.updateArmeEquipee(armeEquippee.getNom(), armeEquippee.getDegats())

    def afficherMenuPrincipal(self) -> None:
        """
        Affiche le menu principal du jeu avec les options disponibles.
        """
        self.view.supprimerMonstre()
        self.view.showChoices([
            {"text": "Faire des achats", "command": self.gestionAchats},
            {"text": "Voir les quêtes", "command": self.gestionQuetes},
            {"text": "Voir les donjons", "command": self.gestionDonjons},
            {"text": "Informations sur le personnage", "command": self.gestionPersonnage},
            {"text": "Quitter le jeu", "command": self.quitterJeu}
        ])

    def quitterJeu(self) -> None:
        """
        Ferme le jeu et affiche un message de fin.
        """
        self.view.showMessage("Merci d'avoir joué !")
        self.view.root.quit()

    def gestionAchats(self):
        """
        Affiche les options d'achat (forgeron, médecin, retour au menu principal).
        """
        self.view.showChoices([
            {"text": "Visiter le Forgeron", "command": self.gestionForgeron},
            {"text": "Visiter le Médecin", "command": self.gestionMedecin},
            {"text": "Retour", "command": self.afficherMenuPrincipal}
        ])

    def gestionForgeron(self) -> None:
        """
        Affiche les armes disponibles chez le forgeron pour achat.
        """
        armes = self.forgeron.getInventaireArmes()
        choices = [{"text": f"{arme}", "image": arme.getImage(), "command": lambda arme=arme: self.acheterArme(arme)} for arme in armes]
        choices.append({"text": "Retour", "command": self.gestionAchats})
        self.view.showChoicesWithImages(choices)

    def acheterArme(self, arme: Arme) -> None:
        """
        Gère l'achat d'une arme par le joueur auprès du forgeron.

        :param arme: Arme à acheter
        :raises InsufficientFundsError: Si le joueur n'a pas assez d'or
        :raises NoSuchItemError: Si l'arme n'est pas disponible
        """
        try:
            self.joueur.acheterArme(self.forgeron, arme)
            self.view.showMessage(f"Vous avez acheté l'arme {arme.getNom()} pour {arme.getValeurOr()} or.")
            self.updateStats()
        except (InsufficientFundsError, NoSuchItemError) as e:
            self.view.showMessage(str(e))
        self.gestionForgeron()

    def gestionMedecin(self) -> None:
        """
        Affiche les options pour acheter des potions chez le médecin.
        """
        stock = self.medecin.getStockPotions()
        choices = [{"text": f"Acheter {i} potion(s)", "command": lambda i=i: self.acheterPotion(i)} for i in range(1, stock + 1)]
        choices.append({"text": "Retour", "command": self.gestionAchats})
        self.view.showChoices(choices)

    def acheterPotion(self, quantite: int) -> None:
        """
        Gère l'achat de potions par le joueur auprès du médecin.

        :param quantite: Nombre de potions à acheter
        :raises InsufficientFundsError: Si le joueur n'a pas assez d'or
        :raises NoSuchItemError: Si les potions ne sont pas disponibles
        :raises InventoryFullError: Si l'inventaire du joueur est plein
        """
        try:
            for _ in range(quantite):
                self.joueur.acheterPotion(self.medecin)
            self.view.showMessage(f"Vous avez acheté {quantite} potion(s).")
            self.updateStats()
        except (InsufficientFundsError, NoSuchItemError, InventoryFullError) as e:
            self.view.showMessage(str(e))
        self.gestionMedecin()

    def gestionQuetes(self) -> None:
        """
        Affiche la liste des quêtes disponibles pour acceptation.
        """
        quetes = Quete.getToutesLesQuetesEnCours()
        choices = [{"text": f"{quete.getNom()} ({'★' * quete.getDifficulte()}) - Monstre: {quete.getMonstreCible().getNom()} dans le {quete.getDonjonAssocie().getNom()}", "command": lambda quete=quete: self.accepterQuete(quete)} for quete in quetes]
        choices.append({"text": "Retour", "command": self.afficherMenuPrincipal})
        self.view.showChoices(choices)

    def accepterQuete(self, quete: Quete) -> None:
        """
        Permet au joueur d'accepter une quête.

        :param quete: Quête à accepter
        :raises QuestAlreadyAcceptedError: Si une quête est déjà en cours
        :raises IndexError: Si la quête n'est pas valide
        """
        try:
            self.joueur.accepterQuete(quete)
            self.view.showMessage(f"Vous avez accepté la quête {quete.getNom()}.")
            self.view.updateQuestInfo(quete)
        except (QuestAlreadyAcceptedError, IndexError) as e:
            self.view.showMessage(str(e))
        self.gestionQuetes()

    def abandonnerQuete(self) -> None:
        """
        Permet au joueur d'abandonner la quête en cours.

        :raises NoActiveQuestError: Si aucune quête n'est en cours
        """
        try:
            self.joueur.abandonnerQuete()
            self.view.showMessage("Vous avez abandonné la quête.")
            self.view.updateQuestInfo(None)
        except NoActiveQuestError as e:
            self.view.showMessage(str(e))
        self.gestionPersonnage()

    def gestionDonjons(self) -> None:
        """
        Affiche la liste des donjons disponibles pour exploration.
        """
        donjons = Donjon.getTousLesDonjonsActifs()
        choices = [{"text": f"{donjon.getNom()} ({'★' * donjon.getDifficulte()}) - Monstres: {donjon.getNbMonstres()}", "command": lambda donjon=donjon: self.explorerDonjon(donjon)} for donjon in donjons]
        choices.append({"text": "Retour", "command": self.afficherMenuPrincipal})
        self.view.showChoices(choices)

    def explorerDonjon(self, donjon: Donjon) -> None:
        """
        Lance l'exploration d'un donjon par le joueur.

        :param donjon: Donjon à explorer
        """
        self.view.showMessage(f"Vous entrez dans le {donjon.getNom()}.")
        self.combatDonjon(donjon)

    def combatDonjon(self, donjon: Donjon) -> None:
        """
        Gère le combat dans un donjon, en affrontant les monstres un par un.

        :param donjon: Donjon en cours d'exploration
        """
        if donjon.estVide():
            donjon.setInactif()
            self.creerQueteArme(self.joueur, 1, 2)
            self.view.showMessage(f"Vous avez vidé le {donjon.getNom()} ! Retour au village.")
            self.afficherMenuPrincipal()
            return

        monstre = donjon.getMonstreAleatoire()
        self.view.showMessage(f"Vous rencontrez un {monstre.getNom()} !")
        self.view.afficherMonstre(monstre.getNom(), monstre.getVie(), monstre.getArmePossedee().getNom())
        self.combatMonstre(monstre, donjon)

    def combatMonstre(self, monstre: Monstre, donjon: Donjon) -> None:
        """
        Gère le combat entre le joueur et un monstre dans un donjon.

        :param monstre: Monstre à combattre
        :param donjon: Donjon où se déroule le combat
        """
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
                if message.startswith("Félicitations ! Vous avez terminé la") or message.startswith("Félicitations ! Vous avez atteint le niveau"): # Quête terminée ou niveau monté
                    self.medecin.restockPotions()
                    self.creerQueteArme(self.joueur, 1, 2)
                    if message.startswith("Félicitations ! Vous avez terminé la"):
                        self.view.updateQuestInfo(None)
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
        """
        Permet au joueur d'attaquer un monstre et gère la riposte du monstre.

        :param monstre: Monstre à attaquer
        :param donjon: Donjon où se déroule le combat
        """
        self.view.showMessage(f"Vous attaquez {monstre.getNom()} !")
        self.joueur.attaquer(monstre)
        self.view.showMessage(f"Le {monstre.getNom()} a {monstre.getVie()} points de vie.")
        self.view.updateMonstre(monstre.getVie())
        if not monstre.estMort():
            self.view.showMessage(f"{monstre.getNom()} vous attaque !")
            monstre.attaquer(self.joueur)
            self.updateStats()
        self.combatMonstre(monstre, donjon)

    def boirePotion(self, monstre: Monstre, donjon: Donjon) -> None:
        """
        Permet au joueur de boire une potion pour récupérer des points de vie.

        :param monstre: Monstre en cours de combat
        :param donjon: Donjon où se déroule le combat
        :raises NoSuchItemError: Si aucune potion n'est disponible
        """
        try:
            self.joueur.boirePotion()
            self.view.showMessage("Vous avez bu une potion.")
            self.updateStats()
        except NoSuchItemError as e:
            self.view.showMessage(str(e))
        self.combatMonstre(monstre, donjon)

    def gestionPersonnage(self) -> None:
        """
        Affiche les options de gestion du personnage (changer d'arme, abandonner une quête, retour).
        """
        self.view.showChoices([
            {"text": "Changer d'arme", "command": self.changerArme},
            {"text": "Abandonner la quête", "command": self.abandonnerQuete},
            {"text": "Retour", "command": self.afficherMenuPrincipal}
        ])

    def changerArme(self) -> None:
        """
        Affiche les armes disponibles dans l'inventaire du joueur pour les équiper.
        """
        armes = self.joueur.getInventaireArmes()
        choices = [{"text": f"{arme.getNom()} ({arme.getDegats()} dgts)", "image": arme.getImage(), "command": lambda arme=arme: self.equiperArme(arme)} for arme in armes]
        choices.append({"text": "Retour", "command": self.gestionPersonnage})
        self.view.showChoicesWithImages(choices)

    def equiperArme(self, arme: Arme) -> None:
        """
        Permet au joueur d'équiper une arme de son inventaire.

        :param arme: Arme à équiper
        :raises NoSuchItemError: Si l'arme n'est pas dans l'inventaire
        """
        try:
            self.joueur.equiperArme(arme)
            self.view.showMessage(f"Vous avez équipé l'arme {arme.getNom()}.")
            self.updateStats()
        except NoSuchItemError as e:
            self.view.showMessage(str(e))
        self.gestionPersonnage()