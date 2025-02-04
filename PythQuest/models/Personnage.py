from models.exceptions import InsufficientFundsError, InventoryFullError, NoSuchItemError, QuestAlreadyAcceptedError, NoActiveQuestError


class Personnage:
    def __init__(self, nom, or_, vie):
        self.nom = nom
        self.or_ = or_
        self.vie = vie

    def gagnerOr(self, or_: int) -> None:
        self.or_ += or_
    
    def perdreOr(self, or_: int) -> None:
        if self.or_ - or_ < 0:
            raise InsufficientFundsError("Vous n'avez pas assez d'or.")
        self.or_ -= or_
        

        
    def perdreVie(self, degats: int) -> bool:
        self.vie -= degats
        if self.vie <= 0:
            self.vie = 0
        
    def estMort(self) -> bool:
        return self.vie == 0
    
    
        
    def getNom(self) -> str:
        return self.nom
    
    def getOr(self) -> int:
        return self.or_
    
    def getVie(self) -> int:
        return self.vie
        
    def __str__(self):
        return (f"Personnage(nom={self.nom}, or_={self.or_}, vie={self.vie})")