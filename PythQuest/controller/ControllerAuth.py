from configdb.database import getDbConnection
from tkinter import messagebox

class ControllerAuth:
    def __init__(self, root, onLoginSuccess):
        """
        :param root: Fenêtre principale Tkinter
        :param onLoginSuccess: Callback à appeler après une connexion réussie
        """
        from view.ViewAuth import ViewAuth
        self.view = ViewAuth(root, self)
        self.onLoginSuccess = onLoginSuccess

    def login(self, email, password):
        conn = getDbConnection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id, nom FROM combattant WHERE email = %s AND motDePasse = %s", (email, password))
            user = cursor.fetchone()
            if user:
                messagebox.showinfo("Connexion réussie", f"Bienvenue, {user[1]}!")
                self.onLoginSuccess(user[0], user[1])  # Passe l'ID et le nom de l'utilisateur
            else:
                messagebox.showerror("Erreur", "Email ou mot de passe incorrect.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue: {e}")
        finally:
            cursor.close()
            conn.close()

    def register(self, name, email, password):
        conn = getDbConnection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO combattant (nom, email, motDePasse) VALUES (%s, %s, %s)", (name, email, password))
            conn.commit()
            messagebox.showinfo("Inscription réussie", "Votre compte a été créé avec succès.")
            self.login(email, password)  # Connecte automatiquement après l'inscription
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue: {e}")
        finally:
            cursor.close()
            conn.close()