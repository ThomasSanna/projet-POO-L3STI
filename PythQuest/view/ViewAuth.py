import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

class ViewAuth:
    def __init__(self, root: tk.Tk, controller: "ControllerAuth") -> None:
        """
        Initialise la vue d'authentification.
        :param root: Fenêtre principale Tkinter
        :param controller: Instance du contrôleur d'authentification
        """
        self.root = root
        self.controller = controller
        self.is_register_mode = False

        # Configuration de la fenêtre principale
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f2f5")

        # Frame principale avec style
        self.frame = ttk.Frame(root, padding=20, style="Main.TFrame")
        self.frame.pack(expand=True)

        # Configuration du style
        style = ttk.Style()
        style.configure("Main.TFrame", background="#f0f2f5")
        style.configure("Title.TLabel", font=("Helvetica", 20, "bold"), foreground="#2c3e50")
        style.configure("Field.TLabel", font=("Helvetica", 11), foreground="#34495e")
        style.configure("TButton", font=("Helvetica", 11), padding=8)
        style.configure("TEntry", font=("Helvetica", 11))

        # Titre
        self.titleLabel = ttk.Label(
            self.frame, 
            text="Bienvenue sur PythQuest", 
            style="Title.TLabel"
        )
        self.titleLabel.grid(row=0, column=0, columnspan=2, pady=(0, 30))

        # Email
        self.emailLabel = ttk.Label(self.frame, text="Email :", style="Field.TLabel")
        self.emailLabel.grid(row=1, column=0, sticky=tk.W, pady=10)
        self.emailEntry = ttk.Entry(self.frame, width=30)
        self.emailEntry.grid(row=1, column=1, pady=10, padx=5)

        # Mot de passe
        self.passwordLabel = ttk.Label(self.frame, text="Mot de passe :", style="Field.TLabel")
        self.passwordLabel.grid(row=2, column=0, sticky=tk.W, pady=10)
        self.passwordEntry = ttk.Entry(self.frame, show="*", width=30)
        self.passwordEntry.grid(row=2, column=1, pady=10, padx=5)

        # Nom (caché par défaut)
        self.nameLabel = ttk.Label(self.frame, text="Nom :", style="Field.TLabel")
        self.nameEntry = ttk.Entry(self.frame, width=30)

        # Boutons
        self.button_frame = ttk.Frame(self.frame)
        self.button_frame.grid(row=4, column=0, columnspan=2, pady=20)
        
        self.loginButton = ttk.Button(
            self.button_frame, 
            text="Se connecter", 
            command=self.login,
            style="Accent.TButton"
        )
        self.loginButton.grid(row=0, column=0, padx=5)

        self.registerButton = ttk.Button(
            self.button_frame, 
            text="S'inscrire", 
            command=self.toggle_register,
            style="Accent.TButton"
        )
        self.registerButton.grid(row=0, column=1, padx=5)

        # Style supplémentaire pour les boutons
        style.configure("Accent.TButton", background="#3498db", foreground="#000")
        style.map("Accent.TButton",
                 background=[('active', '#2980b9')],
                 foreground=[('active', '#000')])

    def toggle_register(self):
        """
        Bascule entre le mode inscription et le mode connexion.
        Affiche ou cache le champ de saisie du nom selon le mode actif.
        """
        # Vérifie si le mode inscription est actif
        if not self.is_register_mode:
            # Passage en mode inscription
            self.nameLabel.grid(row=3, column=0, sticky=tk.W, pady=10) # On rend visible le label et l'entry du nom
            self.nameEntry.grid(row=3, column=1, pady=10, padx=5)
            self.loginButton.config(text="Créer un compte", command=self.register)
            self.registerButton.config(text="Se connecter", command=self.toggle_register)
            self.titleLabel.config(text="Inscription à PythQuest")
            self.is_register_mode = True
        else:
            # Retour au mode connexion
            self.nameLabel.grid_remove() # On cache le label et l'entry du nom
            self.nameEntry.grid_remove()
            self.loginButton.config(text="Se connecter", command=self.login)
            self.registerButton.config(text="S'inscrire", command=self.toggle_register)
            self.titleLabel.config(text="Bienvenue sur PythQuest")
            self.is_register_mode = False

    def login(self):
        """
        Authentifie l'utilisateur en récupérant les informations du formulaire de connexion.
        """
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        self.controller.login(email, password)

    def register(self):
        """
        Inscrit l'utilisateur en récupérant les informations du formulaire d'inscription.
        """
        name = self.nameEntry.get()
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        self.controller.register(name, email, password)
        
    def putMessageBox(self, title: str, message: str):
        """Affiche une boîte de message"""
        tkinter.messagebox.showinfo(title, message)
    
    def putErrorBox(self, title: str, message: str):
        """Affiche une boîte d'erreur"""
        tkinter.messagebox.showerror(title, message)

