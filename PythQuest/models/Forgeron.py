from models.Personnage import Personnage
from models.Combattant import Combattant
from models.Arme import Arme
import random

class Forgeron(Personnage):
    def __init__(self, nom):
        super().__init__(nom, 0, 100)
        self.inventaireArmes = []
        for i in range(random.randint(2, 10)):
            self.forgerArme()
        
    @staticmethod
    def genererArmeAleatoire():
        prefixes = [
            ("Épée", 40), ("Hache", 50), ("Dague", 30), ("Arc", 35), ("Lance", 45),
            ("Marteau", 55), ("Bâton", 25), ("Glaive", 60), ("Faux", 65), ("Fleuret", 30),
            ("Katana", 45), ("Gourdin", 20), ("Bouclier", 15), ("Fouet", 25), ("Hallebarde", 55),
            ("Masse", 50), ("Poignard", 35), ("Rapière", 40), ("Sceptre", 30), ("Trident", 50)
        ]
        suffixes = [
            ("de Feu", 20), ("de Glace", 20), ("du Dragon", 30), ("des Ombres", 25), ("de Lumière", 20),
            ("de la Nuit", 25), ("du Soleil", 30), ("de l'Aube", 20), ("du Crépuscule", 25), ("de la Tempête", 30),
            ("de la Foudre", 35), ("de la Terre", 20), ("de l'Eau", 20), ("du Vent", 20), ("de l'Esprit", 25),
            ("de la Forêt", 20), ("de la Montagne", 25), ("de l'Océan", 20), ("de la Lune", 20), ("des Étoiles", 25),
            ("du Chaos", 35), ("de l'Ordre", 25), ("de la Mort", 40), ("de la Vie", 20), ("de l'Inconnu", 30),
            ("de l'Ancien Temps", 35), ("du Guerrier", 25), ("du Mage", 20), ("du Voleur", 25), ("du Paladin", 30),
            ("du Barbare", 35), ("du Ranger", 25), ("du Sorcier", 20), ("du Nécromancien", 35), ("du Druide", 25),
            ("de l'Assassin", 30), ("du Chevalier", 25), ("en Acier", 15), ("en Fer", 10), ("en Or", 20),
            ("en Argent", 15), ("en Bronze", 10), ("en Cuivre", 5), ("en Bois", 5), ("en Os", 10),
            ("en Pierre", 10), ("en Cristal", 20), ("en Diamant", 30), ("en Saphir", 25), ("en Rubis", 25),
            ("en Émeraude", 20), ("en Topaze", 15), ("en Améthyste", 20), ("en Opale", 15), ("en Quartz", 10),
            ("en Jade", 20), ("en Mithril", 25), ("en Adamantium", 35), ("en Obsidienne", 30), ("en Verre", 5),
            ("en Plastique", 1)
        ]
        etatArme = [
            ("Cassé", 20), ("Endommagé", 40), ("Usé", 60), ("Solide", 80), ("Neuf", 90)
        ]
        prefixe, degatsPrefixe = random.choice(prefixes)
        suffixe, degatsSuffixe = random.choice(suffixes)
        etat, pourcentageDegats = random.choice(etatArme)
        degats = int((degatsPrefixe + degatsSuffixe) * (pourcentageDegats / 100))
        plageValeurOr = [degats*3 - 10, degats*3 + 10] # Valeur de l'arme entre degats*2 - 50 et degats*2 + 100
        valeurOr = random.randint(plageValeurOr[0], plageValeurOr[1])
        
        return Arme(f"{prefixe} {suffixe} ({etat})", valeurOr, degats)

        
    def ajouterArme(self, arme: Arme) -> None:
        self.inventaireArmes.append(arme)
        
    def enleverArme(self, arme: Arme) -> bool:
        if arme in self.inventaireArmes:
            self.inventaireArmes.remove(arme)
            return True
        return False
        
    def forgerArme(self) -> None:
        self.ajouterArme(self.genererArmeAleatoire())
        
    def __str__(self):
        return (f"Forgeron(nom={self.nom}, or_={self.or_}, vie={self.vie}, inventaireArmes={self.inventaireArmes})")