from models.Personnage import Personnage

class Medecin(Personnage):
    def __init__(self, nom, or_, vie, stockPotions):
        super().__init__(nom, or_, vie)
        self.stockPotions = stockPotions