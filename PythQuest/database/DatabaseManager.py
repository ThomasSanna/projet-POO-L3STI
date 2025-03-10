from database.database import getDbConnection
from models.Combattant import Combattant
from models.Arme import Arme
from models.Quete import Quete
from models.Donjon import Donjon
from models.Monstre import Monstre
from models.Forgeron import Forgeron
from models.Medecin import Medecin

class DatabaseManager:
  
  def __init__(self):
    self.conn = getDbConnection()
    self.cursor = self.conn.cursor() # exécuter des requêtes SQL
    self.id = None
  
  def sEnregistrer(self, username: str, password: str) -> bool:
    """
    Enregistre un utilisateur dans la base de données.
    
    :param username: Le nom d'utilisateur.
    :param password: Le mot de passe.
    :return: True si l'utilisateur a été enregistré, False sinon.
    """
    self.cursor.execute("SELECT * FROM Utilisateur WHERE nomUtilisateur = ?", (username,))
    if self.cursor.fetchone() is not None:
      return False
    self.cursor.execute("INSERT INTO Utilisateur (nomUtilisateur, motDePasse) VALUES (?, ?)", (username, password))
    self.conn.commit()
    return True  