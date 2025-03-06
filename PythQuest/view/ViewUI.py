import tkinter as tk
from tkinter import ttk
import time

class ViewUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PythQuest")
        self.root.geometry("800x600")

        # Variables du jeu
        self.piece = tk.IntVar(value=0)
        self.vie = tk.IntVar(value=100)
        self.niveau = tk.IntVar(value=1)
        self.experience = tk.IntVar(value=0)

        # Frame du haut pour les stats
        self.statsFrame = ttk.Frame(root)
        self.statsFrame.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

        # Labels pour les stats
        self.pieceLabel = ttk.Label(self.statsFrame, 
                                   text=f"Pièces: {self.piece.get()}")
        self.pieceLabel.grid(row=0, column=0, padx=5)
        
        self.vieLabel = ttk.Label(self.statsFrame, 
                                    text=f"Vie: {self.vie.get()}")
        self.vieLabel.grid(row=0, column=1, padx=5)
        
        self.niveauLabel = ttk.Label(self.statsFrame, 
                                   text=f"Niveau: {self.niveau.get()} ({self.experience.get()}/{self.niveau.get() * 100})")
        self.niveauLabel.grid(row=0, column=2, padx=5)

        # Frame central pour les images (vide pour l'instant)
        self.imageFrame = ttk.Frame(root)
        self.imageFrame.pack(expand=True, fill=tk.BOTH)

        # Frame pour les messages
        self.messageFrame = ttk.Frame(root, height=100)
        self.messageFrame.pack_propagate(False)  # Empêche la frame de s'ajuster à la taille de son contenu
        self.messageFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=(0, 10))
        
        # Liste pour stocker les messages actifs
        self.activeMessages = []

        # Frame pour les choix
        self.choicesFrame = ttk.Frame(root)
        self.choicesFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

    # Méthodes de mise à jour des stats
    def updatePiece(self, amount):
        self.piece.set(amount)
        self.pieceLabel.config(text=f"Pièces: {self.piece.get()}")

    def updateVie(self, amount):
        self.vie.set(amount)
        self.vieLabel.config(text=f"Vie: {self.vie.get()}")

    def updateNiveau(self, niveau, experience):
        self.niveau.set(niveau)
        self.experience.set(experience)
        self.niveauLabel.config(text=f"Niveau: {self.niveau.get()} ({self.experience.get()}/{self.niveau.get() * 100})")

    # Méthode pour afficher un message temporaire
    def showMessage(self, message):
        # Créer un nouveau label pour le message
        msgLabel = ttk.Label(self.messageFrame, text=message)
        msgLabel.pack(anchor=tk.W, padx=10)
        
        # Ajouter à la liste des messages actifs
        self.activeMessages.append(msgLabel)
        
        # Supprimer le message après 3 secondes
        self.root.after(3000, lambda: self.removeMessage(msgLabel))

    # Méthode pour supprimer un message
    def removeMessage(self, msgLabel):
        if msgLabel in self.activeMessages:
            msgLabel.destroy()
            self.activeMessages.remove(msgLabel)

    # Méthode pour afficher des choix
    def showChoices(self, choicesList):
        # Nettoyer les choix précédents
        for widget in self.choicesFrame.winfo_children():
            widget.destroy()

        # Ajouter les nouveaux boutons de choix
        for i, choice in enumerate(choicesList):
            btn = ttk.Button(self.choicesFrame, 
                           text=choice["text"],
                           command=choice["command"])
            btn.pack(pady=2)