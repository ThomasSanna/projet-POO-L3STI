from models.Personnage import Personnage
from models.Arme import Arme
import random

class Forgeron(Personnage):
    def __init__(self, nom):
        super().__init__(nom, 0, 100)
        self.inventaireArmes = []
        for i in range(random.randint(2, 10)):
            self.forgerArme()
        
    def ajouterArme(self, arme: Arme) -> None:
        self.inventaireArmes.append(arme)
        
    def enleverArme(self, arme: Arme) -> bool:
        if arme in self.inventaireArmes:
            self.inventaireArmes.remove(arme)
            return True
        return False
        
    def forgerArme(self) -> None:
        self.ajouterArme(Arme.creerArmeAleatoire())
        
    def getInventaireArmes(self):
        return self.inventaireArmes
    
    def getNbArmes(self):
        return len(self.inventaireArmes)
    
    def afficherInventaire(self):
        for i, arme in enumerate(self.inventaireArmes):
            print(f"{i + 1}. {arme}")
        print(f"{self.getNbArmes() + 1}. Retour")
        
    def getArmeIndex(self, index: int) -> Arme: # systeme d'erreur à revoir
        return self.inventaireArmes[index]
        
    def __str__(self):
        return (f"Forgeron {self.nom}, {self.getNbArmes()} armes en stock")