from models.Monstre import Monstre
from models.Donjon import Donjon

class Quete:
  
    STATUT_CREEE = "Créée"
    STATUT_EN_COURS = "En cours"
    STATUT_TERMINEE = "Terminée"
  
    def __init__(self, description, recompenseOr, monstreCible, donjonAssocie):
        self.description = description
        self.recompenseOr = recompenseOr
        self.monstreCible = monstreCible
        self.donjonAssocie = donjonAssocie
        self.statut = Quete.STATUT_CREEE
        
    def __str__(self):
        return (f"Quete(description={self.description}, recompenseOr={self.recompenseOr}, "
                f"monstreCible={self.monstreCible}, donjonAssocie={self.donjonAssocie}, "
                f"statut={self.statut})")