from configdb.database import getDbConnection
import bcrypt  # Import de bcrypt

class CombattantDAO:
    
    def __init__(self):
        """
        Initialise la connexion à la base de données et le curseur.
        """
        self.conn = getDbConnection()
        self.cursor = self.conn.cursor(dictionary=True)
    
    @staticmethod
    def authenticate(email: str, password: str) -> dict:
        """
        Authentifie un utilisateur en vérifiant ses identifiants.

        :param email: Email de l'utilisateur
        :param password: Mot de passe de l'utilisateur
        :return: Dictionnaire contenant les informations du combattant si authentifié, sinon None
        """
        conn = getDbConnection()
        cursor = conn.cursor(dictionary=True)
        
        query = "SELECT * FROM Combattant WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        """
        Pourquoi utf-8 ? Il y aura un problème si on n'utilise pas un caractere utf-8 dans le mdp ?
        On utilise utf-8 pour s'assurer que les chaînes de caractères sont correctement encodées et décodées.
        Si notre mdp contient des caractères hors UTF-8 comme "é" ou "ç", on aura un problème.
        """
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
            # Vérification de l'existence de l'email
            query = "SELECT * FROM Combattant WHERE email = %s"
            cursor.execute(query, (email,))
            if cursor.fetchone():
                return None  # Email déjà utilisé

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
            
    def saveCombattant(self, combattant: 'Combattant') -> None:
        """
        Enregistre les informations d'un combattant dans la base de données.

        :param combattant: Dictionnaire contenant les informations du combattant
        """
        self.conn = getDbConnection()
        self.cursor = self.conn.cursor(dictionary=True)
        try:
            query = "UPDATE Combattant SET piece = %s, vie = %s, maxVie = %s, niveau = %s, experience = %s, inventairePotions = %s, armeEquipee_id = %s WHERE id = %s"
            self.cursor.execute(query, (combattant.getOr(), 
                                        combattant.getVie(), 
                                        combattant.getMaxVie(), 
                                        combattant.getNiveau(), 
                                        combattant.getExperience(), 
                                        combattant.getInventairePotions(), 
                                        combattant.getArmeEquipee().getId(),
                                        combattant.getId()))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            self.cursor.close()
            self.conn.close()
            
    def getArmeEquipeeId(self, idCombattant: int) -> int:
        """
        Récupère l'ID de l'arme équipée d'un combattant.

        :param idCombattant: ID du combattant
        :return: ID de l'arme équipée
        """
        self.conn = getDbConnection()
        self.cursor = self.conn.cursor(dictionary=True)
        
        try:
            query = "SELECT armeEquipee_id FROM Combattant WHERE id = %s"
            self.cursor.execute(query, (idCombattant,))
            result = self.cursor.fetchone()
            return result['armeEquipee_id'] if result else None
        except Exception as e:
            raise e
        finally:
            self.cursor.close()
            self.conn.close()