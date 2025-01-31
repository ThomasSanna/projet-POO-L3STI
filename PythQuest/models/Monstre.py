from models.Personnage import Personnage
from models.Arme import Arme
import random

class Monstre(Personnage):
    def __init__(self, nom, or_, vie, armePossedee):
        super().__init__(nom, or_, vie)
        self.armePossedee = armePossedee
        
    @staticmethod
    def creerMonstreAleatoire(difficulte):
        nom = f"Monstre_{random.randint(1, 1000)}"
        or_ = random.randint(10, 20) * difficulte
        vie = random.randint(50, 100) * difficulte
        armeMonstre = Arme.creerArme(random.randint(5, 10) * difficulte)
        monstre = Monstre(nom, or_, vie, armeMonstre)
        return monstre
    
    def getArmePossedee(self) -> Arme:
        """
        Retourne l'arme possédée par le monstre.
        
        :return: L'arme possédée par le monstre.
        """
        return self.armePossedee
    
    def getNom(self) -> str:
        """
        Retourne le nom du monstre.
        
        :return: Le nom du monstre.
        """
        return self.nom
    
    def getOr(self) -> int:
        """
        Retourne l'or du monstre.
        
        :return: L'or du monstre.
        """
        return self.or_
        
    def __str__(self):
        return (f"Monstre(nom={self.nom}, or_={self.or_}, vie={self.vie}, armePossedee={self.armePossedee})")