import mysql.connector

def getDbConnection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="pythquest",
    )


def testDbConnection():
    try:
        conn = getDbConnection()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("INSERT INTO combattant (email, motDePasse, nom) VALUES ('aaa@gmail.com', 'cqfd', 'pablo')")
            conn.commit()
        conn.close()
    except mysql.connector.Error as err:
        raise err

# Test de la connexion
if __name__ == "__main__":
    testDbConnection()
