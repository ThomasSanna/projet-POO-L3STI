from models.Personnage import Personnage
from models.Arme import Arme
import random

class Monstre(Personnage):
    
    PREFIXES = (
        "Zombie", "Goule", "Squelette", "Gobelin", "Orc", "Troll", "Dragon", 
        "Hydre", "Basilic", "Cyclope", "Sphinx", "Minotaure", "Cerberus", "Kraken", 
        "Loup", "Chauve-souris", "Vampire", "Fantôme", "Momie", "Spectre", "Liche", 
        "Golem", "Géant", "Serpent", "Scorpion", "Araignée", "Chimère", "Harpie", 
        "Centaure", "Licorne", "Pégase", "Phénix", "Griffon", "Dragonnet", "Béhémoth", 
        "Banshee", "Démon", "Diablotin", "Succube", "Incube", "Loup-garou", "Elfe", 
        "Nain", "Ogre", "Gnome", "Fée", "Sirène", "Pirate", "Corsaire", "Boucanier", 
        "Voleur", "Assassin", "Mercenaire", "Guerrier", "Chevalier", "Paladin", "Barbare", 
        "Viking", "Samouraï", "Ninja", "Moine", "Mage", "Sorcier", "Enchanteur", "Alchimiste", 
        "Prêtre", "Clerc", "Moine", "Prêtresse", "Clerc", "Sorcière", "Enchanteresse", 
        "Alchimiste", "Prêtresse", "Oracle", "Divinité", "Démon", "Ange"
    )
    
    SUFFIXES = (
        "maudit", "sanguinaire", "affamé", "vorace", "bizarre", "étrange", "volant", "malicieux",
        "sournois", "rusé", "fourbe", "cruel", "sadique", "impitoyable", "inflexible", "implacable",
        "carnivore", "cannibale"
    )

    
    def __init__(self, nom, or_, vie, armePossedee:Arme):
        super().__init__(nom, or_, vie)
        self.armePossedee = armePossedee
        
    @staticmethod
    def creerMonstreAleatoire(difficulte):
        nom = random.choice(Monstre.PREFIXES) + " " + random.choice(Monstre.SUFFIXES)
        or_ = random.randint(10, 20) * difficulte
        vie = random.randint(50, 100) * difficulte
        armeMonstre = Arme.creerArme(random.randint(5, 10) * difficulte)
        monstre = Monstre(nom, or_, vie, armeMonstre)
        return monstre
    
    
    def perdreVie(self, degats: int) -> bool:
        if(self.vie - degats <= 0):
            self.vie = 0
            return False
        self.vie -= degats
        return True
    
    def attaquer(self, combattant:"Combattant") -> bool:
        degats = self.armePossedee.getDegats()
        return combattant.perdreVie(degats)
        
    
    def getArmePossedee(self) -> Arme:
        """
        Retourne l'arme possédée par le monstre.
        
        :return: L'arme possédée par le monstre.
        """
        return self.armePossedee
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return (f"Monstre(nom={self.nom}, or_={self.or_}, vie={self.vie}, armePossedee={self.armePossedee})")