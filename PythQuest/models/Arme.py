class Arme:
    """
    Classe représentant une arme avec un nom, une valeur en or et des dégâts.
    """
    
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
    
    def getDegat(self) -> int:
        """
        Retourne les dégâts de l'arme.
        
        :return: Les dégâts de l'arme.
        """
        return self.__degat
        
    def __repr__(self) -> str:
        """
        Retourne une représentation non ambiguë de l'objet.
        
        :return: Une chaîne de caractères représentant l'objet.
        """
        return f"{self.__nom}, {self.__degat} dgts, {self.__valeurOr} or"
        
    def __str__(self) -> str:
        """
        Retourne une représentation lisible de l'objet.
        
        :return: Une chaîne de caractères lisible représentant l'objet.
        """
        return f"Arme(nom={self.__nom}, valeurOr={self.__valeurOr}, degat={self.__degat})"