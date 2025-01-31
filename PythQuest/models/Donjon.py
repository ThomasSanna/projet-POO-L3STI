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
    
    def __init__(self, nom, difficulte, monstre=None):
        self.id = Donjon.nbDonjons
        Donjon.nbDonjons += 1
        self.nom = nom
        self.difficulte = difficulte
        if monstre is None:
            monstre = Monstre.creerMonstreAleatoire(difficulte)
        self.listeMonstres = [monstre]
        self.ajouterNbMonstre(random.randint(3, 10))
        self.statut = Donjon.ACTIF
        Donjon.tousLesDonjons.append(self)
        
    @staticmethod
    def creerDonjonAleatoire(difficulte, monstre: Monstre):
        prefixe = Donjon.PREFIXES
        suffixe = Donjon.SUFFIXES[random.randint(0, len(Donjon.SUFFIXES) - 1)]
        nom = prefixe + suffixe
        donjon = Donjon(nom, difficulte, monstre)
        return donjon
        
    def ajouterNbMonstre(self, nb: int):
        for i in range(nb):
            monstre = Monstre.creerMonstreAleatoire(self.difficulte)
            self.listeMonstres.append(monstre)
            
    def supprimerMonstre(self, monstre: Monstre):
        if monstre in self.listeMonstres:
            self.listeMonstres.remove(monstre)
            return True
        return False
    
    def putInactif(self):
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
    
    def getTousLesDonjons():
        return Donjon.tousLesDonjons

    def __str__(self):
        return (f"Donjon(id={self.id}, nom={self.nom}, difficulte={self.difficulte}, monstres={self.listeMonstres})")