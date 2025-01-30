from models.Personnage import Personnage
from models.Quete import Quete
from models.Arme import Arme
from models.Donjon import Donjon
from models.Medecin import Medecin
from typing import List, Optional

class Combattant(Personnage):
    
    GAIN_POTION = 15
    
    def __init__(self, nom: str):
        super().__init__(nom, 0, 100)
        self.inventairePotions: int = 0
        self.armeEquipee: Optional[Arme] = None
        self.inventaireArmes: List[Arme] = []
        self.queteActuelle: Optional[Quete] = None
        self.donjonsExplores: List[Donjon] = []
        
    def perdreVie(self, degats: int) -> bool:
        self.vie -= degats
        if self.vie <= 0: # Si le combattant n'a plus de vie, il perd la moitié de son or et sa vie est remise à 100
            self.vie = 100
            self.or_ = self.or_ // 2
            return False
        return True
    
    def gagnerOr(self, or_: int) -> bool:
        self.or_ += or_
        return True
    
    def perdreOr(self, or_: int) -> bool:
        self.or_ -= or_
        if self.or_ < 0:
            self.or_ = 0
            return False
        return True
        
    def gagnerVie(self, vie: int) -> bool:
        self.vie += vie
        if self.vie > 100:
            self.vie = 100
            return False
        return True
            
    def gagnerPotion(self) -> bool:
        self.inventairePotions += 1
        if self.inventairePotions > 5:
            self.inventairePotions = 5
            return False
        return True
    
    def perdrePotion(self) -> bool:
        self.inventairePotions -= 1
        if self.inventairePotions < 0:
            self.inventairePotions = 0
            return False
        return True
    
    def boirePotion(self) -> bool:
        if self.inventairePotions > 0:
            self.gagnerVie(Combattant.GAIN_POTION)
            self.perdrePotion()
            return True
        return False
    
    def ajouterArmeInventaire(self, arme: Arme) -> bool:
        self.inventaireArmes.append(arme)
        return True
        
    def retirerArmeInventaire(self, arme: Arme) -> bool:
        if arme in self.inventaireArmes:
            self.inventaireArmes.remove(arme)
            return True
        return False
    
    def equiperArme(self, arme: Arme) -> bool:
        if arme in self.inventaireArmes:
            if self.armeEquipee is not None: # Remettre l'arme équipée dans l'inventaire si le combattant en a déjà une
                self.ajouterArmeInventaire(self.armeEquipee)
            self.armeEquipee = arme
            self.retirerArmeInventaire(arme)
            return True
        return False
    
    def abandonnerQuete(self) -> bool: # changer le statut de la quête
        self.queteActuelle = None
        return True
    
    def accepterQuete(self, quete: Quete) -> bool: # changer le statut de la quête
        self.queteActuelle = quete
        return True
    
    def explorerDonjon(self, donjon: Donjon) -> bool: # à revoir
        if donjon not in self.donjonsExplores:
            self.donjonsExplores.append(donjon)
            return True
        return False
    
    def entrerBoutique(self) -> bool: # à faire
        return True
    
    def acheterPotion(self, medecin: Medecin) -> bool:
        prixPotion = medecin.prixPotion
        if self.perdreOr(prixPotion):
            self.gagnerPotion()
            medecin.perdrePotion()
            return True
        return False

    def acheterArme(self, forgeron: 'Forgeron', arme: Arme) -> bool:
        if self.perdreOr(arme.getValeurOr()):
            self.ajouterArmeInventaire(arme)
            return True
        return False
    
    def __repr__(self) -> str: # sert à afficher le combattant dans une liste
        return self.nom
    
    def __str__(self) -> str:
        return (f"Combattant(nom={self.nom}, or_={self.or_}, vie={self.vie}, "
                f"inventairePotions={self.inventairePotions}, armeEquipee={self.armeEquipee}, "
                f"inventaireArmes={self.inventaireArmes}, queteActuelle={self.queteActuelle}, "
                f"donjonExplore={self.donjonsExplores})")