from models.Personnage import Personnage
from models.Quete import Quete
from models.Arme import Arme
from models.Donjon import Donjon
from typing import List, Optional
from models.exceptions import InsufficientFundsError, InventoryFullError, NoSuchItemError, QuestAlreadyAcceptedError, NoActiveQuestError
class Combattant(Personnage):
    
    GAIN_POTION = 15
    NB_POTION_MAX = 10
    
    def __init__(self, nom: str, or_: int = 0, vie: int = 100):
        super().__init__(nom, or_, vie)
        self.inventairePotions: int = 0
        self.armeEquipee: Optional[Arme] = None
        self.inventaireArmes: List[Arme] = []
        self.queteActuelle: Optional[Quete] = None
        self.donjonsExplores: List[Donjon] = []
    
    def gagnerOr(self, or_: int) -> None:
        self.or_ += or_
    
    def perdreOr(self, or_: int) -> None:
        if self.or_ - or_ < 0:
            raise InsufficientFundsError("Vous n'avez pas assez d'or.")
        self.or_ -= or_
        
    def gagnerVie(self, vie: int) -> None:
        self.vie += vie
        if self.vie > 100:
            self.vie = 100

    def perdreVie(self, degats: int) -> None:
        self.vie -= degats
        if self.vie <= 0:
            self.vie = 100
            self.or_ = self.or_ // 2
            
    def gagnerPotion(self) -> None:
        self.inventairePotions += 1
        if self.inventairePotions > Combattant.NB_POTION_MAX:
            self.inventairePotions = Combattant.NB_POTION_MAX
            raise InventoryFullError("L'inventaire de potion est au maximum (5).")
    
    def perdrePotion(self) -> None:
        if self.inventairePotions <= 0:
            raise NoSuchItemError("Vous n'avez plus de potion.")
        self.inventairePotions -= 1
    
    def boirePotion(self) -> None:
        if self.inventairePotions > 0:
            self.gagnerVie(Combattant.GAIN_POTION)
            self.perdrePotion()
        else:
            raise NoSuchItemError("Vous n'avez plus de potion.")
    
    def ajouterArmeInventaire(self, arme: Arme) -> None:
        self.inventaireArmes.append(arme)
        
    def retirerArmeInventaire(self, arme: Arme) -> None:
        if arme not in self.inventaireArmes:
            raise NoSuchItemError("L'arme n'est pas dans l'inventaire.")
        self.inventaireArmes.remove(arme)
    
    def equiperArme(self, arme: Arme) -> None:
        if arme not in self.inventaireArmes:
            raise NoSuchItemError("L'arme n'est pas dans l'inventaire.")
        if self.armeEquipee is not None:
            self.ajouterArmeInventaire(self.armeEquipee)
        self.armeEquipee = arme
        self.retirerArmeInventaire(arme)
    
    def abandonnerQuete(self) -> None:
        if self.queteActuelle is None:
            raise NoActiveQuestError("Vous n'avez pas de quête active.")
        self.queteActuelle.queteAbandonnee()
        self.queteActuelle = None
    
    def accepterQuete(self, quete: Quete) -> None:
        if self.queteActuelle is not None:
            raise QuestAlreadyAcceptedError("Une quête est déjà en cours.")
        self.queteActuelle = quete
        self.queteActuelle.queteEnCours()
    
    def explorerDonjon(self, donjon: Donjon) -> None:
        if donjon not in self.donjonsExplores:
            self.donjonsExplores.append(donjon)
    
    def entrerBoutique(self) -> None:
        pass
    
    def acheterPotion(self, medecin: "Medecin") -> None:
        prixPotion = medecin.getPrixPotion()
        if self.or_ < prixPotion:
            raise InsufficientFundsError("Vous n'avez pas assez d'or pour acheter une potion.")
        if medecin.getStockPotions() <= 0:
            raise NoSuchItemError("Le médecin n'a plus de potions en stock.")
        if self.inventairePotions > Combattant.NB_POTION_MAX:
            raise InventoryFullError("Votre inventaire de potions est plein.")
        
        self.perdreOr(prixPotion)
        self.gagnerPotion()
        medecin.perdrePotion()

    def acheterArme(self, forgeron: 'Forgeron', arme: Arme) -> None:
        self.perdreOr(arme.getValeurOr())
        self.ajouterArmeInventaire(arme)
        forgeron.enleverArme(arme)
    
    def getInventairePotions(self) -> int:
        return self.inventairePotions
    
    def getArmeEquipee(self) -> Optional[Arme]:
        return self.armeEquipee
    
    def getInventaireArmes(self) -> List[Arme]:
        return self.inventaireArmes
    
    def getQueteActuelle(self) -> Optional[Quete]:
        return self.queteActuelle
    
    def getDonjonsExplores(self) -> List[Donjon]:
        return self.donjonsExplores
    
    def getNbArmesInventaire(self) -> int:
        return len(self.inventaireArmes)
    
    def getArmeIndexInventaire(self, index: int) -> Arme:
        if index < 0 or index >= len(self.inventaireArmes):
            raise IndexError("Weapon index out of range.")
        return self.inventaireArmes[index]
    
    def afficherArmes(self) -> None:
        print("Arme portée :", self.armeEquipee)
        print("Armes dans l'inventaire :")
        for i, arme in enumerate(self.inventaireArmes):
            print(f"{i + 1}. {arme}")
        print(f"{self.getNbArmesInventaire() + 1}. Retour")
    
    def __repr__(self) -> str:
        return self.nom
    
    def __str__(self) -> str:
        return (f"Combattant(nom={self.nom}, or_={self.or_}, vie={self.vie}, "
                f"inventairePotions={self.inventairePotions}, armeEquipee={self.armeEquipee}, "
                f"inventaireArmes={self.inventaireArmes}, queteActuelle={self.queteActuelle}, "
                f"donjonExplore={self.donjonsExplores})")