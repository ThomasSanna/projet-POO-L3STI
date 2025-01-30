from models.Personnage import Personnage
from models.Quete import Quete
from models.Arme import Arme
from models.Donjon import Donjon

class Combattant(Personnage):
    def __init__(self, nom, or_, vie, inventairePotions):
        super().__init__(nom, or_, vie)
        self.inventairePotions = inventairePotions
        self.armeEquipee = None
        self.inventaireArmes = []
        self.queteActuelle = None
        self.donjonExplore = []