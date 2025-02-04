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

    
    def __init__(self, nom, or_, vie, armePossedee:Arme, niveau):
        super().__init__(nom, or_, vie)
        self.armePossedee = armePossedee
        self.niveau = niveau
        
    @staticmethod
    def creerMonstreAleatoire(difficulte, niveauJoueur):
        nom = random.choice(Monstre.PREFIXES) + " " + random.choice(Monstre.SUFFIXES)
        or_ = random.randint(10, 20) * difficulte * niveauJoueur
        vie = random.randint(8, 18) * difficulte//2 * niveauJoueur
        armeMonstre = Arme.creerArme(int(random.randint(2, 5) * difficulte * niveauJoueur))
        monstre = Monstre(nom, or_, vie, armeMonstre, niveauJoueur)
        return monstre
    
    
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
        return f"{self.nom} (lvl {self.niveau}), {self.vie} vie, possédant {self.armePossedee} et {self.or_} or"

    def __str__(self):
        return f"Monstre(nom={self.nom}, vie={self.vie}, or={self.or_}, arme={self.armePossedee}, niveau={self.niveau})"