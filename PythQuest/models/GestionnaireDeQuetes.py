from models.Quete import Quete
from models.Monstre import Monstre
from models.Donjon import Donjon
import random

class GestionnaireDeQuetes:
    def __init__(self):
        pass


    @staticmethod
    def creerQueteDonjonMonstres():
        return Quete.creerQueteAleatoire()
        