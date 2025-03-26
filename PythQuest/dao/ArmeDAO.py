from configdb.database import getDbConnection

class ArmeDAO:
  
  def __init__(self):
    """
    Initialise la connexion à la base de données et le curseur.
    """
    self.conn = getDbConnection()
    self.cursor = self.conn.cursor(dictionary=True)
    
  @staticmethod
  def recupAllArmes(idCombattant: int) -> list:
    """
    Récupère toutes les armes d'un combattant à partir de la base de données.
    
    :param idCombattant: ID du combattant dont on veut récupérer les armes
    :return: Liste des armes du combattant
    """
    conn = getDbConnection()
    cursor = conn.cursor(dictionary=True)
    try:
      query = "SELECT * FROM Arme WHERE combattant_id = %s"
      cursor.execute(query, (idCombattant,))
      armes = cursor.fetchall()
      return armes
    except Exception as e:
      raise e
    finally:
      cursor.close()
      conn.close()
  
  def saveArme(self, arme: dict) -> None:
    """
    Enregistre une arme dans la base de données ou met à jour si elle existe déjà.
    
    :param arme: Dictionnaire contenant les informations de l'arme
    """
    try:
      query = """
        INSERT INTO Arme (id, combattant_id, nom, valeurOr, degat, image, inventaire_combattant_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
          nom = VALUES(nom),
          valeurOr = VALUES(valeurOr),
          degat = VALUES(degat),
          image = VALUES(image),
          inventaire_combattant_id = VALUES(inventaire_combattant_id)
      """
      values = (
        arme["id"],
        arme["combattant_id"],
        arme["nom"],
        arme["valeurOr"],
        arme["degat"],
        arme["imageBin"],
        arme["inventaire_combattant_id"]
      )
      self.cursor.execute(query, values)
      self.conn.commit()
    except Exception as e:
      raise e
    finally:
      self.cursor.close()
      self.conn.close()
  
