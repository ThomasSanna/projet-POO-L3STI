Vous avez raison, il est préférable de séparer la logique de la base de données de la logique métier pour des raisons de sécurité, de maintenabilité et de testabilité. Nous pouvons créer une classe dédiée à la gestion de la sauvegarde et du chargement des données, appelée par exemple `DatabaseManager`.

Voici comment vous pouvez structurer cela :

1. **Créer la classe `DatabaseManager`**:
   ```py
   // filepath: c:\Users\thoma\Desktop\programmes\L3STI\Semestre 2\projetPOO-Cours-Projet\projet-POO-L3STI\PythQuest\database\DatabaseManager.py
   from database import get_db_connection
   from models.Combattant import Combattant
   from models.Arme import Arme
   from models.Quete import Quete
   from models.Donjon import Donjon
   from models.Monstre import Monstre
   from models.Forgeron import Forgeron
   from models.Medecin import Medecin

   class DatabaseManager:
       @staticmethod
       def save_combattant(combattant: Combattant):
           conn = get_db_connection()
           cursor = conn.cursor()
           cursor.execute("""
               INSERT INTO Combattant (email, motDePasse, nom, piece, vie, maxVie, niveau, experience, inventairePotions, armeEquipee_id, queteActuelle_id)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               ON DUPLICATE KEY UPDATE
               email=VALUES(email), motDePasse=VALUES(motDePasse), nom=VALUES(nom), piece=VALUES(piece), vie=VALUES(vie), maxVie=VALUES(maxVie), niveau=VALUES(niveau), experience=VALUES(experience), inventairePotions=VALUES(inventairePotions), armeEquipee_id=VALUES(armeEquipee_id), queteActuelle_id=VALUES(queteActuelle_id)
           """, (combattant.email, combattant.motDePasse, combattant.nom, combattant.piece, combattant.vie, combattant.maxVie, combattant.niveau, combattant.experience, combattant.inventairePotions, combattant.armeEquipee_id, combattant.queteActuelle_id))
           conn.commit()
           cursor.close()
           conn.close()

       @staticmethod
       def load_combattant(id: int) -> Combattant:
           conn = get_db_connection()
           cursor = conn.cursor()
           cursor.execute("SELECT * FROM Combattant WHERE id = %s", (id,))
           row = cursor.fetchone()
           cursor.close()
           conn.close()
           if row:
               return Combattant(*row)
           return None

       # Similar methods for Arme, Quete, Donjon, Monstre, Forgeron, Medecin...
   ```

2. **Modifier les classes pour utiliser `DatabaseManager`**:
   ```py
   // filepath: c:\Users\thoma\Desktop\programmes\L3STI\Semestre 2\projetPOO-Cours-Projet\projet-POO-L3STI\PythQuest\models\Combattant.py
   from database.DatabaseManager import DatabaseManager

   class Combattant(Personnage):
       # ...existing code...

       def save(self):
           DatabaseManager.save_combattant(self)

       @staticmethod
       def load(id):
           return DatabaseManager.load_combattant(id)

       # ...existing code...
   ```

3. **Utiliser `DatabaseManager` dans le contrôleur**:
   ```py
   // filepath: c:\Users\thoma\Desktop\programmes\L3STI\Semestre 2\projetPOO-Cours-Projet\projet-POO-L3STI\PythQuest\controller\Controller.py
   from database.DatabaseManager import DatabaseManager

   class Controller:
       # ...existing code...

       def sauvegarderPartie(self):
           self.joueur.save()
           # Save other entities if needed

       def chargerPartie(self, id: int):
           self.joueur = Combattant.load(id)
           # Load other entities if needed

       # ...existing code...
   ```

Cette approche permet de centraliser la gestion des interactions avec la base de données dans une seule classe, `DatabaseManager`, ce qui rend le code plus propre et plus facile à maintenir.