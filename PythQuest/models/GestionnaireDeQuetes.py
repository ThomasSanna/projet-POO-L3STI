from models.Quete import Quete

class GestionnaireDeQuetes:
    """Classe responsible de la gestion et de la création des quêtes dans le jeu."""

    def __init__(self) -> None:
        """
        Initialise un gestionnaire de quêtes.

        Actuellement, aucune donnée n'est stockée dans l'instance, servant uniquement de conteneur pour des méthodes statiques.
        """
        pass

    @staticmethod
    def creerQueteDonjonMonstres(niveauJoueur: int) -> Quete:
        """
        Crée une quête aléatoire basée sur le niveau du joueur.

        :param niveauJoueur: Le niveau du joueur pour adapter la difficulté de la quête.
        :return: Une instance de Quete générée aléatoirement.
        """
        return Quete.creerQueteAleatoire(niveauJoueur)