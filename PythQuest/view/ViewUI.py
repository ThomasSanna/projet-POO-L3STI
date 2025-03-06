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
                                   text=f"Niveau: {self.niveau.get()}")
        self.niveauLabel.grid(row=0, column=2, padx=5)

        # Frame central pour les images (vide pour l'instant)
        self.imageFrame = ttk.Frame(root)
        self.imageFrame.pack(expand=True, fill=tk.BOTH)

        # Frame pour les messages
        self.messageFrame = ttk.Frame(root)
        self.messageFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=(0, 10))
        
        # Liste pour stocker les messages actifs
        self.activeMessages = []

        # Frame pour les choix
        self.choicesFrame = ttk.Frame(root)
        self.choicesFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

    # Méthodes de mise à jour des stats
    def updatepiece(self, amount):
        self.piece.set(amount)
        self.pieceLabel.config(text=f"Pièces: {self.piece.get()}")

    def updatevie(self, amount):
        self.vie.set(amount)
        self.vieLabel.config(text=f"Vie: {self.vie.get()}")

    def updateniveau(self, niveau):
        self.niveau.set(niveau)
        self.niveauLabel.config(text=f"Niveau: {self.niveau.get()}")

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

# Exemple d'utilisation
def main():
    root = tk.Tk()
    view = ViewUI(root)

    # Exemple de mise à jour des stats
    view.updatepiece(50)
    view.updatevie(-20)
    view.updateniveau(2)

    # Exemple de messages
    view.showMessage("Vous avez gagné 99 or!")
    root.after(1000, lambda: view.showMessage("Attention, ennemi proche!"))

    # Exemple de choix
    choices = [
        {"text": "Attaquer", "command": lambda: print("Attaque!")},
        {"text": "Fuir", "command": lambda: print("Fuite!")},
        {"text": "Se cacher", "command": lambda: print("Cachette!")}
    ]
    view.showChoices(choices)

    root.mainloop()

if __name__ == "__main__":
    main()