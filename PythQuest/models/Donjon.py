from models.Monstre import Monstre
import random
from typing import List, Optional

class Donjon:
    """Classe représentant un donjon avec des monstres, une difficulté et un statut."""

    PREFIXES: str = "Donjon "  # Préfixe utilisé pour générer les noms de donjons
    SUFFIXES: tuple[str, ...] = (
        "sombre", "glacial", "ancien", "mystérieux", "perdu", "maudit", "dangereux", 
        "sinistre", "hanté", "abandonné", "oublié", "délabré", "dévasté", "déchu",
        "majestueux", "infini", "souterrain", "enchanté", "démoniaque", "caché",
        "profond", "infesté", "désolé", "désespéré", "interdit", "ténébreux", 
        "sanguinaire", "corrompu", "lumineux", "rougeoyant", "chaotique", "immortel",
        "pestiféré", "tombé", "destructeur", "légendaire", "éternel", "foudroyé",
        "ensorcelé", "inexorable", "voilé", "métallique", "runique", "cristallin",
        "doré", "argenté", "de glace", "de feu", "de pierre", "de lave", "de l'ombre",
        "de la lumière", "de la mort", "de la vie", "de la guerre", "de la paix",
        "de la brume", "du crépuscule", "de l'aube", "de l'éclipse", "de la tempête",
        "de la foudre", "de la terreur", "de l'oubli", "de la renaissance", "du chaos",
        "de l'ordre", "de la destruction", "de la création", "de l'illusion", "de la réalité",
        "de l'infini", "de l'éternité", "de l'abîme", "de la caverne", "de la montagne",
        "de la vallée", "de la forêt", "de la mer", "de l'océan", "du désert",
        "de la plaine", "de la jungle", "de la savane", "de la toundra", "de l'arctique",
        "de l'antarctique", "de l'espace", "de la galaxie", "de l'univers", "du multivers"
    )  # Suffixes pour générer les noms de donjons

    ACTIF: str = "Actif"  # Statut d'un donjon actif
    INACTIF: str = "Inactif"  # Statut d'un donjon inactif

    tousLesDonjons: List["Donjon"] = []  # Liste de tous les donjons créés
    nbDonjons: int = 1  # Compteur d'identifiants des donjons

    def __init__(self, nom: str, difficulte: int, niveauJoueur: int, monstre: Optional[Monstre] = None) -> None:
        """
        Initialise un nouveau donjon.

        :param nom: Le nom du donjon.
        :param difficulte: La difficulté du donjon.
        :param niveauJoueur: Le niveau du joueur pour adapter les monstres.
        :param monstre: Un monstre optionnel à ajouter initialement. Par défaut None.
        """
        self.id: int = Donjon.nbDonjons
        Donjon.nbDonjons += 1
        self.nom: str = nom
        self.difficulte: int = difficulte
        self.listeMonstres: List[Monstre] = []
        if monstre is not None:
            self.listeMonstres = [monstre]
        self.ajouterNbMonstre(random.randint(3, 10), niveauJoueur)
        self.statut: str = Donjon.ACTIF
        self.niveau: int = niveauJoueur
        Donjon.tousLesDonjons.append(self)

    @staticmethod
    def creerDonjonAleatoire(difficulte: int, monstre: Monstre, niveauJoueur: int) -> "Donjon":
        """
        Crée un donjon avec un nom aléatoire.

        :param difficulte: La difficulté du donjon.
        :param monstre: Le monstre initial à inclure.
        :param niveauJoueur: Le niveau du joueur pour adapter les monstres.
        :return: Le donjon créé.
        """
        prefixe = Donjon.PREFIXES
        suffixe = Donjon.SUFFIXES[random.randint(0, len(Donjon.SUFFIXES) - 1)]
        nom = prefixe + suffixe
        donjon = Donjon(nom, difficulte, niveauJoueur, monstre)
        return donjon

    @staticmethod
    def afficherTousLesDonjonsActifs() -> str:
        """
        Retourne une représentation textuelle de tous les donjons actifs.

        :return: Une chaîne de caractères listant les donjons actifs.
        """
        result = []
        for i, donjon in enumerate(Donjon.getTousLesDonjonsActifs()):
            if donjon.statut == Donjon.ACTIF:  # Cette condition est redondante avec getTousLesDonjonsActifs
                result.append(f"{i + 1}. {donjon.nom} (lvl {donjon.niveau}, difficulté {donjon.difficulte}). Nombre de monstres: {len(donjon.listeMonstres)}")
        result.append(f"{len(Donjon.getTousLesDonjonsActifs()) + 1}. Retour")
        return "\n".join(result)

    def ajouterNbMonstre(self, nb: int, niveauJoueur: int) -> None:
        """
        Ajoute un nombre spécifié de monstres aléatoires au donjon.

        :param nb: Le nombre de monstres à ajouter.
        :param niveauJoueur: Le niveau du joueur pour adapter les monstres.
        """
        for _ in range(nb):
            monstre = Monstre.creerMonstreAleatoire(self.difficulte, niveauJoueur)
            self.listeMonstres.append(monstre)

    def supprimerMonstre(self, monstre: Monstre) -> None:
        """
        Supprime un monstre du donjon.

        :param monstre: Le monstre à supprimer.
        :raises ValueError: Si le monstre n'est pas dans la liste des monstres du donjon.
        """
        if monstre in self.listeMonstres:
            self.listeMonstres.remove(monstre)
        else:
            raise ValueError("Le monstre n'est pas dans la liste des monstres du donjon.")

    def getMonstreAleatoire(self) -> Monstre:
        """
        Retourne un monstre aléatoire du donjon.

        :return: Un monstre choisi aléatoirement dans la liste.
        """
        return random.choice(self.listeMonstres)

    def setInactif(self) -> None:
        """
        Définit le statut du donjon comme inactif.
        """
        self.statut = Donjon.INACTIF

    def estVide(self) -> bool:
        """
        Vérifie si le donjon est vide de monstres.

        :return: True si aucun monstre n'est présent, False sinon.
        """
        return len(self.listeMonstres) == 0

    def getListeMonstres(self) -> List[Monstre]:
        """
        Retourne la liste des monstres du donjon.

        :return: La liste des monstres.
        """
        return self.listeMonstres

    def getNom(self) -> str:
        """
        Retourne le nom du donjon.

        :return: Le nom du donjon.
        """
        return self.nom

    def getDifficulte(self) -> int:
        """
        Retourne la difficulté du donjon.

        :return: La difficulté du donjon.
        """
        return self.difficulte

    def getId(self) -> int:
        """
        Retourne l'identifiant du donjon.

        :return: L'identifiant du donjon.
        """
        return self.id

    def getNbMonstres(self) -> int:
        """
        Retourne le nombre de monstres dans le donjon.

        :return: Le nombre de monstres.
        """
        return len(self.listeMonstres)

    @staticmethod
    def getTousLesDonjons() -> List["Donjon"]:
        """
        Retourne la liste de tous les donjons créés.

        :return: La liste de tous les donjons.
        """
        return Donjon.tousLesDonjons

    @staticmethod
    def getTousLesDonjonsActifs() -> List["Donjon"]:
        """
        Retourne la liste de tous les donjons actifs.

        :return: La liste des donjons actifs.
        """
        donjonsActifs = []
        for donjon in Donjon.tousLesDonjons:
            if donjon.statut == Donjon.ACTIF:
                donjonsActifs.append(donjon)
        return donjonsActifs

    @staticmethod
    def getDonjonIndexActif(index: int) -> "Donjon":
        """
        Retourne un donjon actif à partir de son index dans la liste des donjons actifs.

        :param index: L'index du donjon dans la liste des donjons actifs.
        :return: Le donjon correspondant à l'index.
        :raises IndexError: Si l'index est hors de portée.
        """
        donjonsActifs = Donjon.getTousLesDonjonsActifs()
        if index < 0 or index >= len(donjonsActifs):
            raise IndexError("Donjon index out of range.")
        return donjonsActifs[index]

    @staticmethod
    def getNbDonjonsActifs() -> int:
        """
        Retourne le nombre de donjons actifs.

        :return: Le nombre de donjons actifs.
        """
        return len(Donjon.getTousLesDonjonsActifs())  # Correction: ajout du return manquant

    def __repr__(self) -> str:
        """
        Retourne une représentation formelle du donjon.

        :return: Une chaîne de caractères représentant le donjon.
        """
        return self.__str__()

    def __str__(self) -> str:
        """
        Retourne une représentation détaillée du donjon.

        :return: Une chaîne de caractères représentant le donjon.
        """
        return f"{self.nom} (id: {self.id}, niveau: {self.niveau}, difficulté: {self.difficulte}, monstres: {self.listeMonstres}, statut: {self.statut})"