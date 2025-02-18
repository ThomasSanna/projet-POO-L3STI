class ViewV1:
    def choixConsole(self, message: str) -> str:
        return input(message)

    def afficherMenuPrincipal(self) -> None:
        print("Que voulez-vous faire ?")
        print("1. Faire des achats")
        print("2. Voir les quêtes")
        print("3. Voir les donjons")
        print("4. Informations sur le personnage")
        print("5. Quitter le jeu")

    def afficherMenuPersonnage(self) -> None:
        print("Que voulez-vous faire ?")
        print("1. Changer d'arme")
        print("2. Abandonner la quête")
        print("3. Retour")

    def afficherMessage(self, message: str) -> None:
        print(message)