import mysql.connector

def getDbConnection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="pythquest",
    )

"""
def testDbConnection():
    try:
        print("j'essaie")
        conn = getDbConnection()
        if conn.is_connected():
            print("Connexion réussie à la base de données.")
        else:
            print("Échec de la connexion à la base de données.")
        conn.close()
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")

# Test de la connexion
if __name__ == "__main__":
    testDbConnection()
"""