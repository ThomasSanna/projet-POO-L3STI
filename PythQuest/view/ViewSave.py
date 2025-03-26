from tkinter import messagebox

class ViewSave:
  
    def __init__(self):
        pass
    
    def putMessageBox(self, title, message):
        """
        Affiche une boîte de message avec le titre et le message spécifiés.
        """
        messagebox.showinfo(title, message)
        
    def putErrorBox(self, title, message):
        """
        Affiche une boîte de message d'erreur avec le titre et le message spécifiés.
        """
        messagebox.showerror(title, message)