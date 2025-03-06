from models.Personnage import Personnage
from models.Quete import Quete
from models.Arme import Arme
from models.Donjon import Donjon
from typing import List, Optional
from models.exceptions import InsufficientFundsError, InventoryFullError, NoSuchItemError, QuestAlreadyAcceptedError, NoActiveQuestError

class Combattant(Personnage):
    """Classe représentant un combattant, héritant de Personnage, avec des fonctionnalités de combat et de gestion d'inventaire."""

    GAIN_POTION: int = 15  # Quantité de vie gagnée par potion
    NB_POTION_MAX: int = 10  # Nombre maximum de potions dans l'inventaire

    def __init__(self, nom: str, piece: int = 0, vie: int = 100) -> None:
        """
        Initialise un nouveau Combattant avec le nom, l'or et la vie spécifiés.

        :param nom: Le nom du combattant.
        :param piece: La quantité d'or initiale du combattant. Par défaut 0.
        :param vie: La vie initiale du combattant. Par défaut 100.
        """
        super().__init__(nom, piece, vie)
        self.maxVie: int = vie
        self.inventairePotions: int = 0
        self.armeEquipee: Arme = Arme("Poings", 0, 5)
        self.inventaireArmes: List[Arme] = []
        self.queteActuelle: Optional[Quete] = None
        self.donjonsExplores: List[Donjon] = []
        self.niveau: int = 1
        self.experience: int = 0

    def gagnerExperience(self, exp: int) -> List[str]:
        """
        Permet au combattant de gagner de l'expérience.

        :param exp: La quantité d'expérience à gagner. Doit être positive.
        :raises ValueError: Si exp est négatif ou nul.
        :return: Liste des messages à afficher.
        """
        messages = []
        if exp <= 0:
            raise ValueError("L'expérience gagnée doit être positive.")
        self.experience += exp
        expNiveauSuivant = self.niveau * 100
        messages.append(f"Vous avez gagné {exp} points d'expérience.")
        messages.append(f"Vous avez maintenant {self.experience}/{expNiveauSuivant} points d'expérience.")
        while self.experience >= self.niveau * 100:
            self.experience -= self.niveau * 100
            self.niveau += 1
            self.maxVie = int(self.maxVie + 100)
            messages.append(f"Félicitations ! Vous avez atteint le niveau {self.niveau}. Votre vie maximale est maintenant de {self.maxVie}.")
        return messages

    def estMort(self) -> bool:
        """
        Vérifie si le combattant est mort.

        :return: True si la vie du combattant est inférieure ou égale à 0, False sinon.
        """
        return self.vie <= 0

    def resetApresMort(self) -> List[str]:
        """
        Réinitialise le combattant après sa mort.

        Le combattant perd la moitié de son or et sa vie est réinitialisée à la moitié de sa vie maximale.
        :return: Liste des messages à afficher.
        """
        messages = []
        messages.append("Vous êtes mort.")
        messages.append(f"Vous perdez {self.piece // 1.5} pièces d'or.")
        self.vie = self.maxVie // 1.5
        self.perdreOr(self.piece // 1.5)
        return messages

    def gagnerPotion(self) -> None:
        """
        Ajoute une potion à l'inventaire du combattant.

        :raises InventoryFullError: Si l'inventaire de potions est déjà au maximum.
        """
        self.inventairePotions += 1
        if self.inventairePotions > Combattant.NB_POTION_MAX:
            self.inventairePotions = Combattant.NB_POTION_MAX
            raise InventoryFullError("L'inventaire de potion est au maximum (5).")

    def perdrePotion(self) -> None:
        """
        Retire une potion de l'inventaire du combattant.

        :raises NoSuchItemError: Si l'inventaire de potions est vide.
        """
        if self.inventairePotions <= 0:
            raise NoSuchItemError("Vous n'avez plus de potion.")
        self.inventairePotions -= 1

    def boirePotion(self) -> None:
        """
        Permet au combattant de boire une potion pour gagner de la vie.

        :raises NoSuchItemError: Si l'inventaire de potions est vide.
        """
        if self.inventairePotions > 0:
            self.gagnerVie(Combattant.GAIN_POTION)
            self.perdrePotion()
        else:
            raise NoSuchItemError("Vous n'avez plus de potion.")

    def gagnerVie(self, vie: int) -> None:
        """
        Augmente la vie du combattant.

        :param vie: La quantité de vie à gagner.
        """
        self.vie += vie
        if self.vie > self.maxVie:
            self.vie = self.maxVie

    def ajouterArmeInventaire(self, arme: Arme) -> None:
        """
        Ajoute une arme à l'inventaire du combattant.

        :param arme: L'arme à ajouter.
        """
        self.inventaireArmes.append(arme)

    def retirerArmeInventaire(self, arme: Arme) -> None:
        """
        Retire une arme de l'inventaire du combattant.

        :param arme: L'arme à retirer.
        :raises NoSuchItemError: Si l'arme n'est pas dans l'inventaire.
        """
        if arme not in self.inventaireArmes:
            raise NoSuchItemError("L'arme n'est pas dans l'inventaire.")
        self.inventaireArmes.remove(arme)

    def equiperArme(self, arme: Arme) -> None:
        """
        Équipe une arme de l'inventaire.

        :param arme: L'arme à équiper.
        :raises NoSuchItemError: Si l'arme n'est pas dans l'inventaire.
        """
        if arme not in self.inventaireArmes:
            raise NoSuchItemError("L'arme n'est pas dans l'inventaire.")
        if self.armeEquipee is not None:
            self.ajouterArmeInventaire(self.armeEquipee)
        self.armeEquipee = arme
        self.retirerArmeInventaire(arme)

    def abandonnerQuete(self) -> None:
        """
        Abandonne la quête actuelle.

        :raises NoActiveQuestError: Si aucune quête n'est active.
        """
        if self.queteActuelle is None:
            raise NoActiveQuestError("Vous n'avez pas de quête active.")
        self.queteActuelle.queteAbandonnee()
        self.queteActuelle = None

    def accepterQuete(self, quete: Quete) -> None:
        """
        Accepte une nouvelle quête.

        :param quete: La quête à accepter.
        :raises QuestAlreadyAcceptedError: Si une quête est déjà en cours.
        """
        if self.queteActuelle is not None:
            raise QuestAlreadyAcceptedError("Une quête est déjà en cours.")
        self.queteActuelle = quete
        self.queteActuelle.queteEnCours()

    def explorerDonjon(self, donjon: Donjon) -> None:
        """
        Ajoute un donjon à la liste des donjons explorés.

        :param donjon: Le donjon à ajouter.
        """
        if donjon not in self.donjonsExplores:
            self.donjonsExplores.append(donjon)

    def entrerBoutique(self) -> None:
        """
        Permet au combattant d'entrer dans une boutique.

        Cette méthode est actuellement vide et doit être implémentée.
        """
        pass

    def acheterPotion(self, medecin: "Medecin") -> None:
        """
        Achète une potion à un médecin.

        :param medecin: Le médecin auprès duquel acheter la potion.
        :raises InsufficientFundsError: Si le combattant n'a pas assez d'or.
        :raises NoSuchItemError: Si le médecin n'a plus de potions en stock.
        :raises InventoryFullError: Si l'inventaire de potions du combattant est plein.
        """
        prixPotion = medecin.getPrixPotion()
        if self.piece < prixPotion:
            raise InsufficientFundsError("Vous n'avez pas assez d'or pour acheter une potion.")
        if medecin.getStockPotions() <= 0:
            raise NoSuchItemError("Le médecin n'a plus de potions en stock.")
        if self.inventairePotions >= Combattant.NB_POTION_MAX:  # Correction ici
            raise InventoryFullError("Votre inventaire de potions est plein.")
        self.perdreOr(prixPotion)
        self.gagnerPotion()
        medecin.perdrePotion()

    def acheterArme(self, forgeron: "Forgeron", arme: Arme) -> None:
        """
        Achète une arme à un forgeron.

        :param forgeron: Le forgeron auprès duquel acheter l'arme.
        :param arme: L'arme à acheter.
        """
        self.perdreOr(arme.getValeurOr())
        self.ajouterArmeInventaire(arme)
        forgeron.enleverArme(arme)

    def reussiteQuete(self) -> None:
        """
        Marque la quête actuelle comme réussie et accorde les récompenses.

        :raises NoActiveQuestError: Si aucune quête n'est active.
        """
        if self.queteActuelle is None:
            raise NoActiveQuestError("Vous n'avez pas de quête active.")
        self.queteActuelle.queteFinie()
        messages = []
        messages.append("Félicitations ! Vous avez terminé la ", self.queteActuelle.getNom())
        messages.append(f"Vous avez gagné {self.queteActuelle.getRecompenseOr()} pièces d'or.")
        self.gagnerOr(self.queteActuelle.getRecompenseOr())
        self.gagnerExperience(int((self.queteActuelle.getDifficulte() / 1.3) * 30 * self.niveau / 1.3))
        self.queteActuelle = None
        return messages

    def battreMonstre(self, monstre: "Monstre", donjon: "Donjon") -> List[str]:
        """
        Gère les actions après avoir battu un monstre.

        :param monstre: Le monstre vaincu.
        :param donjon: Le donjon dans lequel le monstre a été vaincu.
        :raises NoActiveQuestError: Si aucune quête n'est active et que le monstre est lié à une quête.
        :return: Liste des messages à afficher.
        """
        messages = []
        messages.append(f"Vous avez vaincu {monstre.getNom()} !")
        messages.append(f"Vous avez gagné {monstre.getOr()} pièces d'or.")
        self.gagnerOr(monstre.getOr())
        messages.extend(self.gagnerExperience(int(10 * self.niveau * 1.3)))  # Typage explicite pour int
        self.ajouterArmeInventaire(monstre.getArmePossedee())
        messages.append(f"Vous avez obtenu {monstre.getArmePossedee()}.")
        donjon.supprimerMonstre(monstre)
        try:
            monstreQuete = self.getMonstreQueteActuelle()
            if monstreQuete == monstre:
                messages.extend(self.reussiteQuete())
        except NoActiveQuestError:
            pass
        return messages

    def attaquer(self, monstre: "Monstre") -> None:
        """
        Attaque un monstre avec l'arme équipée.

        :param monstre: Le monstre à attaquer.
        """
        degats = self.armeEquipee.getDegats()
        monstre.perdreVie(degats)

    def getInventairePotions(self) -> int:
        """
        Retourne le nombre de potions dans l'inventaire.

        :return: Le nombre de potions.
        """
        return self.inventairePotions

    def getArmeEquipee(self) -> Arme:
        """
        Retourne l'arme actuellement équipée.

        :return: L'arme équipée.
        """
        return self.armeEquipee

    def getNiveau(self) -> int:
        """
        Retourne le niveau actuel du combattant.

        :return: Le niveau.
        """
        return self.niveau

    def getExperience(self) -> int:
        """
        Retourne l'expérience actuelle du combattant.

        :return: L'expérience.
        """
        return self.experience

    def getInventaireArmes(self) -> List[Arme]:
        """
        Retourne la liste des armes dans l'inventaire.

        :return: La liste des armes.
        """
        return self.inventaireArmes

    def getQueteActuelle(self) -> Optional[Quete]:
        """
        Retourne la quête actuellement active.

        :return: La quête active ou None si aucune quête n'est active.
        """
        return self.queteActuelle

    def getMonstreQueteActuelle(self) -> "Monstre":
        """
        Retourne le monstre cible de la quête actuelle.

        :return: Le monstre cible.
        :raises NoActiveQuestError: Si aucune quête n'est active.
        """
        if self.queteActuelle is None:
            raise NoActiveQuestError("Vous n'avez pas de quête active.")
        return self.queteActuelle.getMonstreCible()

    def getDonjonsExplores(self) -> List[Donjon]:
        """
        Retourne la liste des donjons explorés.

        :return: La liste des donjons explorés.
        """
        return self.donjonsExplores

    def getNbArmesInventaire(self) -> int:
        """
        Retourne le nombre d'armes dans l'inventaire.

        :return: Le nombre d'armes.
        """
        return len(self.inventaireArmes)

    def getArmeIndexInventaire(self, index: int) -> Arme:
        """
        Retourne l'arme à l'index spécifié dans l'inventaire.

        :param index: L'index de l'arme.
        :return: L'arme à l'index spécifié.
        :raises IndexError: Si l'index est hors de portée.
        """
        if index < 0 or index >= len(self.inventaireArmes):
            raise IndexError("Weapon index out of range.")
        return self.inventaireArmes[index]

    def afficherArmes(self) -> str:
        """
        Retourne une représentation textuelle des armes du combattant.

        :return: Une chaîne de caractères représentant les armes.
        """
        result = f"Arme portée : {self.armeEquipee}\n"
        result += "Armes dans l'inventaire :\n"
        for i, arme in enumerate(self.inventaireArmes):
            result += f"{i + 1}. {arme}\n"
        result += f"{self.getNbArmesInventaire() + 1}. Retour\n"
        return result

    def __repr__(self) -> str:
        """
        Retourne une représentation formelle du combattant.

        :return: Une chaîne de caractères représentant le combattant.
        """
        return self.nom

    def __str__(self) -> str:
        """
        Retourne une représentation détaillée du combattant.

        :return: Une chaîne de caractères représentant le combattant.
        """
        return (f"Combattant(nom={self.nom}, piece={self.piece}, vie={self.vie}/{self.maxVie}, "
                f"niveau={self.niveau}, experience={self.experience}, "
                f"inventairePotions={self.inventairePotions}, armeEquipee={self.armeEquipee}, "
                f"inventaireArmes={self.inventaireArmes}, queteActuelle={self.queteActuelle}, "
                f"donjonExplore={self.donjonsExplores})")