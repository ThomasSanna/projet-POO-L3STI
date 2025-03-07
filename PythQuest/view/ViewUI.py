import tkinter as tk
from tkinter import ttk
import time

class ViewUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PythQuest")
        self.root.geometry("1200x900")
        self.root.configure(bg="#2b2b2b")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#2b2b2b")
        style.configure("TLabel", background="#2b2b2b", foreground="#e0e0e0", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10), padding=5)

        # Variables du jeu (inchangées)
        self.piece = tk.IntVar(value=0)
        self.vie = tk.IntVar(value=100)
        self.niveau = tk.IntVar(value=1)
        self.experience = tk.IntVar(value=0)

        # Frame du haut pour les stats (inchangé)
        self.statsFrame = ttk.Frame(root, relief="raised", borderwidth=2)
        self.statsFrame.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10, fill=tk.X)

        self.pieceLabel = ttk.Label(self.statsFrame, text=f"Pièces: {self.piece.get()}", foreground="#ffd700")
        self.pieceLabel.grid(row=0, column=0, padx=10, pady=5)
        
        self.vieLabel = ttk.Label(self.statsFrame, text=f"Vie: {self.vie.get()}", foreground="#ff4040")
        self.vieLabel.grid(row=0, column=1, padx=10, pady=5)
        
        self.niveauLabel = ttk.Label(self.statsFrame, text=f"Niveau: {self.niveau.get()} ({self.experience.get()}/{self.niveau.get() * 100})", foreground="#40c4ff")
        self.niveauLabel.grid(row=0, column=2, padx=10, pady=5)

        # Frame pour la quête associée (inchangé)
        self.questFrame = ttk.Frame(root, relief="raised", borderwidth=2)
        self.questFrame.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

        self.questLabel = ttk.Label(self.questFrame, text="Quête: Aucune", foreground="#ffffff", font=("Arial", 11, "bold"))
        self.questLabel.grid(row=0, column=0, padx=10, pady=5)
        
        self.monsterLabel = ttk.Label(self.questFrame, text="", foreground="#ff7043")
        self.monsterLabel.grid(row=1, column=0, padx=10, pady=2)
        
        self.dungeonLabel = ttk.Label(self.questFrame, text="", foreground="#66bb6a")
        self.dungeonLabel.grid(row=2, column=0, padx=10, pady=2)

        # Frame central pour les images (inchangé)
        self.imageFrame = ttk.Frame(root, relief="sunken", borderwidth=2)
        self.imageFrame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Frame pour les messages (inchangé)
        self.messageFrame = ttk.Frame(root, height=100, relief="groove", borderwidth=2)
        self.messageFrame.pack_propagate(False)
        self.messageFrame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=(0, 10))
        self.activeMessages = []

        # Frame pour les choix avec scrollbar
        self.choicesFrame = ttk.Frame(root)
        self.choicesFrame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        # Ajout d'un Canvas et d'une Scrollbar
        self.choicesCanvas = tk.Canvas(self.choicesFrame, bg="#2b2b2b", highlightthickness=0)
        self.choicesScrollbar = ttk.Scrollbar(self.choicesFrame, orient="vertical", command=self.choicesCanvas.yview)
        self.choicesCanvas.configure(yscrollcommand=self.choicesScrollbar.set)

        # Frame interne pour les boutons
        self.choicesInnerFrame = ttk.Frame(self.choicesCanvas)
        self.choicesCanvas.create_window((0, 0), window=self.choicesInnerFrame, anchor="nw")

        # Placement du Canvas et de la Scrollbar
        self.choicesCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.choicesScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configuration du défilement avec la molette
        self.choicesCanvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # Configuration des boutons (inchangée)
        style.configure("TButton", background="#424242", foreground="#ffffff")
        style.map("TButton", background=[("active", "#616161")])

    # Méthode pour gérer le défilement avec la molette
    def _on_mousewheel(self, event):
        self.choicesCanvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # Méthode pour afficher des choix (modifiée)
    def showChoices(self, choicesList):
        # Supprimer les anciens widgets
        for widget in self.choicesInnerFrame.winfo_children():
            widget.destroy()

        # Ajouter les nouveaux boutons
        for choice in choicesList:
            btn = ttk.Button(self.choicesInnerFrame, text=choice["text"], command=choice["command"])
            btn.pack(pady=3, fill=tk.X)

        # Mettre à jour la région défilable
        self.choicesInnerFrame.update_idletasks()
        self.choicesCanvas.configure(scrollregion=self.choicesCanvas.bbox("all"))

    # Autres méthodes inchangées (updatePiece, updateVie, etc.)
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

    def showMessage(self, message):
        msgLabel = ttk.Label(self.messageFrame, text=message, foreground="#b0bec5", font=("Arial", 9, "italic"))
        msgLabel.pack(anchor=tk.W, padx=10, pady=2)
        self.activeMessages.append(msgLabel)
        self.root.after(3000, lambda: self.removeMessage(msgLabel))

    def removeMessage(self, msgLabel):
        if msgLabel in self.activeMessages:
            msgLabel.destroy()
            self.activeMessages.remove(msgLabel)

    def afficherMonstre(self, nom, vie, arme):
        for widget in self.imageFrame.winfo_children():
            widget.destroy()

        nomLabel = ttk.Label(self.imageFrame, text=f"{nom}", font=("Arial", 14, "bold"), foreground="#ffca28")
        nomLabel.pack(pady=5)
        
        vieLabel = ttk.Label(self.imageFrame, text=f"Vie: {vie}", foreground="#ff4040")
        vieLabel.pack(pady=5)
        
        armeLabel = ttk.Label(self.imageFrame, text=f"Possède {arme}", foreground="#ffffff")
        armeLabel.pack(pady=5)

        try:
            self.monster_image = tk.PhotoImage(file="view/assets/monstre/zombie.png").subsample(3, 3)
            imageLabel = ttk.Label(self.imageFrame, image=self.monster_image)
            imageLabel.pack(pady=2)
        except tk.TclError:
            ttk.Label(self.imageFrame, text="[Image indisponible]", foreground="#757575").pack(pady=10)

    def supprimerMonstre(self):
        for widget in self.imageFrame.winfo_children():
            widget.destroy()

    def updateMonstre(self, vie):
        for widget in self.imageFrame.winfo_children():
            if "Vie" in widget.cget("text"):
                widget.config(text=f"Vie: {vie}")
                break

    def updateQuestInfo(self, quete=None):
        if quete:
            self.questLabel.config(text=f"Quête: {quete.getNom()}")
            self.monsterLabel.config(text=f"Monstre: {quete.getMonstreCible().getNom()}")
            self.dungeonLabel.config(text=f"Donjon: {quete.getDonjonAssocie().getNom()}")
        else:
            self.questLabel.config(text="Quête: Aucune")
            self.monsterLabel.config(text="")
            self.dungeonLabel.config(text="")