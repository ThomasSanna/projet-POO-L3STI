from models.Personnage import Personnage
from models.Arme import Arme

class Monstre(Personnage):
    def __init__(self, nom, or_, vie, difficulte):
        super().__init__(nom, or_, vie)
        self.difficulte = difficulte
        self.armePossedee = None