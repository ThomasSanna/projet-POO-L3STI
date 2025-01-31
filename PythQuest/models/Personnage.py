class Personnage:
    def __init__(self, nom, or_, vie):
        self.nom = nom
        self.or_ = or_
        self.vie = vie
        
    def getNom(self) -> str:
        return self.nom
    
    def getOr(self) -> int:
        return self.or_
    
    def getVie(self) -> int:
        return self.vie
        
    def __str__(self):
        return (f"Personnage(nom={self.nom}, or_={self.or_}, vie={self.vie})")