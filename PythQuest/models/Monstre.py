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
    
    nbMonstres = 1

    
    def __init__(self, nom: str, piece: int, vie: int, armePossedee: Arme, niveau: int) -> None:
        """
        Initialise un monstre avec un nom, une quantité d'or, des points de vie, une arme possédée et un niveau.

        :param nom: Le nom du monstre.
        :param piece: La quantité d'or possédée par le monstre.
        :param vie: Les points de vie du monstre.
        :param armePossedee: L'arme possédée par le monstre.
        :param niveau: Le niveau du monstre.
        """
        self.id = Monstre.nbMonstres
        Monstre.nbMonstres += 1
        super().__init__(nom, piece, vie)
        self.armePossedee = armePossedee
        self.niveau = niveau
        
    @staticmethod
    def creerMonstreAleatoire(difficulte: int, niveauJoueur: int) -> "Monstre":
        """
        Crée un monstre aléatoire basé sur la difficulté et le niveau du joueur.

        :param difficulte: La difficulté du jeu.
        :param niveauJoueur: Le niveau du joueur.
        :return: Un monstre généré aléatoirement.
        """
        nom = random.choice(Monstre.PREFIXES) + " " + random.choice(Monstre.SUFFIXES)
        piece = random.randint(10, 20) * difficulte * niveauJoueur # Calcule une quantité d'or aléatoire basée sur la difficulté et le niveau du joueur
        vie = random.randint(8, 18) * difficulte // 2 * niveauJoueur # Calcule des points de vie aléatoires basés sur la difficulté et le niveau du joueur
        armeMonstre = Arme.creerArme(int(random.randint(2, 5) * difficulte * niveauJoueur))
        monstre = Monstre(nom, piece, vie, armeMonstre, niveauJoueur)
        return monstre
    
    
    def attaquer(self, combattant: "Combattant") -> bool:
        """
        Attaque un combattant et lui inflige des dégâts.

        :param combattant: Le combattant à attaquer.
        :return: True si le combattant a perdu de la vie, False sinon.
        """
        degats = self.armePossedee.getDegats()
        return combattant.perdreVie(degats)
        
    def getArmePossedee(self) -> Arme:
        """
        Retourne l'arme possédée par le monstre.

        :return: L'arme possédée par le monstre.
        """
        return self.armePossedee
    
    def __repr__(self) -> str:
        """
        Retourne une représentation non ambiguë du monstre.

        :return: Une chaîne de caractères représentant le monstre.
        """
        return f"{self.nom} (lvl {self.niveau}), {self.vie} vie, possédant {self.armePossedee} et {self.piece} or"

    def __str__(self) -> str:
        """
        Retourne une représentation lisible du monstre.

        :return: Une chaîne de caractères représentant le monstre.
        """
        return f"Monstre(nom={self.nom}, vie={self.vie}, or={self.piece}, arme={self.armePossedee}, niveau={self.niveau})"