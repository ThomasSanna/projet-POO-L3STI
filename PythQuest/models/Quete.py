from models.Monstre import Monstre
from models.Donjon import Donjon
import random
from typing import List, Optional

class Quete:
    """
    Classe représentant une quête dans le jeu, avec un monstre cible, un donjon associé et une récompense.

    Attributs:
        PREFIXES (str): Préfixe utilisé pour générer les noms de quêtes.
        SUFFIXES (Tuple[str, ...]): Suffixes pour générer les noms de quêtes.
        STATUT_EN_COURS (str): Statut d'une quête en cours.
        STATUT_TERMINEE (str): Statut d'une quête terminée.
        toutesLesQuetes (List["Quete"]): Liste de toutes les quêtes créées.
    """

    PREFIXES: str = "Quête "  # Préfixe utilisé pour générer les noms de quêtes
    SUFFIXES: tuple[str, ...] = (
        "du savant fou", "de la libraire", "interdite",
        "de la montagne", "de la forêt", "du dragon",
        "de l'ombre", "de la lumière", "du guerrier",
        "de la sorcière", "du magicien", "du voleur",
        "du roi", "de la reine", "du prince",
        "de la princesse", "du chevalier", "de la fée",
        "du nain", "de l'elfe", "du géant",
        "du loup", "du serpent", "de l'araignée",
        "du scorpion", "du zombie", "du squelette",
        "du fantôme", "du vampire", "du loup-garou",
        "du démon", "de l'ange", "du dieu",
        "de la déesse", "du titan", "de la chimère",
        "du sphinx", "du minotaure", "du cyclope",
        "du centaure", "du dragonnier", "du chasseur",
        "du pêcheur", "du bûcheron", "du mineur"
    )  # Suffixes pour générer les noms de quêtes

    STATUT_EN_COURS: str = "En cours"  # Statut d'une quête en cours
    STATUT_TERMINEE: str = "Terminée"  # Statut d'une quête terminée

    toutesLesQuetes: List["Quete"] = []  # Liste de toutes les quêtes créées

    def __init__(self, nom: str, recompenseOr: int, difficulte: int, niveauJoueur: int) -> None:
        """
        Initialise une nouvelle quête.

        :param nom: Le nom de la quête.
        :param recompenseOr: La récompense en or pour la quête.
        :param difficulte: La difficulté de la quête.
        :param niveauJoueur: Le niveau du joueur pour adapter la quête.
        """
        self.id = len(Quete.toutesLesQuetes) + 1
        self.nom: str = nom
        self.recompenseOr: int = recompenseOr
        self.difficulte: int = difficulte
        self.monstreCible: Monstre = Monstre.creerMonstreAleatoire(difficulte, niveauJoueur)
        self.donjonAssocie: Donjon = Donjon.creerDonjonAleatoire(difficulte, self.monstreCible, niveauJoueur)
        self.statut: str = Quete.STATUT_EN_COURS
        self.niveau: int = niveauJoueur
        Quete.toutesLesQuetes.append(self)

    @staticmethod
    def creerQueteAleatoire(niveauJoueur: int) -> "Quete":
        """
        Crée une quête aléatoire basée sur le niveau du joueur.

        :param niveauJoueur: Le niveau du joueur pour adapter la difficulté et la récompense.
        :return: Une instance de Quete générée aléatoirement.
        """
        nom = Quete.PREFIXES + Quete.SUFFIXES[random.randint(0, len(Quete.SUFFIXES) - 1)]
        difficulte = random.randint(1, 5)
        recompenseOr = random.randint(difficulte * 15, difficulte * 35) + niveauJoueur * 10
        return Quete(nom, recompenseOr, difficulte, niveauJoueur)

    @staticmethod
    def afficherToutesLesQuetesEnCours() -> str:
        """
        Retourne une représentation textuelle de toutes les quêtes en cours.

        :return: Une chaîne de caractères listant les quêtes en cours.
        """
        result = []
        for i, quete in enumerate(Quete.getToutesLesQuetesEnCours()):
            if quete.getStatut() == Quete.STATUT_EN_COURS:
                result.append(f"{i + 1}. {quete}")
        result.append(f"{len(Quete.getToutesLesQuetesEnCours()) + 1}. Retour")
        return "\n".join(result)

    @staticmethod
    def getQueteIndexEnCours(id: int) -> "Quete":
        """
        Retourne une quête en cours à partir de son index.

        :param id: L'index de la quête dans la liste des quêtes en cours.
        :return: La quête correspondante.
        :raises IndexError: Si l'index est hors de portée.
        """
        quetes_en_cours = Quete.getToutesLesQuetesEnCours()
        if id < 0 or id >= len(quetes_en_cours):
            raise IndexError("Quête index hors de portée.")
        return quetes_en_cours[id]

    def queteFinie(self) -> None:
        """
        Marque la quête comme terminée.
        """
        self.statut = Quete.STATUT_TERMINEE

    def queteEnCours(self) -> None:
        """
        Marque la quête comme étant en cours.
        """
        self.statut = Quete.STATUT_EN_COURS

    def queteAbandonnee(self) -> None:
        """
        Marque la quête comme terminée (abandonnée).
        """
        pass

    def getNom(self) -> str:
        """
        Retourne le nom de la quête.

        :return: Le nom de la quête.
        """
        return self.nom

    def getMonstreCible(self) -> Monstre:
        """
        Retourne le monstre cible de la quête.

        :return: Le monstre cible.
        """
        return self.monstreCible

    def getDonjonAssocie(self) -> Donjon:
        """
        Retourne le donjon associé à la quête.

        :return: Le donjon associé.
        """
        return self.donjonAssocie

    def getStatut(self) -> str:
        """
        Retourne le statut actuel de la quête.

        :return: Le statut de la quête ("En cours" ou "Terminée").
        """
        return self.statut

    def getRecompenseOr(self) -> int:
        """
        Retourne la récompense en or de la quête.

        :return: La quantité d'or de la récompense.
        """
        return self.recompenseOr

    def getDifficulte(self) -> int:
        """
        Retourne la difficulté de la quête.

        :return: La difficulté de la quête.
        """
        return self.difficulte

    @staticmethod
    def getToutesLesQuetes() -> List["Quete"]:
        """
        Retourne la liste de toutes les quêtes créées.

        :return: La liste de toutes les quêtes.
        """
        return Quete.toutesLesQuetes

    @staticmethod
    def getToutesLesQuetesEnCours() -> List["Quete"]:
        """
        Retourne la liste de toutes les quêtes en cours.

        :return: La liste des quêtes en cours.
        """
        quetes = []
        for quete in Quete.toutesLesQuetes:
            if quete.getStatut() == Quete.STATUT_EN_COURS:
                quetes.append(quete)
        return quetes
    
    @staticmethod
    def getQuetesEnCoursUsingDifficulte(difficulte: int) -> List["Quete"]:
        """
        Retourne la liste des quêtes en cours pour une difficulté donnée.

        :param difficulte: La difficulté des quêtes à rechercher.
        :return: La liste des quêtes en cours pour la difficulté donnée.
        """
        quetes = []
        for quete in Quete.getToutesLesQuetesEnCours():
            if quete.getDifficulte() == difficulte:
                quetes.append(quete)
        return quetes

    @staticmethod
    def getNbQuetesEnCours() -> int:
        """
        Retourne le nombre de quêtes en cours.

        :return: Le nombre de quêtes en cours.
        """
        return len(Quete.getToutesLesQuetesEnCours())

    def __repr__(self) -> str:
        """
        Retourne une représentation formelle de la quête.

        :return: Une chaîne de caractères représentant la quête.
        """
        return self.__str__()

    def __str__(self) -> str:
        """
        Retourne une représentation détaillée de la quête.

        :return: Une chaîne de caractères décrivant la quête.
        """
        return f"{self.nom} (lvl {self.niveau}, difficulté {self.difficulte}) : Monstre à tuer : {self.monstreCible.getNom()} dans le {self.donjonAssocie.getNom()}, (récompense : {self.recompenseOr} or) ((statut : {self.statut}))"