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
        self.maxVie = vie
        self.inventairePotions: int = 0
        self.armeEquipee: Arme = Arme("Poings", 0, 5)
        self.inventaireArmes: List[Arme] = []
        self.queteActuelle: Optional[Quete] = None
        self.donjonsExplores: List[Donjon] = []
        self.niveau: int = 1
        self.experience: int = 0
    
    def gagnerExperience(self, exp: int) -> None:
        if exp <= 0:
            raise ValueError("L'expérience gagnée doit être positive.")
        self.experience += exp
        expNiveauSuivant = self.niveau * 100
        print(f"Vous avez gagné {exp} points d'expérience.")
        print(f"Vous avez maintenant {self.experience}/{expNiveauSuivant} points d'expérience.")
        while self.experience >= self.niveau * 100:  # Par exemple, 100 XP par niveau
            self.niveau += 1
            self.experience = self.experience - self.niveau * 100
            self.maxVie = int(self.maxVie * 1.5)
            print(f"Félicitations ! Vous avez atteint le niveau {self.niveau}. Votre vie maximale est maintenant de {self.maxVie}.")
        
    def estMort(self):
        if(self.vie <= 0):
            return True
        return False
    
    def resetApresMort(self):
        print("Vous êtes mort.")
        print(f"Vous perdez {self.or_//1.5} pièces d'or.")
        self.vie = self.maxVie//1.5
        self.perdreOr(self.or_//1.5)
        
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
        
    def gagnerVie(self, vie: int) -> None:
        self.vie += vie
        if self.vie > self.maxVie:
            self.vie = self.maxVie
    
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
        
    def reussiteQuete(self) -> None:
        if self.queteActuelle is None:
            raise NoActiveQuestError("Vous n'avez pas de quête active.")
        self.queteActuelle.queteFinie()
        self.gagnerOr(self.queteActuelle.getRecompenseOr())
        self.gagnerExperience(int((self.queteActuelle.getDifficulte()/1.3) * 30 * self.niveau/1.3))
        self.queteActuelle = None
        
    def battreMonstre(self, monstre: "Monstre", donjon: "Donjon") -> None:
        print(f"Vous avez vaincu {monstre.getNom()} !")
        self.gagnerOr(monstre.getOr())
        self.gagnerExperience(10 * self.niveau*1.3)
        self.ajouterArmeInventaire(monstre.getArmePossedee())
        donjon.supprimerMonstre(monstre)
        try:
            monstreQuete = self.getMonstreQueteActuelle()
            if monstreQuete == monstre:
                self.reussiteQuete()
                print("Vous avez réussi la quête !")
        except NoActiveQuestError:
            raise NoActiveQuestError("Vous n'avez pas de quête active.")
        
    def attaquer(self, monstre: "Monstre") -> None:
        degats = self.armeEquipee.getDegats()
        monstre.perdreVie(degats)
    
    def getInventairePotions(self) -> int:
        return self.inventairePotions
    
    def getArmeEquipee(self) -> Arme:
        return self.armeEquipee
    
    def getNiveau(self) -> int:
        return self.niveau
    
    def getExperience(self) -> int:
        return self.experience
    
    def getInventaireArmes(self) -> List[Arme]:
        return self.inventaireArmes
    
    def getQueteActuelle(self) -> Optional[Quete]:
        return self.queteActuelle
    
    def getMonstreQueteActuelle(self) -> "Monstre":
        if self.queteActuelle is None:
            raise NoActiveQuestError("Vous n'avez pas de quête active.")
        return self.queteActuelle.getMonstreCible()
    
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
        return (f"Combattant(nom={self.nom}, or_={self.or_}, vie={self.vie}/{self.maxVie}, "
                f"niveau={self.niveau}, experience={self.experience}, "
                f"inventairePotions={self.inventairePotions}, armeEquipee={self.armeEquipee}, "
                f"inventaireArmes={self.inventaireArmes}, queteActuelle={self.queteActuelle}, "
                f"donjonExplore={self.donjonsExplores})")
        