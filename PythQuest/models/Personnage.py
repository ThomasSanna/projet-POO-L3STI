class Personnage:
    def __init__(self, nom, or_, vie):
        self.nom = nom
        self.or_ = or_
        self.vie = vie
        
    def __str__(self):
        return (f"Personnage(nom={self.nom}, or_={self.or_}, vie={self.vie})")