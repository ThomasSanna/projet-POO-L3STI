from models.Monstre import Monstre

class Donjon:
    def __init__(self, nom, difficulte):
        self.nom = nom
        self.difficulte = difficulte
        self.monstres = []