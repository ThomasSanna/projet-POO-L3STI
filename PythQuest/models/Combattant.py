from dao.CombattantDAO import CombattantDAO
from models.Personnage import Personnage
from models.Quete import Quete
from models.Arme import Arme
from models.Donjon import Donjon
from typing import List, Optional
from models.exceptions import InsufficientFundsError, InventoryFullError, NoSuchItemError, QuestAlreadyAcceptedError, NoActiveQuestError

class Combattant(Personnage):
    """
    Classe représentant un combattant, héritant de Personnage, avec des fonctionnalités de combat et de gestion d'inventaire.
    
    Attributs:
        maxVie (int): La vie maximale du combattant.
        inventairePotions (int): Le nombre de potions dans l'inventaire.
        armeEquipee (Arme): L'arme actuellement équipée.
        inventaireArmes (List[Arme]): La liste des armes dans l'inventaire.
        queteActuelle (Optional[Quete]): La quête actuellement active.
        donjonsExplores (List[Donjon]): La liste des donjons explorés.
        niveau (int): Le niveau du combattant. Une augmentation de niveau augmente la vie maximale, mais aussi la force des monstres dans le futur.
        experience (int): L'expérience du combattant. Un certain nombre d'expérience est nécessaire pour passer au niveau suivant.
    """
    

    GAIN_POTION: int = 15  # Quantité de vie gagnée par potion
    NB_POTION_MAX: int = 10  # Nombre maximum de potions dans l'inventaire

    def __init__(self, id: int, nom: str, piece: int = 0, vie: int = 100, maxVie: int = 100, 
                 inventairePotions: int = 0, niveau: int = 1, experience: int = 0, armeEquipee: Arme = Arme("Poings", 0, 5), 
                 queteActuelle: Optional[Quete] = None) -> None:
        """
        Initialise un nouveau Combattant avec les attributs spécifiés.

        :param nom: Le nom du combattant.
        :param piece: La quantité d'or initiale du combattant. Par défaut 0.
        :param vie: La vie initiale du combattant. Par défaut 100.
        :param maxVie: La vie maximale du combattant. Par défaut 100.
        :param inventairePotions: Le nombre de potions dans l'inventaire. Par défaut 0.
        :param armeEquipee: L'arme actuellement équipée. Par défaut "Poings".
        :param inventaireArmes: La liste des armes dans l'inventaire. Par défaut vide.
        :param queteActuelle: La quête actuellement active. Par défaut None.
        :param niveau: Le niveau du combattant. Par défaut 1.
        :param experience: L'expérience du combattant. Par défaut 0.
        """
        super().__init__(nom, piece, vie)
        self.id: int = id
        self.maxVie: int = maxVie
        self.vie: int = vie
        self.inventairePotions: int = inventairePotions
        self.armeEquipee: Arme = armeEquipee
        self.inventaireArmes: List[Arme] = []
        self.queteActuelle: Optional[Quete] = queteActuelle
        self.niveau: int = niveau
        self.experience: int = experience
        self.dao = CombattantDAO()
        
    @staticmethod
    def authentifier(email: str, password: str) -> Optional["Combattant"]:
        """
        Authentifie un utilisateur en utilisant CombattantDAO.

        :param email: Email de l'utilisateur
        :param password: Mot de passe de l'utilisateur
        :return: Instance de Combattant si l'authentification réussie, sinon None
        """
        combattantInfo = CombattantDAO.authentifier(email, password)
        if combattantInfo:
            if combattantInfo["piece"] == None:
                return Combattant(
                    combattantInfo["id"],
                    combattantInfo["nom"]
                )
            return Combattant(
                combattantInfo["id"],
                combattantInfo["nom"],
                combattantInfo["piece"],
                combattantInfo["vie"],
                combattantInfo["maxVie"],
                combattantInfo["inventairePotions"],
                combattantInfo["niveau"],
                combattantInfo["experience"],
            )
        return None
        
    @staticmethod
    def inscrire(name: str, email: str, password: str) -> Optional["Combattant"]:
        """
        Enregistre un nouvel utilisateur en utilisant CombattantDAO.

        :param name: Nom de l'utilisateur
        :param email: Email de l'utilisateur
        :param password: Mot de passe de l'utilisateur
        :return: Instance de Combattant si l'inscription est réussie, sinon None
        """
        combattantInfo = CombattantDAO.inscrire(name, email, password)
        return Combattant(
            combattantInfo["id"], 
            combattantInfo["nom"]) if combattantInfo else None
        
    def save(self) -> None:
        """
        Enregistre les informations du combattant dans la base de données.

        :raises Exception: Si l'enregistrement échoue.
        """
        try:
            self.dao.saveCombattant(self)
        except Exception as e:
            raise e
        
    def recupererArmeEquipee(self) -> None:
        """
        Récupère l'arme équipée du combattant depuis la base de données.

        :raises Exception: Si la récupération échoue.
        """
        try:
            armeEquipeeId = self.dao.getArmeEquipeeId(self.id)
            arme = Arme.getArmeById(armeEquipeeId)
            if arme:
                self.armeEquipee = arme
            else:
                raise NoSuchItemError("Aucune arme équipée.")
        except Exception as e:
            raise e

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
        messages.append("Félicitations ! Vous avez terminé la " + str(self.queteActuelle.getNom()) + " !")
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

        # Vérifier si le monstre est dans la liste avant de le supprimer
        if monstre in donjon.getListeMonstres():
            donjon.supprimerMonstre(monstre)
        try:
            monstreQuete = self.getMonstreQueteActuelle()
            if monstreQuete == monstre:
                messages.extend(self.reussiteQuete()) # réussite de quete : gain d'or, d'expérience, suppression de la quête actuelle (statut devient Terminée)
        except NoActiveQuestError:
            pass
        finally:
            quetesEnCours = Quete.getQuetesEnCoursUsingDifficulte(donjon.getDifficulte())
            for quete in quetesEnCours:
                if quete.getMonstreCible() == monstre:
                    quete.queteFinie()
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

    def armeDansInventaire(self, arme: Arme) -> bool:
        """
        Vérifie si une arme est dans l'inventaire.

        :param arme: L'arme à vérifier.
        :return: True si l'arme est dans l'inventaire, False sinon.
        """
        return arme in self.inventaireArmes
    
    def getMaxVie(self) -> int:
        """
        Retourne la vie maximale du combatt
        :return: La vie maximale.
        """
        return self.maxVie
    
    def getId(self) -> int:
        """
        Retourne l'identifiant du combattant.

        :return: L'identifiant.
        """
        return self.id
    
    def __str__(self):
        return f"Combattant(nom={self.nom}, piece={self.piece}, vie={self.vie}, maxVie={self.maxVie}, inventairePotions={self.inventairePotions}, armeEquipee={self.armeEquipee}, inventaireArmes={self.inventaireArmes}, queteActuelle={self.queteActuelle}, niveau={self.niveau}, experience={self.experience})"