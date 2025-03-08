import tkinter as tk
from tkinter import ttk
import time
from PIL import Image, ImageTk

class View:
    """
    Classe représentant la vue du jeu
    Cette classe ne doit pas utiliser de méthodes de contrôleur
    
    Attributs:
        root (tk.Tk): Fenêtre principale de l'application
        piece (tk.IntVar): Pièces du joueur
        vie (tk.IntVar): Vie du joueur
        niveau (tk.IntVar): Niveau du joueur
        experience (tk.IntVar): Expérience du joueur
        armeEquipee (tk.StringVar): Arme équipée par le joueur
        statsFrame (ttk.Frame): Frame pour les statistiques
        pieceLabel (ttk.Label): Label pour les pièces
        vieLabel (ttk.Label): Label pour la vie
        niveauLabel (ttk.Label): Label pour le niveau
        armeLabel (ttk.Label): Label pour l'arme équipée
        questFrame (ttk.Frame): Frame pour la quête
        questLabel (ttk.Label): Label pour le nom de la quête
        monsterLabel (ttk.Label): Label pour le monstre de la quête
        dungeonLabel (ttk.Label): Label pour le donjon de la quête
        imageFrame (ttk.Frame): Frame pour les images
        messageFrame (ttk.Frame): Frame pour les messages
        activeMessages (list): Liste des messages actifs
        choicesFrame (ttk.Frame): Frame pour les choix
        choicesCanvas (tk.Canvas): Canvas pour les choix
        choicesScrollbar (ttk.Scrollbar): Scrollbar pour les choix
        choicesInnerFrame (ttk.Frame): Frame interne pour les boutons
        monsterImage (tk.PhotoImage): Image du monstre
    """
    
    def __init__(self, root):
        """
        Initialise la vue du jeu
        
        :param root: Fenêtre principale de l'application
        """
        self.root = root
        self.root.title("PythQuest")
        self.root.geometry("1200x900")
        self.root.configure(bg="#2b2b2b")
        
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.quit()) 

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
        self.armeEquipee = tk.StringVar(value="Poings (5 dgts)")

        # Frame du haut pour les stats (inchangé)
        self.statsFrame = ttk.Frame(root, relief="raised", borderwidth=2)
        self.statsFrame.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10, fill=tk.X)

        self.pieceLabel = ttk.Label(self.statsFrame, text=f"Pièces: {self.piece.get()}", foreground="#ffd700")
        self.pieceLabel.grid(row=0, column=0, padx=10, pady=5)
        
        self.vieLabel = ttk.Label(self.statsFrame, text=f"Vie: {self.vie.get()}", foreground="#ff4040")
        self.vieLabel.grid(row=0, column=1, padx=10, pady=5)
        
        self.niveauLabel = ttk.Label(self.statsFrame, text=f"Niveau: {self.niveau.get()} ({self.experience.get()}/{self.niveau.get() * 100})", foreground="#40c4ff")
        self.niveauLabel.grid(row=0, column=2, padx=10, pady=5)

        self.armeLabel = ttk.Label(self.statsFrame, text=f"Arme équipée: {self.armeEquipee.get()}", foreground="#ffffff")
        self.armeLabel.grid(row=0, column=3, padx=10, pady=5)

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
        self.choicesCanvas.bind("<MouseWheel>", self._on_mousewheel)

        # Configuration des boutons (inchangée)
        style.configure("TButton", background="#424242", foreground="#ffffff")
        style.map("TButton", background=[("active", "#616161")])

    def _on_mousewheel(self, event):
        """
        Gère le défilement du Canvas avec la molette de la souris
        
        :param event: Événement de la molette de la souris
        """
        self.choicesCanvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def showChoices(self, choicesList):
        """
        Affiche une liste de choix sous forme de boutons
        
        :param choicesList: Liste de dictionnaires contenant le texte et la commande de chaque choix
        """
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

    def updatePiece(self, amount):
        """
        Met à jour le nombre de pièces du joueur
        
        :param amount: Nouveau montant de pièces
        """
        self.piece.set(amount)
        self.pieceLabel.config(text=f"Pièces: {self.piece.get()}")

    def updateVie(self, amount):
        """
        Met à jour la vie du joueur
        
        :param amount: Nouveau montant de vie
        """
        self.vie.set(amount)
        self.vieLabel.config(text=f"Vie: {self.vie.get()}")

    def updateNiveau(self, niveau, experience):
        """
        Met à jour le niveau et l'expérience du joueur
        
        :param niveau: Nouveau niveau du joueur
        :param experience: Nouvelle expérience du joueur
        """
        self.niveau.set(niveau)
        self.experience.set(experience)
        self.niveauLabel.config(text=f"Niveau: {self.niveau.get()} ({self.experience.get()}/{self.niveau.get() * 100})")

    def updateArmeEquipee(self, armeNom, armeDgt):
        """
        Met à jour l'arme équipée par le joueur
        
        :param armeNom: Nom de la nouvelle arme équipée
        :param armeDgt: Dégâts de la nouvelle arme équipée
        """
        self.armeEquipee.set(f"{armeNom} ({armeDgt} dgts)")
        self.armeLabel.config(text=f"Arme équipée: {self.armeEquipee.get()}")

    def showMessage(self, message):
        """
        Affiche un message dans la frame dédiée
        
        :param message: Message à afficher
        """
        msgLabel = ttk.Label(self.messageFrame, text=message, foreground="#b0bec5", font=("Arial", 9, "italic"))
        msgLabel.pack(anchor=tk.W, padx=10, pady=2)
        self.activeMessages.append(msgLabel)
        self.root.after(3000, lambda: self.removeMessage(msgLabel))
    
    def showChoicesWithImages(self, choicesList):
        """
        Affiche une liste de choix avec des images au dessus des boutons
        
        :param choicesList: Liste de dictionnaires contenant le texte, l'image et la commande de chaque choix
        """
        # Supprimer les anciens widgets
        for widget in self.choicesInnerFrame.winfo_children():
            widget.destroy()

        # Ajouter les choix avec images et boutons
        for choice in choicesList:
            frame = ttk.Frame(self.choicesInnerFrame)
            frame.pack(pady=3, fill=tk.X)

            try:
                # Redimensionner l'image et la convertir pour Tkinter
                resizedImage = choice["image"].resize((50, 50), Image.Resampling.LANCZOS)
                photoImage = ImageTk.PhotoImage(resizedImage)
                
                # Créer un label pour l'image
                imageLabel = ttk.Label(frame, image=photoImage)
                imageLabel.image = photoImage  # Garder une référence pour éviter la garbage collection
                imageLabel.pack(side=tk.TOP, pady=5)
            except Exception:
                pass

            # Créer un bouton avec le texte et la commande
            btn = ttk.Button(frame, text=choice["text"], command=choice["command"])
            btn.pack(side=tk.BOTTOM, fill=tk.X)

        # Mettre à jour la région de défilement
        self.choicesInnerFrame.update_idletasks()
        self.choicesCanvas.configure(scrollregion=self.choicesCanvas.bbox("all"))
        self.choicesCanvas.yview_moveto(0)  # Remettre le défilement en haut
        
    def removeMessage(self, msgLabel):
        """
        Supprime un message de la frame dédiée
        
        :param msgLabel: Label du message à supprimer
        """
        if msgLabel in self.activeMessages:
            msgLabel.destroy()
            self.activeMessages.remove(msgLabel)

    def afficherMonstre(self, nom, vie, arme):
        """
        Affiche les informations d'un monstre
        
        :param nom: Nom du monstre
        :param vie: Vie du monstre
        :param arme: Arme du monstre
        """
        for widget in self.imageFrame.winfo_children():
            widget.destroy()

        nomLabel = ttk.Label(self.imageFrame, text=f"{nom}", font=("Arial", 14, "bold"), foreground="#ffca28")
        nomLabel.pack(pady=5)
        
        vieLabel = ttk.Label(self.imageFrame, text=f"Vie: {vie}", foreground="#ff4040")
        vieLabel.pack(pady=5)
        
        armeLabel = ttk.Label(self.imageFrame, text=f"Possède {arme}", foreground="#ffffff")
        armeLabel.pack(pady=5)

        try:
            self.monsterImage = tk.PhotoImage(file="view/assets/monstre/zombie.png").subsample(3, 3)
            imageLabel = ttk.Label(self.imageFrame, image=self.monsterImage)
            imageLabel.pack(pady=2)
        except tk.TclError:
            ttk.Label(self.imageFrame, text="[Image indisponible]", foreground="#757575").pack(pady=10)

    def supprimerMonstre(self):
        """
        Supprime les informations du monstre affiché pour y laisser un espace vide
        """
        for widget in self.imageFrame.winfo_children():
            widget.destroy()

    def updateMonstre(self, vie):
        """
        Met à jour la vie du monstre à afficher
        
        :param vie: Nouvelle vie du monstre
        """
        for widget in self.imageFrame.winfo_children():
            if "Vie" in widget.cget("text"):
                widget.config(text=f"Vie: {vie}")
                break

    def updateQuestInfo(self, quete=None):
        """
        Met à jour les informations de la quête en cours du combattant
        
        :param quete: Quête à afficher
        """
        if quete:
            self.questLabel.config(text=f"Quête: {quete.getNom()}")
            self.monsterLabel.config(text=f"Monstre: {quete.getMonstreCible().getNom()}")
            self.dungeonLabel.config(text=f"Donjon: {quete.getDonjonAssocie().getNom()}")
        else:
            self.questLabel.config(text="Quête: Aucune")
            self.monsterLabel.config(text="")
            self.dungeonLabel.config(text="")