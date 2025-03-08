from controller.Controller import Controller
import tkinter as tk

def main():
    """
    Fonction principale à lancer pour démarrer le jeu
    """
    root = tk.Tk()
    Controller(root)
    root.mainloop()

if __name__ == "__main__":
    main()