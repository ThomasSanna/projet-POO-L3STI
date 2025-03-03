import unittest
import sys
import os

# Ajouter le chemin du répertoire parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.Combattant import Combattant
from models.Arme import Arme
from models.Quete import Quete
from models.Donjon import Donjon
from models.Medecin import Medecin
from models.Forgeron import Forgeron
from models.Monstre import Monstre
from models.exceptions import InsufficientFundsError, InventoryFullError, NoSuchItemError, QuestAlreadyAcceptedError, NoActiveQuestError

class TestCombattant(unittest.TestCase):
    """
    Classe de test pour la classe Combattant.
    """

    def setUp(self):
        """
        Configure les objets nécessaires pour les tests.
        """
        self.combattant = Combattant("Testeur", 100, 100)
        self.arme = Arme("Épée de Test", 50, 20)
        self.quete = Quete("Quête de Test", 100, 1, 1)
        self.monstre = Monstre("Test Monstre", 10, 10, self.arme, 1)
        self.donjon = Donjon("Donjon de Test", 1, 1, self.monstre)

    def testGagnerExperience(self):
        """
        Teste la méthode gagnerExperience.
        """
        self.combattant.gagnerExperience(150)
        self.assertEqual(self.combattant.niveau, 2)
        self.assertEqual(self.combattant.experience, 50)

    def testResetApresMort(self):
        """
        Teste la méthode resetApresMort.
        """
        self.combattant.perdreVie(100)
        self.combattant.resetApresMort()
        self.assertEqual(self.combattant.vie, self.combattant.maxVie // 1.5)
        self.assertEqual(self.combattant.piece, 100 - (100 // 1.5))

    def testGagnerPotion(self):
        """
        Teste la méthode gagnerPotion.
        """
        self.combattant.gagnerPotion()
        self.assertEqual(self.combattant.inventairePotions, 1)
        with self.assertRaises(InventoryFullError):
            for _ in range(Combattant.NB_POTION_MAX + 1):
                self.combattant.gagnerPotion()

    def testPerdrePotion(self):
        """
        Teste la méthode perdrePotion.
        """
        self.combattant.gagnerPotion()
        self.combattant.perdrePotion()
        self.assertEqual(self.combattant.inventairePotions, 0)
        with self.assertRaises(NoSuchItemError):
            self.combattant.perdrePotion()

    def testBoirePotion(self):
        """
        Teste la méthode boirePotion.
        """
        self.combattant.gagnerPotion()
        self.combattant.perdreVie(50)
        self.combattant.boirePotion()
        self.assertEqual(self.combattant.vie, 65)
        self.assertEqual(self.combattant.inventairePotions, 0)
        with self.assertRaises(NoSuchItemError):
            self.combattant.boirePotion()

    def testAcheterPotion(self):
        """
        Teste la méthode acheterPotion.
        """
        medecin = Medecin("Test Medecin")
        self.combattant.acheterPotion(medecin)
        self.assertEqual(self.combattant.inventairePotions, 1)
        self.assertEqual(self.combattant.piece, 90)

    def testAcheterArme(self):
        """
        Teste la méthode acheterArme.
        """
        forgeron = Forgeron("Test Forgeron")
        forgeron.ajouterArme(self.arme)
        self.combattant.acheterArme(forgeron, self.arme)
        self.assertIn(self.arme, self.combattant.inventaireArmes)
        self.assertEqual(self.combattant.piece, 50)

    def testAccepterQuete(self):
        """
        Teste la méthode accepterQuete.
        """
        self.combattant.accepterQuete(self.quete)
        self.assertEqual(self.combattant.queteActuelle, self.quete)
        with self.assertRaises(QuestAlreadyAcceptedError):
            self.combattant.accepterQuete(self.quete)

    def testAbandonnerQuete(self):
        """
        Teste la méthode abandonnerQuete.
        """
        self.combattant.accepterQuete(self.quete)
        self.combattant.abandonnerQuete()
        self.assertIsNone(self.combattant.queteActuelle)
        with self.assertRaises(NoActiveQuestError):
            self.combattant.abandonnerQuete()

    def testBattreMonstre(self):
        """
        Teste la méthode battreMonstre.
        """
        self.combattant.battreMonstre(self.monstre, self.donjon)
        self.assertIn(self.monstre.getArmePossedee(), self.combattant.inventaireArmes)

    def testAttaquer(self):
        """
        Teste la méthode attaquer.
        """
        monstre = Monstre("Test Monstre", 10, 10, self.arme, 1)
        self.combattant.attaquer(monstre)
        self.assertEqual(monstre.vie, 5) # 10-5=5 (car l'arme de base du combattant inflige 5 dégâts (Poings))

if __name__ == '__main__':
    unittest.main()