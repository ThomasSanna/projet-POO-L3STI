from models.exceptions import InsufficientFundsError, InventoryFullError, NoSuchItemError, QuestAlreadyAcceptedError, NoActiveQuestError
from typing import Optional

class Personnage:
    """
    Classe de base représentant un personnage dans le jeu avec un nom, de l'or et de la vie.
    
    Attributs:
        nom (str): Le nom du personnage.
        piece (int): La quantité d'or du personnage.
        vie (int): La quantité de vie du personnage.
    """

    def __init__(self, nom: str, piece: int, vie: int) -> None:
        """
        Initialise un nouveau personnage.

        :param nom: Le nom du personnage.
        :param piece: La quantité d'or initiale du personnage.
        :param vie: La quantité de vie initiale du personnage.
        """
        self.nom: str = nom
        self.piece: int = piece
        self.vie: int = vie

    def gagnerOr(self, piece: int) -> None:
        """
        Ajoute une quantité d'or au personnage.

        :param piece: La quantité d'or à ajouter.
        """
        self.piece += piece

    def perdreOr(self, piece: int) -> None:
        """
        Retire une quantité d'or au personnage.

        :param piece: La quantité d'or à retirer.
        :raises InsufficientFundsError: Si le personnage n'a pas assez d'or pour effectuer la perte.
        """
        if self.piece - piece < 0:
            raise InsufficientFundsError("Vous n'avez pas assez d'or.")
        self.piece -= piece

    def perdreVie(self, degats: int) -> None:  # Correction du typage de retour
        """
        Retire une quantité de vie au personnage.

        La vie ne peut pas descendre en dessous de 0.

        :param degats: La quantité de dégâts à subir.
        """
        self.vie -= degats
        if self.vie <= 0:
            self.vie = 0

    def estMort(self) -> bool:
        """
        Vérifie si le personnage est mort.

        :return: True si la vie du personnage est à 0, False sinon.
        """
        return self.vie == 0

    def getNom(self) -> str:
        """
        Retourne le nom du personnage.

        :return: Le nom du personnage.
        """
        return self.nom

    def getOr(self) -> int:
        """
        Retourne la quantité d'or du personnage.

        :return: La quantité d'or.
        """
        return self.piece

    def getVie(self) -> int:
        """
        Retourne la quantité de vie du personnage.

        :return: La quantité de vie.
        """
        return self.vie

    def __str__(self) -> str:
        """
        Retourne une représentation textuelle du personnage.

        :return: Une chaîne de caractères décrivant le personnage.
        """
        return f"Personnage(nom={self.nom}, piece={self.piece}, vie={self.vie})"