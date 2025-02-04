import random

class Arme:
    """
    Classe représentant une arme avec un nom, une valeur en or et des dégâts.
    """
    
    PREFIXES = (
        ("Épée", 40), ("Hache", 50), ("Dague", 30), ("Arc", 35), ("Lance", 45),
        ("Marteau", 55), ("Bâton", 25), ("Glaive", 60), ("Faux", 65), ("Fleuret", 30),
        ("Katana", 45), ("Gourdin", 20), ("Bouclier", 15), ("Fouet", 25), ("Hallebarde", 55),
        ("Masse", 50), ("Poignard", 35), ("Rapière", 40), ("Sceptre", 30), ("Trident", 50)
    )
    SUFFIXES = (
        ("de Feu", 20), ("de Glace", 20), ("du Dragon", 30), ("des Ombres", 25), ("de Lumière", 20),
        ("de la Nuit", 25), ("du Soleil", 30), ("de l'Aube", 20), ("du Crépuscule", 25), ("de la Tempête", 30),
        ("de la Foudre", 35), ("de la Terre", 20), ("de l'Eau", 20), ("du Vent", 20), ("de l'Esprit", 25),
        ("de la Forêt", 20), ("de la Montagne", 25), ("de l'Océan", 20), ("de la Lune", 20), ("des Étoiles", 25),
        ("du Chaos", 35), ("de l'Ordre", 25), ("de la Mort", 40), ("de la Vie", 20), ("de l'Inconnu", 30),
        ("de l'Ancien Temps", 35), ("du Guerrier", 25), ("du Mage", 20), ("du Voleur", 25), ("du Paladin", 30),
        ("du Barbare", 35), ("du Ranger", 25), ("du Sorcier", 20), ("du Nécromancien", 35), ("du Druide", 25),
        ("de l'Assassin", 30), ("du Chevalier", 25), ("en Acier", 15), ("en Fer", 10), ("en Or", 20),
        ("en Argent", 15), ("en Bronze", 10), ("en Cuivre", 5), ("en Bois", 5), ("en Os", 10),
        ("en Pierre", 10), ("en Cristal", 20), ("en Diamant", 30), ("en Saphir", 25), ("en Rubis", 25),
        ("en Émeraude", 20), ("en Topaze", 15), ("en Améthyste", 20), ("en Opale", 15), ("en Quartz", 10),
        ("en Jade", 20), ("en Mithril", 25), ("en Adamantium", 35), ("en Obsidienne", 30), ("en Verre", 5),
        ("en Plastique", 1)
    )
    ETAT_ARME = (
        ("Cassé", 20), ("Endommagé", 40), ("Usé", 60), ("Solide", 80), ("Neuf", 90)
    )
    
    def __init__(self, nom: str, valeurOr: int, degat: int):
        """
        Initialise une nouvelle arme.
        
        :param nom: Le nom de l'arme.
        :param valeurOr: La valeur en or de l'arme.
        :param degat: Les dégâts de l'arme.
        """
        self.__nom = nom
        self.__valeurOr = valeurOr
        self.__degat = degat
        
    @staticmethod
    def creerArmeAleatoire():
        prefixe, degatsPrefixe = random.choice(Arme.PREFIXES)
        suffixe, degatsSuffixe = random.choice(Arme.SUFFIXES)
        etat, pourcentageDegats = random.choice(Arme.ETAT_ARME)
        degats = int((degatsPrefixe + degatsSuffixe) * (pourcentageDegats / 100))
        plageValeurOr = [degats*5 - 10, degats*5 + 30] # Valeur de l'arme entre degats*2 - 50 et degats*2 + 100
        valeurOr = random.randint(plageValeurOr[0], plageValeurOr[1])
        
        return Arme(f"{prefixe} {suffixe} ({etat})", valeurOr, degats)
    
    @staticmethod
    def creerArme(degats):
        prefixe = random.choice(Arme.PREFIXES)[0]
        suffixe = random.choice(Arme.SUFFIXES)[0]
        plageValeurOr = [degats*3 - 10, degats*3 + 10] # Valeur de l'arme entre degats*2 - 50 et degats*2 + 100
        valeurOr = random.randint(plageValeurOr[0], plageValeurOr[1])
        
        return Arme(f"{prefixe} {suffixe} (Rouillé)", valeurOr, degats//1.5)
    
    
    def getNom(self) -> str:
        """
        Retourne le nom de l'arme.
        
        :return: Le nom de l'arme.
        """
        return self.__nom
    
    def getValeurOr(self) -> int:
        """
        Retourne la valeur en or de l'arme.
        
        :return: La valeur en or de l'arme.
        """
        return self.__valeurOr
    
    def getDegats(self) -> int:
        """
        Retourne les dégâts de l'arme.
        
        :return: Les dégâts de l'arme.
        """
        return self.__degat
    
    def setDegats(self, degat: int) -> None:
        """
        Modifie les dégâts de l'arme.
        
        :param degat: Les nouveaux dégâts de l'arme.
        """
        self.__degat = degat
        
    def __repr__(self) -> str:
        """
        Retourne une représentation non ambiguë de l'objet.
        
        :return: Une chaîne de caractères représentant l'objet.
        """
        return self.__str__()
        
    def __str__(self) -> str:
        """
        Retourne une représentation lisible de l'objet.
        
        :return: Une chaîne de caractères lisible représentant l'objet.
        """
        return f"{self.__nom} : {self.__degat} dgts, {self.__valeurOr} or"