from models.Personnage import Personnage
from models.Combattant import Combattant
from models.Arme import Arme

class Forgeron(Personnage):
    def __init__(self, nom, or_, vie):
        super().__init__(nom, or_, vie)
        self.inventaireArmes = []