from configdb.database import getDbConnection
import bcrypt  # Import de bcrypt

class CombattantDAO:
    @staticmethod
    def authenticate(email: str, password: str) -> dict:
        """
        Authentifie un utilisateur en vérifiant ses identifiants.

        :param email: Email de l'utilisateur
        :param password: Mot de passe de l'utilisateur
        :return: Dictionnaire contenant les informations du combattant si authentifié, sinon None
        """
        conn = getDbConnection()
        cursor = conn.cursor(dictionary=True)  # Utilisation d'un DictCursor
        query = "SELECT * FROM Combattant WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result and bcrypt.checkpw(password.encode('utf-8'), result['motDePasse'].encode('utf-8')):
            return result
        return None  

    @staticmethod
    def register(name: str, email: str, password: str) -> dict:
        """
        Enregistre un nouvel utilisateur.

        :param name: Nom de l'utilisateur
        :param email: Email de l'utilisateur
        :param password: Mot de passe de l'utilisateur
        :return: Dictionnaire contenant les informations du combattant enregistré, sinon None
        """
        conn = getDbConnection()
        cursor = conn.cursor(dictionary=True)
        try:
            # Hachage du mot de passe
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            query = "INSERT INTO Combattant (nom, email, motDePasse) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, hashed_password))
            conn.commit()
            query = "SELECT id, nom FROM Combattant WHERE email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            return result
        except Exception:
            conn.rollback()
            return None 
        finally:
            cursor.close()
            conn.close()