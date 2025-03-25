import tkinter as tk
from controller.ControllerAuth import ControllerAuth
from controller.Controller import Controller

def startGame():
    root.destroy()  # Ferme la fenêtre d'authentification
    gameRoot = tk.Tk()
    gameRoot.title("PythQuest")
    Controller(gameRoot)  # Lance le jeu
    gameRoot.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Authentification - PythQuest")
    ControllerAuth(root, startGame)
    root.mainloop()