# PythQuest

PythQuest est un jeu de rôle textuel développé en Python. Le jeu utilise une architecture MVC (Modèle-Vue-Contrôleur) et inclut des fonctionnalités telles que la gestion de quêtes, de donjons, de monstres, et d'armes. Le projet est conçu pour être extensible et maintenable, avec des tests automatisés et une interface graphique prévue avec Tkinter.

## Table des matières

- [PythQuest](#pythquest)
  - [Table des matières](#table-des-matières)
  - [Explication du jeu](#explication-du-jeu)
  - [Installation](#installation)
  - [Utilisation](#utilisation)

## Explication du jeu

PythQuest est un jeu de rôle qui permet au joueur d'incarner un aventurier qui doit accomplir des quêtes pour progresser dans le jeu. Le joueur peut explorer des donjons, combattre des monstres, et gagner des récompenses. Le jeu est divisé en plusieurs parties :

- **Achat d'armes** : le joueur peut acheter des armes pour améliorer ses chances de victoire lors des combats.
- **Potions** : le joueur peut acheter des potions pour se soigner lors des combats.
- **Quêtes** : le joueur peut accomplir des quêtes pour gagner de l'expérience et de l'or. Ces quêtes sont assignées obligatoirement à un donjon existant et à un monstre. Le joueur doit donc se rendre dans le donjon correspondant et vaincre le monstre pour accomplir la quête.
- **Donjons** : le joueur peut explorer des donjons pour combattre des monstres et gagner des récompenses.
- **Monstres** : le joueur peut combattre des monstres pour gagner de l'expérience et de l'or. Lorsqu'un monstre est combattu, le joueur gagne son arme, et son or attribué est calculé en fonction de la difficulté du monstre.
- **Inventaire** : le joueur peut consulter son inventaire pour voir les armes et les potions qu'il possède. Il peut également équiper une arme. Lorsqu'une arme est équipée, elle remplace l'arme actuelle du joueur.
- **Statistiques** : le joueur peut consulter ses statistiques pour voir son niveau, son expérience, son or, et ses points de vie.

## Installation

Pour installer et exécuter PythQuest, suivez les étapes ci-dessous :

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/ThomasSanna/projet-POO-L3STI.git
    cd PythQuest
    ```

2. Créez un environnement virtuel et activez-le :
    ```sh
    python -m venv env
    .\env\Scripts\activate  # Sur Windows
    source env/bin/activate  # Sur macOS/Linux
    ```

3. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

## Utilisation

Pour lancer le jeu, exécutez le fichier principal :
```sh
python main.py
```