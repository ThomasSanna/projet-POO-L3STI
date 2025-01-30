from models.Personnage import Personnage
import random

class Medecin(Personnage):
    def __init__(self, nom: str):
        super().__init__(nom, 0, 100)
        self.prixPotion = 10
        self.stockPotions = 5
        
    def setPrixPotion(self, prixPotion: int) -> None:
        self.prixPotion = prixPotion
        
    def perdrePotion(self) -> None:
        self.stockPotions -= 1
        
    def restockPotions(self) -> None:
        self.stockPotions = random.randint(2, 5)
        
    def __str__(self) -> str:
        return (f"Medecin(nom={self.nom}, or_={self.or_}, vie={self.vie}, stockPotions={self.stockPotions})")