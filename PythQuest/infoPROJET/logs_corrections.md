# Logs de Corrections de bug / Ajustements dans le jeu depuis la V1

## Corrections de bugs

- Correction du fait que le joueur pouvait battre un montre qui appartenait à une quête non-associée, sans que la quête ne soit notée comme "Terminée".
- Optimisation de la création de donjon
  - Empecher la création d'un donjon qui possède la même difficulté qu'un donjon déjà en cours.
- Correction du fait que le combat contre un monstre d'une quête associée ne se terminait pas correctement.
- Affichage de la récompense or de la quête, affichage de la récompense d'arme et d'or lorsqu'on bat un monstre.
- Correction du fait que le joueur n'arrivait pas à fuir un donjon.
- Correction du fait que le joueur pouvat avoir une valeure négative d'experiences lors d'un passage de niveau.
- Correction de certaines méthodes dans Forgeron et Combattant qui utilisaient encore des print() pour afficher des informations.

## Ajustements/Rééquilibrage

- Baisse de la récompense d'or des monstres de ~20%.
- Baisse des dégats des monstres (3 à 10 -> 2 à 5 (évoluant avec la difficulté et le niveau du joueur)).
- Baisse de la vie maximale obtenue lors d'un passage de niveau, qui était beaucoup trop élevée au fil du temps (VieMax * 1.5 -> VieMax + 100).
- Augmentation du prix des armes chez le forgeron de ~50%.

# Logs de Corrections de bug / Ajustements dans le jeu de la V2 à la V3

## Corrections de bugs

- Correction du fait que les données sur l'écran ne se mettaient pas à jour lors d'un certain cas à l'achat de potion et de vie.

## Ajustements/Rééquilibrage

- Baisse de la scalabilité des dégats des montres selon le niveau du joueur (Dégats * niveau -> Dégats * sqrt(niveau)).
- Baisse de la scalabilité des dégats des montres selon la difficulé du donjon (Dégats * difficulte -> Dégats * sqrt(difficulte)).
- Baisse de la scalabilité de l'or des monstres selon le niveau du joueur (Or * niveau -> Or * sqrt(niveau)).