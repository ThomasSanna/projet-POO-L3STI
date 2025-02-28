# PythQuest

PythQuest est un jeu de rôle textuel développé en Python. Il inclut des fonctionnalités telles que la gestion de quêtes, de donjons, de monstres, et d'armes. Le projet est conçu pour être extensible et maintenable, avec des tests automatisés et une interface graphique prévue avec Tkinter.

## Table des matières

- [PythQuest](#pythquest)
  - [Table des matières](#table-des-matières)
  - [Explication du jeu](#explication-du-jeu)
  - [Bonnes pratiques de codage](#bonnes-pratiques-de-codage)
    - [Nommage des variables et des fonctions](#nommage-des-variables-et-des-fonctions)
    - [Structure du code](#structure-du-code)
    - [Gestion des exceptions](#gestion-des-exceptions)
    - [Tests automatisés](#tests-automatisés)
    - [Documentation](#documentation)
    - [Collaboration](#collaboration)
  - [Informations supplémentaires](#informations-supplémentaires)
    - [Architecture du projet](#architecture-du-projet)
    - [Dépendances](#dépendances)
    - [Exécution du jeu](#exécution-du-jeu)
    - [Contribution](#contribution)

## Explication du jeu

PythQuest est un jeu de rôle qui permet au joueur d'incarner un aventurier qui doit accomplir des quêtes pour progresser dans le jeu. Le joueur peut explorer des donjons, combattre des monstres, et gagner des récompenses. Le jeu est divisé en plusieurs parties :

- **Achat d'armes** : le joueur peut acheter des armes pour améliorer ses chances de victoire lors des combats.
- **Potions** : le joueur peut acheter des potions pour se soigner lors des combats.
- **Quêtes** : le joueur peut accomplir des quêtes pour gagner de l'expérience et de l'or. Ces quêtes sont assignées obligatoirement à un donjon existant et à un monstre. Le joueur doit donc se rendre dans le donjon correspondant et vaincre le monstre pour accomplir la quête.
- **Donjons** : le joueur peut explorer des donjons pour combattre des monstres et gagner des récompenses.
- **Monstres** : le joueur peut combattre des monstres pour gagner de l'expérience et de l'or. Lorsqu'un monstre est combattu, le joueur gagne son arme, et son or attribué est calculé en fonction de la difficulté du monstre.
- **Inventaire** : le joueur peut consulter son inventaire pour voir les armes et les potions qu'il possède. Il peut également équiper une arme. Lorsqu'une arme est équipée, elle remplace l'arme actuelle du joueur.
- **Statistiques** : le joueur peut consulter ses statistiques pour voir son niveau, son expérience, son or, et ses points de vie.

## Bonnes pratiques de codage

Ce projet suit plusieurs bonnes pratiques de codage pour assurer la maintenabilité et la lisibilité du code. Voici quelques-unes des pratiques suivies :

### Nommage des variables et des fonctions

- Utilisez des noms de variables et de fonctions explicites et significatifs.
- Utilisez le style camelCase pour les noms de variables et de fonctions.
- Utilisez le style PascalCase pour les noms de classes.

### Structure du code

- Séparez la logique applicative de l'interface utilisateur en utilisant le modèle MVC (Modèle-Vue-Contrôleur).
- Organisez le code en modules et fichiers logiques.
- Utilisez des docstrings pour documenter les classes, les méthodes et les fonctions.

### Gestion des exceptions

- Gérez les exceptions de manière appropriée pour éviter les plantages inattendus.
- Utilisez des blocs try-except pour capturer et gérer les erreurs spécifiques.

### Tests automatisés

- Écrivez des tests unitaires pour vérifier le bon fonctionnement des différentes parties du code.
- Utilisez des frameworks de test comme `unittest` ou `pytest` pour automatiser les tests.

### Documentation

- Documentez le code avec des commentaires et des docstrings.
- Maintenez un fichier README à jour avec des instructions claires pour l'installation et l'utilisation du projet.

### Collaboration

- Utilisez Git pour le contrôle de version.
- Créez des branches pour chaque nouvelle fonctionnalité ou correction de bug.
- Fusionnez les branches dans `main` uniquement lorsque le code est stable et testé.

## Informations supplémentaires

### Architecture du projet

Le projet utilise une architecture MVC (Modèle-Vue-Contrôleur) pour séparer la logique métier de l'interface utilisateur. Voici un aperçu des composants principaux :

- **Modèle (Model)** : Contient les classes représentant les données et la logique métier du jeu (par exemple, `Combattant`, `Donjon`, `Quete`).
- **Vue (View)** : Gère l'affichage des informations à l'utilisateur et la collecte des entrées utilisateur.
- **Contrôleur (Controller)** : Coordonne les interactions entre le modèle et la vue, et gère la logique de flux du jeu.

### Dépendances
Le projet utilise les bibliothèques suivantes :
- `random` : Pour générer des nombres aléatoires.
- `typing` : Pour les annotations de type.

### Exécution du jeu
Pour lancer le jeu, exécutez le fichier principal :
```sh
python main.py
```

### Contribution
Les contributions sont les bienvenues ! Pour contribuer, suivez ces étapes :
1. Forkez le dépôt.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`).
3. Commitez vos modifications (`git commit -m 'Add some AmazingFeature'`).
4. Poussez la branche (`git push origin feature/AmazingFeature`).
5. Ouvrez une Pull Request.

Nous espérons que vous apprécierez jouer à PythQuest et contribuer à son développement !