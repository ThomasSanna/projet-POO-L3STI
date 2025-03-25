import tkinter as tk
from tkinter import ttk

class ViewAuth:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.frame = ttk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        self.titleLabel = ttk.Label(self.frame, text="Bienvenue sur PythQuest", font=("Arial", 16))
        self.titleLabel.grid(row=0, column=0, columnspan=2, pady=10)

        # Email
        self.emailLabel = ttk.Label(self.frame, text="Email:")
        self.emailLabel.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.emailEntry = ttk.Entry(self.frame)
        self.emailEntry.grid(row=1, column=1, pady=5)

        # Mot de passe
        self.passwordLabel = ttk.Label(self.frame, text="Mot de passe:")
        self.passwordLabel.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.passwordEntry = ttk.Entry(self.frame, show="*")
        self.passwordEntry.grid(row=2, column=1, pady=5)

        # Nom (uniquement pour le register)
        self.nameLabel = ttk.Label(self.frame, text="Nom:")
        self.nameEntry = ttk.Entry(self.frame)

        # Boutons
        self.loginButton = ttk.Button(self.frame, text="Se connecter", command=self.login)
        self.loginButton.grid(row=4, column=0, pady=10)
        self.registerButton = ttk.Button(self.frame, text="S'inscrire", command=self.showRegister)
        self.registerButton.grid(row=4, column=1, pady=10)

    def showRegister(self):
        self.nameLabel.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.nameEntry.grid(row=3, column=1, pady=5)
        self.loginButton.config(text="S'inscrire", command=self.register)

    def login(self):
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        self.controller.login(email, password)

    def register(self):
        name = self.nameEntry.get()
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        self.controller.register(name, email, password)
        
    def putMessageBox(self, title, message):
        """
        Affiche une boîte de message avec le titre et le message spécifiés.
        """
        tk.messagebox.showinfo(title, message)
    
    def putErrorBox(self, title, message):
        """
        Affiche une boîte de message d'erreur avec le titre et le message spécifiés.
        """
        tk.messagebox.showerror(title, message)