from models.Monstre import Monstre
from models.Donjon import Donjon
import random

""" 
Liste de toutes les quetes
Liste de toutes les quetes en cours
Liste de toutes les quetes terminées *
"""

class Quete:

    PREFIXES = "Quête "
    SUFFIXES = (
        "du savant fou", "de la libraire", "interdite",
        "de la montagne", "de la forêt", "du dragon",
        "de l'ombre", "de la lumière", "du guerrier",
        "de la sorcière", "du magicien", "du voleur",
        "du roi", "de la reine", "du prince",
        "de la princesse",
    )
  
    STATUT_EN_COURS = "En cours"
    STATUT_TERMINEE = "Terminée"
    
    toutesLesQuetes = []
  
    def __init__(self, nom, recompenseOr, difficulte, monstreCible, donjonAssocie):
        self.nom = nom
        self.recompenseOr = recompenseOr
        self.difficulte = difficulte
        self.monstreCible = monstreCible
        self.donjonAssocie = donjonAssocie
        self.statut = Quete.STATUT_EN_COURS
        Quete.toutesLesQuetes.append(self)
        
    def __init__(self, nom, recompenseOr, difficulte):
        self.nom = nom
        self.recompenseOr = recompenseOr
        self.difficulte = difficulte
        self.monstreCible =  Monstre.creerMonstreAleatoire(difficulte)
        self.donjonAssocie = Donjon.creerDonjonAleatoire(difficulte, self.monstreCible)
        self.statut = Quete.STATUT_EN_COURS
        Quete.toutesLesQuetes.append(self)
        
    @staticmethod
    def creerQueteAleatoire():
        nom = Quete.PREFIXES + Quete.SUFFIXES[random.randint(0, len(Quete.SUFFIXES) - 1)]
        difficulte = random.randint(1, 5)
        recompenseOr = random.randint(difficulte * 15, difficulte * 35)
        return Quete(nom, recompenseOr, difficulte)
        
    def queteFinie(self):
        self.statut = Quete.STATUT_TERMINEE
        
    def queteEnCours(self):
        self.statut = Quete.STATUT_EN_COURS
        
    def queteAbandonnee(self):
        self.statut = Quete.STATUT_TERMINEE
        
    def getNom(self):
        return self.nom
        
    def getMonstreCible(self):
        return self.monstreCible
    
    def getDonjonAssocie(self):
        return self.donjonAssocie
    
    def getStatut(self):
        return self.statut
    
    def getRecompenseOr(self):
        return self.recompenseOr

    def getDifficulte(self):
        return self.difficulte
    
        
    def __repr__(self):
        return f"{self.description}, {self.recompenseOr} or, {self.monstreCible}, {self.donjonAssocie}, {self.statut}"
        
    def __str__(self):
        return (f"Quete(nom={self.nom}, recompenseOr={self.recompenseOr}, "
                f"monstreCible={self.monstreCible}, donjonAssocie={self.donjonAssocie}, "
                f"statut={self.statut})")