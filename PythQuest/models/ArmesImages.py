import random
from PIL import Image
import os

# Tuples de préfixes, suffixes et états d'arme
prefixes = (
    ("Épée", 40), ("Hache", 50), ("Dague", 30), ("Lance", 45),
    ("Marteau", 55), ("Bâton", 25), ("Glaive", 60), ("Faux", 65), ("Fleuret", 30),
    ("Katana", 45), ("Gourdin", 20), ("Fouet", 25), ("Hallebarde", 55),
    ("Masse", 50), ("Poignard", 35), ("Trident", 50)
)

suffixes = (
    ("de Feu", 20),  
    ("du Dragon", 30),  
    ("de Glace", 20),  
    ("des Ombres", 25),  
    ("de la Nuit", 25),  
    ("du Chaos", 35),  
    ("de la Mort", 40),  
    ("de Lumière", 20),  
    ("du Soleil", 30),  
    ("de la Lune", 20),  
    ("des Étoiles", 25),  
    ("de la Vie", 20),  
    ("de la Tempête", 30),  
    ("du Vent", 20),  
    ("de la Foudre", 35),  
    ("de l'Eau", 20),  
    ("de l'Océan", 20),  
    ("de l'Esprit", 25),  
    ("de la Forêt", 20),  
    ("en Bois", 5),  
    ("du Guerrier", 25),  
    ("du Mage", 20),  
    ("du Voleur", 25),  
    ("du Paladin", 30),  
    ("du Barbare", 35),  
    ("du Ranger", 25),  
    ("du Sorcier", 20),  
    ("du Nécromancien", 35),  
    ("du Druide", 25),  
    ("de l'Assassin", 30),  
    ("du Chevalier", 25),  
    ("en Argent", 15),  
    ("en Adamantium", 35),  
    ("en Acier", 15),  
    ("en Fer", 10),  
    ("en Cuivre", 5),  
    ("en Os", 10),  
    ("en Quartz", 10),  
    ("en Pierre", 10),  
    ("en Cristal", 20),  
    ("en Diamant", 30),  
    ("en Topaze", 15), 
    ("en Opale", 15),  
    ("en Saphir", 25),  
    ("en Rubis", 25),  
    ("en Émeraude", 20),  
    ("en Jade", 20),  
    ("en Améthyste", 20),  
    ("en Obsidienne", 30),  
    ("en Verre", 5),  
    ("en Plastique", 1),  
    ("en Or", 20),  
    ("en Bronze", 10)
)

etatArme = (
    ("Cassé", 20), ("Endommagé", 40), ("Usé", 60), ("Solide", 80), ("Neuf", 90)
)

raretes = {
    (0, 20): "normal",
    (20, 40): "moyenne",
    (40, 60): "rare",
    (60, 80): "epique",
    (80, 100): "legendaire"
}

# Dictionnaire des catégories de suffixes
categoriesSuffixes = {
    "feu": ["de Feu", "du Dragon"],
    "glace": ["de Glace"],
    "ombre": ["des Ombres", "de la Nuit", "du Chaos", "de la Mort"],
    "lumiere": ["de Lumière", "du Soleil", "de la Lune", "des Étoiles", "de la Vie"],
    "vent": ["de la Tempête", "du Vent"],
    "foudre": ["de la Foudre"],
    "eau": ["de l'Eau", "de l'Océan"],
    "esprit": ["de l'Esprit"],
    "nature": ["de la Forêt", "en Bois"],
    "rien": ["du Guerrier", "du Mage", "du Voleur", "du Paladin", "du Barbare", "du Ranger", "du Sorcier", "du Nécromancien", "du Druide", "de l'Assassin", "du Chevalier", "en Argent", "en Adamantium", "en Acier", "en Fer"],
    "cuivre": ["en Cuivre", "en Bronze"],
    "os": ["en Os", "en Quartz"],
    "pierre": ["en Pierre"],
    "diamant": ["en Cristal", "en Diamant", "en Topaze", "en Opale"],
    "saphir": ["en Saphir"],
    "rubis": ["en Rubis"],
    "emeraude": ["en Émeraude", "en Jade"],
    "amethyste": ["en Améthyste"],
    "obsidienne": ["en Obsidienne"],
    "transparent": ["en Verre", "en Plastique"],
    "or": ["en Or"],
}

# Fonction de génération d'arme
def getCategorie(suffixe):
    """Retourne la catégorie associée à un suffixe."""
    for categorie, suffixes in categoriesSuffixes.items():
        if suffixe in suffixes:
            return categorie
    return "inconnu"

def getRarete(degats):
    """Retourne la rareté en fonction des dégâts."""
    for (minDegats, maxDegats), rarete in raretes.items():
        if minDegats <= degats < maxDegats:
            return rarete
    return "inconnu"  

def ajusterOpacite(image, alpha):
    """Ajuste l'opacité d'une image en modifiant son canal alpha."""
    image = image.convert("RGBA")
    pixels = image.load()  # Accéder aux pixels
    for i in range(image.width):
        for j in range(image.height):
            r, g, b, a = pixels[i, j]
            pixels[i, j] = (r, g, b, int(a * alpha))  # Modifier l'opacité
    return image

def genererArme(typeArme, suffixe, etat, degats, dossier="view"):
    """
    Génère une image d'arme avec des effets, un état et une rareté spécifiques.
    Args:
        typeArme (str): Le type de l'arme (nom du fichier sans extension).
        suffixe (str): Le suffixe de l'arme, utilisé pour déterminer l'effet.
        etat (str): L'état de l'arme, utilisé pour superposer une image d'état.
        degats (int): Les dégâts de l'arme, utilisés pour déterminer la rareté.
        dossier (str, optional): Le dossier contenant les images des armes, effets, états et raretés. Par défaut "assets".
    Returns:
        None: La fonction sauvegarde l'image générée dans le dossier "assets/armes_crees" et affiche un message de confirmation.
    """
    
    # Déterminer la rareté via le dictionnaire
    rarete = getRarete(degats)
    effet = getCategorie(suffixe)
    
    # Charger l'image de l'arme
    arme = Image.open(f"{dossier}/assets/armes/{typeArme}.png").convert("RGBA")
    
    # Si l'effet est "transparent", on ajuste l'opacité de l'arme
    if effet == "transparent":
        arme = ajusterOpacite(arme, 0.5)  # Baisse l'opacité de l'arme à 50%
    
    # Pour la catégorie "rien", on ne superpose rien
    if effet != "rien":
        # Charger les images d'effet
        effetImg = Image.open(f"{dossier}/assets/effets/{effet}.png").convert("RGBA")
        # Appliquer la transparence de 50% sur l'effet (alpha 0.5)
        effetImg = ajusterOpacite(effetImg, 0.7)
        # Superposer l'effet sur l'arme
        arme.paste(effetImg, (0, 0), effetImg)
    
    # Charger l'image de l'état si elle existe, sinon ne pas l'ajouter
    try:
        etatImg = Image.open(f"{dossier}/assets/etats/{etat}.png").convert("RGBA")
        # Appliquer la transparence de 50% sur l'état (alpha 0.5)
        etatImg = ajusterOpacite(etatImg, 0.5)
        # Superposer l'état sur l'arme
        arme.paste(etatImg, (0, 0), etatImg)
    except FileNotFoundError:
        pass

    # Charger l'image de la rareté
    rareteImg = Image.open(f"{dossier}/assets/raretes/{typeArme}_{rarete}.png").convert("RGBA")
    
    # Superposer l'image de rareté
    arme.paste(rareteImg, (0, 0), rareteImg)

    # Nom du fichier de sortie
    output = f"{typeArme} {suffixe} {etat} {rarete}.png"
    outputPath = os.path.join("view/assets/armes_crees", output)
    arme.save(outputPath)
    print(f"Arme générée : {output} (Rareté : {rarete})")

# Exemple d'utilisation avec des paramètres aléatoires
prefixe, degats = random.choice(prefixes)
suffixe, _ = random.choice(suffixes)
etat, _ = random.choice(etatArme)

genererArme(prefixe, suffixe, etat, degats)