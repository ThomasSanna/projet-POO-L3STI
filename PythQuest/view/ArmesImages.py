import random
from PIL import Image
import os

# Tuples de préfixes, suffixes et états d'arme
PREFIXES = (
    ("Épée", 40), ("Hache", 50), ("Dague", 30), ("Lance", 45),
    ("Marteau", 55), ("Bâton", 25), ("Glaive", 60), ("Faux", 65), ("Fleuret", 30),
    ("Katana", 45), ("Gourdin", 20), ("Fouet", 25), ("Hallebarde", 55),
    ("Masse", 50), ("Poignard", 35), ("Trident", 50)
)

SUFFIXES = (
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

ETAT_ARME = (
    ("Cassé", 20), ("Endommagé", 40), ("Usé", 60), ("Solide", 80), ("Neuf", 90)
)

RARETES = {
    (0, 20): "normal",
    (20, 40): "moyenne",
    (40, 60): "rare",
    (60, 80): "epique",
    (80, 100): "legendaire"
}

# Dictionnaire des catégories de suffixes
CATEGORIES_SUFFIXES = {
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
def get_categorie(suffixe):
    """Retourne la catégorie associée à un suffixe."""
    for categorie, suffixes in CATEGORIES_SUFFIXES.items():
        if suffixe in suffixes:
            return categorie
    return "inconnu"

def get_rarete(degats):
    """Retourne la rareté en fonction des dégâts."""
    for (min_degats, max_degats), rarete in RARETES.items():
        if min_degats <= degats < max_degats:
            return rarete
    return "inconnu"  

def ajuster_opacite(image, alpha):
    """Ajuste l'opacité d'une image en modifiant son canal alpha."""
    image = image.convert("RGBA")
    pixels = image.load()  # Accéder aux pixels
    for i in range(image.width):
        for j in range(image.height):
            r, g, b, a = pixels[i, j]
            pixels[i, j] = (r, g, b, int(a * alpha))  # Modifier l'opacité
    return image

def generer_arme(type_arme, suffixe, etat, degats, dossier="assets"):
    # Déterminer la rareté via le dictionnaire
    rarete = get_rarete(degats)
    effet = get_categorie(suffixe)
    
    # Charger l'image de l'arme
    arme = Image.open(f"{dossier}/armes/{type_arme}.png").convert("RGBA")
    
    # Si l'effet est "transparent", on ajuste l'opacité de l'arme
    if effet == "transparent":
        arme = ajuster_opacite(arme, 0.5)  # Baisse l'opacité de l'arme à 50%
    
    # Pour la catégorie "rien", on ne superpose rien
    if effet != "rien":
        # Charger les images d'effet
        effet_img = Image.open(f"{dossier}/effets/{effet}.png").convert("RGBA")
        # Appliquer la transparence de 50% sur l'effet (alpha 0.5)
        effet_img = ajuster_opacite(effet_img, 0.7)
        # Superposer l'effet sur l'arme
        arme.paste(effet_img, (0, 0), effet_img)
    
    # Charger l'image de l'état si elle existe, sinon ne pas l'ajouter
    try:
        etat_img = Image.open(f"{dossier}/etats/{etat}.png").convert("RGBA")
        # Appliquer la transparence de 50% sur l'état (alpha 0.5)
        etat_img = ajuster_opacite(etat_img, 0.5)
        # Superposer l'état sur l'arme
        arme.paste(etat_img, (0, 0), etat_img)
    except FileNotFoundError:
        pass

    # Charger l'image de la rareté
    rarete_img = Image.open(f"{dossier}/raretes/{type_arme}_{rarete}.png").convert("RGBA")
    
    # Superposer l'image de rareté
    arme.paste(rarete_img, (0, 0), rarete_img)

    # Nom du fichier de sortie
    output = f"{type_arme} {suffixe} {etat} {rarete}.png"
    output_path = os.path.join("assets/armes_crees", output)
    arme.save(output_path)
    print(f"Arme générée : {output} (Rareté : {rarete})")

# Exemple d'utilisation avec des paramètres aléatoires
prefixe, degats = random.choice(PREFIXES)
suffixe, _ = random.choice(SUFFIXES)
etat, _ = random.choice(ETAT_ARME)


generer_arme(prefixe, suffixe, etat, degats)
