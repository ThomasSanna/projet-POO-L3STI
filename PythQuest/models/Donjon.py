from models.Monstre import Monstre
import random

class Donjon:
    
    PREFIXES = "Donjon "
    SUFFIXES = (
        "sombre", "glacial", "ancien", "mystérieux", "perdu", "maudit", "dangereux", 
        "sinistre", "hanté", "abandonné", "oublié", "délabré", "dévasté", "déchu",
        "majestueux", "infini", "souterrain", "enchanté", "démoniaque", "caché",
        "profond", "infesté", "désolé", "désespéré", "interdit", "ténébreux", 
        "sanguinaire", "corrompu", "lumineux", "rougeoyant", "chaotique", "immortel",
        "pestiféré", "tombé", "destructeur", "légendaire", "éternel", "foudroyé",
        "ensorcelé", "inexorable", "voilé", "métallique", "runique", "cristallin",
        "doré", "argenté", "de glace", "de feu", "de pierre", "de lave", "de l'ombre",
        "de la lumière", "de la mort", "de la vie", "de la guerre", "de la paix",
        "de la brume", "du crépuscule", "de l'aube", "de l'éclipse", "de la tempête",
        "de la foudre", "de la terreur", "de l'oubli", "de la renaissance", "du chaos",
        "de l'ordre", "de la destruction", "de la création", "de l'illusion", "de la réalité",
        "de l'infini", "de l'éternité", "de l'abîme", "de la caverne", "de la montagne",
        "de la vallée", "de la forêt", "de la mer", "de l'océan", "du désert",
        "de la plaine", "de la jungle", "de la savane", "de la toundra", "de l'arctique",
        "de l'antarctique", "de l'espace", "de la galaxie", "de l'univers", "du multivers"
    )
    
    ACTIF = "Actif"
    INACTIF = "Inactif"
    
    tousLesDonjons = []
    nbDonjons = 1
    
    def __init__(self, nom, difficulte, niveauJoueur, monstre=None):
        self.id = Donjon.nbDonjons
        Donjon.nbDonjons += 1
        self.nom = nom
        self.difficulte = difficulte
        self.listeMonstres = []
        if monstre is not None:
            self.listeMonstres = [monstre]
        self.ajouterNbMonstre(random.randint(3, 10), niveauJoueur)
        self.statut = Donjon.ACTIF
        self.niveau = niveauJoueur
        Donjon.tousLesDonjons.append(self)
        
    @staticmethod
    def creerDonjonAleatoire(difficulte, monstre: Monstre, niveauJoueur):
        prefixe = Donjon.PREFIXES
        suffixe = Donjon.SUFFIXES[random.randint(0, len(Donjon.SUFFIXES) - 1)]
        nom = prefixe + suffixe
        donjon = Donjon(nom, difficulte, niveauJoueur, monstre)
        return donjon
    
    @staticmethod
    def afficherTousLesDonjonsActifs():
        for i, donjon in enumerate(Donjon.getTousLesDonjonsActifs()):
            if donjon.statut == Donjon.ACTIF:
                print(f"{i + 1}. {donjon.nom} (lvl {donjon.niveau}, difficulté {donjon.difficulte}). Nombre de monstres: {len(donjon.listeMonstres)})")
        print(f"{len(Donjon.getTousLesDonjonsActifs()) + 1}. Retour")
    
    def ajouterNbMonstre(self, nb: int, niveauJoueur):
        for i in range(nb):
            monstre = Monstre.creerMonstreAleatoire(self.difficulte, niveauJoueur)
            self.listeMonstres.append(monstre)
      
    def supprimerMonstre(self, monstre: Monstre):
        if monstre in self.listeMonstres:
            self.listeMonstres.remove(monstre)
        else:
            raise ValueError("Le monstre n'est pas dans la liste des monstres du donjon.")
    
    def getMonstreAleatoire(self) -> "Monstre":
        return random.choice(self.listeMonstres)
    
    def setInactif(self):
        self.statut = Donjon.INACTIF
    
    def estVide(self):
        return len(self.listeMonstres) == 0
    
    def getListeMonstres(self):
        return self.listeMonstres
    
    def getNom(self):
        return self.nom
    
    def getDifficulte(self):
        return self.difficulte
    
    def getId(self):
        return self.id
    
    def getNbMonstres(self):
        return len(self.listeMonstres)
    
    @staticmethod
    def getTousLesDonjons():
        return Donjon.tousLesDonjons
    
    @staticmethod
    def getTousLesDonjonsActifs() -> list['Donjon']:
        donjonsActifs = []
        for donjon in Donjon.tousLesDonjons:
            if donjon.statut == Donjon.ACTIF:
                donjonsActifs.append(donjon)
        return donjonsActifs
    
    @staticmethod
    def getDonjonIndexActif(index: int) -> 'Donjon':
        donjonsActifs = Donjon.getTousLesDonjonsActifs()
        if index < 0 or index >= len(donjonsActifs):
            raise IndexError("Donjon index out of range.")
        return donjonsActifs[index]
    
    @staticmethod
    def getNbDonjonsActifs():
        len(Donjon.getTousLesDonjonsActifs())
    
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return f"{self.nom} (id: {self.id}, niveau: {self.niveau}, difficulté: {self.difficulte}, monstres: {self.listeMonstres}, statut: {self.statut})"