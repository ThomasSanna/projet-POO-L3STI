from models.Personnage import Personnage
from models.Arme import Arme
import random

class Forgeron(Personnage):
    """
    Classe représentant un forgeron, qui peut créer et vendre des armes.

    Attributs:
        nom (str): Nom du forgeron
        inventaireArmes (List[Arme]): Liste des armes dans l'inventaire du forgeron
    """

    def __init__(self, nom: str):
        """
        Initialise un forgeron avec un nom et un inventaire d'armes aléatoire.

        :param nom: Le nom du forgeron.
        """
        super().__init__(nom, 0, 100)
        self.inventaireArmes = []
        for _ in range(random.randint(2, 5)):
            self.forgerArme()
        
    def ajouterArme(self, arme: Arme) -> None:
        """
        Ajoute une arme à l'inventaire du forgeron.

        :param arme: L'arme à ajouter.
        """
        self.inventaireArmes.append(arme)
        
    def enleverArme(self, arme: Arme) -> bool:
        """
        Enlève une arme de l'inventaire du forgeron.

        :param arme: L'arme à enlever.
        :return: True si l'arme a été enlevée, False sinon.
        """
        if arme in self.inventaireArmes:
            self.inventaireArmes.remove(arme)
            return True
        return False
        
    def forgerArme(self) -> None:
        """
        Crée une arme aléatoire et l'ajoute à l'inventaire du forgeron.
        """
        self.ajouterArme(Arme.creerArmeAleatoire())
        
    def getInventaireArmes(self) -> list[Arme]:
        """
        Retourne l'inventaire des armes du forgeron.

        :return: Une liste d'armes.
        """
        return self.inventaireArmes
    
    def getNbArmes(self) -> int:
        """
        Retourne le nombre d'armes dans l'inventaire du forgeron.

        :return: Le nombre d'armes.
        """
        return len(self.inventaireArmes)
    
    def afficherInventaire(self) -> str:
        """
        Renvoie une chaîne de caractères représentant l'inventaire des armes du forgeron.
        """
        inventaireStr = ""
        for i, arme in enumerate(self.inventaireArmes):
            inventaireStr += f"{i + 1}. {arme}\n"
        inventaireStr += f"{self.getNbArmes() + 1}. Retour"
        return inventaireStr
        
    def getArmeIndex(self, index: int) -> Arme:
        """
        Retourne l'arme à l'index spécifié dans l'inventaire.

        :param index: L'index de l'arme.
        :return: L'arme à l'index spécifié.
        """
        return self.inventaireArmes[index]
    
    def getInventaireArmes(self) -> list[Arme]:
        """
        Retourne l'inventaire des armes du forgeron.

        :return: Une liste d'armes.
        """
        return self.inventaireArmes
        
    def __str__(self) -> str:
        """
        Retourne une représentation lisible du forgeron.

        :return: Une chaîne de caractères représentant le forgeron.
        """
        return f"Forgeron {self.nom}, {self.getNbArmes()} armes en stock"