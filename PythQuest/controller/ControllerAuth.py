from models.Combattant import Combattant
from models.Arme import Arme
from view.ViewAuth import ViewAuth

class ControllerAuth:
    
    # Attributs de classe
    # Utilisé pour stocker le combattant connecté
    combattant = None
  
    def __init__(self, root, onLoginSuccess):
        """
        :param root: Fenêtre principale Tkinter
        :param onLoginSuccess: Callback à appeler après une connexion réussie
        """
        self.view = ViewAuth(root, self)
        self.onLoginSuccess = onLoginSuccess
        

    def login(self, email, password):
        """
        Authentifie un utilisateur en passant par le modèle Combattant.
    
        :param email: Email de l'utilisateur
        :param password: Mot de passe de l'utilisateur
        """
        try:
            combattant = Combattant.authentifier(email, password)
            if combattant:
                ControllerAuth.combattant = combattant
                self.recupDonnees()  
                self.onLoginSuccess()
            else:
                self.view.putErrorBox("Erreur de connexion", "Email ou mot de passe incorrect.")
        except Exception as e:
            self.view.putErrorBox("Erreur", f"Une erreur est survenue : {str(e)}")
    
    def register(self, name, email, password):
        """
        Enregistre un nouvel utilisateur en passant par le modèle Combattant.
    
        :param name: Nom de l'utilisateur
        :param email: Email de l'utilisateur
        :param password: Mot de passe de l'utilisateur
        """
        try:
            combattant = Combattant.inscrire(name, email, password)
            if combattant:
                self.view.putMessageBox("Inscription réussie", "Votre compte a été créé avec succès.")
                ControllerAuth.combattant = combattant
                self.onLoginSuccess()
            else:
                self.view.putErrorBox("Erreur", "Impossible de créer le compte. L'email est peut-être déjà utilisé.")
        except Exception as e:
            self.view.putErrorBox("Erreur", f"Une erreur est survenue : {str(e)}")
            
    def recupDonnees(self):
        try:
            Arme.recupererArmes(ControllerAuth.combattant)
            ControllerAuth.combattant.recupererArmeEquipee()
        except Exception as e:
            self.view.putErrorBox("Erreur", f"Une erreur est survenue lors de la récupération des données : {str(e)}")
        return
        