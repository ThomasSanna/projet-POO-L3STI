from models.Personnage import Personnage
import random

class Medecin(Personnage):
    def __init__(self, nom: str):
        super().__init__(nom, 0, 100)
        self.prixPotion = 10
        self.stockPotions = 5
        
    def perdrePotion(self) -> None:
        self.stockPotions -= 1
        
    def restockPotions(self) -> None:
        self.stockPotions = random.randint(2, 5)
        
    def getPrixPotion(self) -> int:
        return self.prixPotion

    def getStockPotions(self) -> int:
        return self.stockPotions
        
    def __str__(self) -> str:
        return (f"Medecin {self.nom}, {self.stockPotions} potions en stock")