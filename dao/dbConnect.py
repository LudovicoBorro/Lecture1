import mysql.connector

class DBConnect:

    @classmethod
    def getConnection(cls):
        try:
            cnx = mysql.connector.connect(
                user = "root",
                password = "ricercaopforreal!347?",
                host = "localhost",
                database = "sw_gestionale"
            )
            return cnx

        except mysql.connector.Error as err:
            print("Non riesco a collegarmi al db")
            print(err)
            return None