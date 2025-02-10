from models.Personnage import Personnage
import random

class Medecin(Personnage):
    
    NB_POTION_MAX = 10
    
    def __init__(self, nom: str):
        super().__init__(nom, 0, 100)
        self.prixPotion = 10
        self.stockPotions = random.randint(4, 8)
        
    def perdrePotion(self) -> None:
        self.stockPotions -= 1
        
    def restockPotions(self) -> None:
        self.stockPotions += random.randint(3, 6)
        if self.stockPotions > Medecin.NB_POTION_MAX:
            self.stockPotions = Medecin.NB_POTION_MAX
            
    def afficherStockPotions(self) -> str:
        result = f"{self.stockPotions} potions en stock\n"
        result += f"Prix d'une potion: {self.prixPotion} pièces d'or\n"
        if self.stockPotions == 0:
            result += "Le stock est vide. 0 pour retourner au menu."
        else:
            result += f"Combien de potions voulez-vous acheter? (1-{self.stockPotions}). 0 pour retourner au menu."
        return result
        
    def getPrixPotion(self) -> int:
        return self.prixPotion

    def getStockPotions(self) -> int:
        return self.stockPotions
        
    def __str__(self) -> str:
        return (f"Medecin {self.nom}, {self.stockPotions} potions en stock")