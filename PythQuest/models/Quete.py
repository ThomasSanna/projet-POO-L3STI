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
        
    def __init__(self, nom, recompenseOr, difficulte, niveauJoueur):
        self.nom = nom
        self.recompenseOr = recompenseOr
        self.difficulte = difficulte
        self.monstreCible =  Monstre.creerMonstreAleatoire(difficulte, niveauJoueur)
        self.donjonAssocie = Donjon.creerDonjonAleatoire(difficulte, self.monstreCible, niveauJoueur)
        self.statut = Quete.STATUT_EN_COURS
        self.niveau = niveauJoueur
        Quete.toutesLesQuetes.append(self)
        
    @staticmethod
    def creerQueteAleatoire(niveauJoueur):
        nom = Quete.PREFIXES + Quete.SUFFIXES[random.randint(0, len(Quete.SUFFIXES) - 1)]
        difficulte = random.randint(1, 5)
        recompenseOr = random.randint(difficulte * 15, difficulte * 35)
        return Quete(nom, recompenseOr, difficulte, niveauJoueur)
    
    @staticmethod
    def afficherToutesLesQuetesEnCours() -> str:
        result = []
        for i, quete in enumerate(Quete.getToutesLesQuetesEnCours()):
            if quete.getStatut() == Quete.STATUT_EN_COURS:
                result.append(f"{i + 1}. {quete}")
        result.append(f"{len(Quete.getToutesLesQuetesEnCours()) + 1}. Retour")
        return "\n".join(result)
        
    def getQueteIndexEnCours(id) -> 'Quete':
        return Quete.getToutesLesQuetesEnCours()[id]
        
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
    
    @staticmethod
    def getToutesLesQuetes():
        return Quete.toutesLesQuetes
    
    @staticmethod
    def getToutesLesQuetesEnCours() -> list['Quete']:
        quetes = []
        for quete in Quete.toutesLesQuetes:
            if quete.getStatut() == Quete.STATUT_EN_COURS:
                quetes.append(quete)
        return quetes
    
    @staticmethod
    def getNbQuetesEnCours():
        return len(Quete.getToutesLesQuetesEnCours())
    
    def __repr__(self):
        return self.__str__()
        
    def __str__(self):
        return f"{self.nom} (lvl {self.niveau}, difficulté {self.difficulte}) : Monstre à tuer : {self.monstreCible.getNom()} dans le {self.donjonAssocie.getNom()}, (récompense : {self.recompenseOr} or) ((statut : {self.statut}))"