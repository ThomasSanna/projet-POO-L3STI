from models.Personnage import Personnage
import random
from typing import Optional

class Medecin(Personnage):
    """Classe représentant un médecin qui vend des potions dans le jeu."""

    NB_POTION_MAX: int = 10  # Nombre maximum de potions dans le stock du médecin

    def __init__(self, nom: str) -> None:
        """
        Initialise un nouveau médecin avec un nom donné.

        :param nom: Le nom du médecin.
        """
        super().__init__(nom, 0, 100)  # Initialise avec 0 or et 100 de vie
        self.prixPotion: int = 10  # Prix fixe d'une potion
        self.stockPotions: int = random.randint(4, 8)  # Stock initial aléatoire entre 4 et 8 potions

    def perdrePotion(self) -> None:
        """
        Retire une potion du stock du médecin.
        """
        self.stockPotions -= 1

    def restockPotions(self) -> None:
        """
        Réapprovisionne le stock de potions du médecin avec un nombre aléatoire.

        Le stock ne dépasse pas NB_POTION_MAX.
        """
        self.stockPotions += random.randint(3, 6)
        if self.stockPotions > Medecin.NB_POTION_MAX:
            self.stockPotions = Medecin.NB_POTION_MAX

    def afficherStockPotions(self) -> str:
        """
        Retourne une représentation textuelle du stock de potions et des options d'achat.

        :return: Une chaîne de caractères décrivant le stock et les choix possibles.
        """
        result = f"{self.stockPotions} potions en stock\n"
        result += f"Prix d'une potion: {self.prixPotion} pièces d'or\n"
        if self.stockPotions == 0:
            result += "Le stock est vide. 0 pour retourner au menu."
        else:
            result += f"Combien de potions voulez-vous acheter? (1-{self.stockPotions}). 0 pour retourner au menu."
        return result

    def getPrixPotion(self) -> int:
        """
        Retourne le prix d'une potion.

        :return: Le prix d'une potion en pièces d'or.
        """
        return self.prixPotion

    def getStockPotions(self) -> int:
        """
        Retourne le nombre de potions actuellement en stock.

        :return: Le nombre de potions dans le stock.
        """
        return self.stockPotions

    def __str__(self) -> str:
        """
        Retourne une représentation détaillée du médecin.

        :return: Une chaîne de caractères représentant le médecin.
        """
        return f"Medecin {self.nom}, {self.stockPotions} potions en stock"