from models.Quete import Quete
import random

class GestionnaireDeQuetes:
    def __init__(self):
        pass


    @staticmethod
    def creerQueteDonjonMonstres(niveauJoueur):
        return Quete.creerQueteAleatoire(niveauJoueur)
        