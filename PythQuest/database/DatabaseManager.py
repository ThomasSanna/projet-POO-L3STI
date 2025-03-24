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
  