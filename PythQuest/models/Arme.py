import random
from PIL import Image 
from .ArmesImages import genererArme 
from dao.ArmeDAO import ArmeDAO

class Arme:
    """
    Classe représentant une arme avec un nom, une valeur en or, des dégâts et une image.
    
    Attributes:
        PREFIXES (tuple): Les préfixes possibles pour les noms d'armes et leurs dégâts associés.
        SUFFIXES (tuple): Les suffixes possibles pour les noms d'armes et leurs dégâts associés.
        ETAT_ARME (tuple): Les états possibles des armes et leurs pourcentages de dégâts associés.
        __nom (str): Le nom de l'arme.
        __valeurOr (int): La valeur en or de l'arme.
        __degat (int): Les dégâts de l'arme.
        __image (Image.Image): L'image de l'arme.
    """
    
    PREFIXES = (
        ("Épée", 40), ("Hache", 50), ("Dague", 30), ("Lance", 45),
        ("Marteau", 55), ("Bâton", 25), ("Glaive", 60), ("Faux", 65), ("Fleuret", 30),
        ("Katana", 45), ("Gourdin", 20), ("Fouet", 25), ("Hallebarde", 55),
        ("Masse", 50), ("Poignard", 35), ("Trident", 50)
    )

    SUFFIXES = (
        ("de Feu", 20),  
        ("du Dragon", 30),  
        ("de Glace", 20),  
        ("des Ombres", 25),  
        ("de la Nuit", 25),  
        ("du Chaos", 35),  
        ("de la Mort", 40),  
        ("de Lumière", 20),  
        ("du Soleil", 30),  
        ("de la Lune", 20),  
        ("des Étoiles", 25),  
        ("de la Vie", 20),  
        ("de la Tempête", 30),  
        ("du Vent", 20),  
        ("de la Foudre", 35),  
        ("de l'Eau", 20),  
        ("de l'Océan", 20),  
        ("de l'Esprit", 25),  
        ("de la Forêt", 20),  
        ("en Bois", 5),  
        ("du Guerrier", 25),  
        ("du Mage", 20),  
        ("du Voleur", 25),  
        ("du Paladin", 30),  
        ("du Barbare", 35),  
        ("du Ranger", 25),  
        ("du Sorcier", 20),  
        ("du Nécromancien", 35),  
        ("du Druide", 25),  
        ("de l'Assassin", 30),  
        ("du Chevalier", 25),  
        ("en Argent", 15),  
        ("en Adamantium", 35),  
        ("en Acier", 15),  
        ("en Fer", 10),  
        ("en Cuivre", 5),  
        ("en Os", 10),  
        ("en Quartz", 10),  
        ("en Pierre", 10),  
        ("en Cristal", 20),  
        ("en Diamant", 30),  
        ("en Topaze", 15), 
        ("en Opale", 15),  
        ("en Saphir", 25),  
        ("en Rubis", 25),  
        ("en Émeraude", 20),  
        ("en Jade", 20),  
        ("en Améthyste", 20),  
        ("en Obsidienne", 30),  
        ("en Or", 20),  
        ("en Bronze", 10)
    )
    
    ETAT_ARME = (
        ("Cassé", 20), ("Endommagé", 40), ("Usé", 60), ("Solide", 80), ("Neuf", 90)
    )
    
    # Attributs de classe
    lstArmes = []
    nbArmes = 0
    
    def __init__(self, nom: str, valeurOr: int, degat: int, image: Image.Image=None, id: int=None) -> None:
        """
        Initialise une nouvelle arme.

        :param nom: Le nom de l'arme.
        :param valeurOr: La valeur en or de l'arme.
        :param degat: Les dégâts de l'arme.
        :param image: L'image de l'arme.
        :param id: L'identifiant de l'arme. Si None, un nouvel identifiant sera généré.
        """
        self.__nom = nom
        self.__valeurOr = valeurOr
        self.__degat = degat
        self.__image = image
        self.__id = id if id is not None else Arme.nbArmes
        # Le nombre d'arme est égal à l'id le plus grand parmi les armes créées + 1
        Arme.nbArmes = id + 1 if id is not None and (id+1)>=Arme.nbArmes else Arme.nbArmes + 1
        self.dao = ArmeDAO()
        Arme.lstArmes.append(self)
        
    @staticmethod
    def creerArmeAleatoire() -> "Arme":
        """
        Crée une arme aléatoire avec un nom, une valeur en or, des dégâts et une image.

        :return: Une instance de la classe Arme.
        """
        prefixe, degatsPrefixe = random.choice(Arme.PREFIXES)
        suffixe, degatsSuffixe = random.choice(Arme.SUFFIXES)
        etat, pourcentageDegats = random.choice(Arme.ETAT_ARME)
        degats = int((degatsPrefixe + degatsSuffixe) * (pourcentageDegats / 100))
        plageValeurOr = [degats*5 - 10, degats*5 + 30] # Valeur de l'arme entre degats*3 - 10 et degats*3 + 10
        valeurOr = random.randint(plageValeurOr[0], plageValeurOr[1])
        
        # Générer l'image de l'arme
        image = genererArme(prefixe, suffixe, etat, degats)
        
        return Arme(f"{prefixe} {suffixe} ({etat})", valeurOr, degats, image)
    
    @staticmethod
    def creerArme(degats: int) -> "Arme":
        """
        Crée une arme avec des dégâts spécifiés.

        :param degats: Les dégâts de l'arme.
        :return: Une instance de la classe Arme.
        """
        prefixe = random.choice(Arme.PREFIXES)[0]
        suffixe = random.choice(Arme.SUFFIXES)[0]
        plageValeurOr = [degats*3 - 10, degats*3 + 10] # Valeur de l'arme entre degats*3 - 10 et degats*3 + 10
        valeurOr = random.randint(plageValeurOr[0], plageValeurOr[1])
        
        # Générer l'image de l'arme
        image = genererArme(prefixe, suffixe, "Rouillé", degats)
        
        return Arme(f"{prefixe} {suffixe} (Rouillé)", valeurOr, degats//1.5, image)
    
    @staticmethod
    def recupererArmes(combattant: 'Combattant') -> list:
        """
        Récupère toutes les armes d'un combattant à partir de la base de données.

        :param idCombattant: ID du combattant dont on veut récupérer les armes.
        :return: Liste des armes du combattant.
        """
        armes = ArmeDAO.recupAllArmes(combattant.getId())
        for arme in armes:
            image = Arme.getImageFromBin(arme["image"])
            armeObj = Arme(arme["nom"], arme["valeurOr"], arme["degat"], image, arme["id"])
            if(arme["inventaire_combattant_id"]):
                combattant.ajouterArmeInventaire(armeObj)
        return
    
    def save(self, combattant: 'Combattant') -> None:
        """
        Enregistre l'arme dans la base de données.
        """
        self.dao.saveArme(self.toDict(combattant))
        
    def toDict(self, combattant: 'Combattant') -> dict:
        """
        Retourne un dictionnaire représentant l'objet.

        :return: Un dictionnaire représentant l'objet.
        """
        return {
            "id": self.__id,
            "nom": self.__nom,
            "valeurOr": self.__valeurOr,
            "degat": self.__degat,
            "image": self.__image.tobytes() if self.__image else None,
            "imageBin": self.getImageBin(),
            "inventaire_combattant_id": combattant.getId() if combattant.armeDansInventaire(self) else None,
            "combattant_id": combattant.getId()
            }
        
    @staticmethod
    def getAllArmes() -> list:
        """
        Retourne la liste de toutes les armes créées.

        :return: La liste des armes.
        """
        return Arme.lstArmes
    
    @staticmethod
    def getArmeById(id: int) -> "Arme":
        """
        Retourne l'arme correspondant à l'identifiant spécifié.

        :param id: L'identifiant de l'arme.
        :return: L'arme correspondante.
        """
        for arme in Arme.lstArmes:
            if arme.getId() == id:
                return arme
        return None
    
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
    
    def getImage(self) -> Image.Image:
        """
        Retourne l'image de l'arme.

        :return: L'image de l'arme.
        """
        return self.__image
    
    def setDegats(self, degat: int) -> None:
        """
        Modifie les dégâts de l'arme.

        :param degat: Les nouveaux dégâts de l'arme.
        """
        self.__degat = degat
        
    def getId(self) -> int:
        """
        Retourne l'identifiant de l'arme.

        :return: L'identifiant de l'arme.
        """
        return self.__id
    
    def getImageBin(self) -> Image.Image:
        """
        Retourne l'image de l'arme sous forme binaire.

        :return: L'image de l'arme sous forme binaire.
        """
        return self.__image.tobytes() if self.__image else None
    
    @staticmethod
    def getImageFromBin(imageBin: bytes) -> Image.Image:
        """
        Retourne l'image de l'arme à partir de sa représentation binaire.

        :param imageBin: L'image binaire.
        :return: L'image de l'arme.
        """
        return Image.frombytes("RGBA", (16, 16), imageBin) if imageBin else None
        
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