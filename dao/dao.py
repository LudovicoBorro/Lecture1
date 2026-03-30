import mysql.connector

from dao.dbConnect import DBConnect
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord


class DAO:

    @staticmethod
    def getAllProdotti():
         #   cnx = mysql.connector.connect(
         #      user = "root",
         #      password = "ricercaopforreal!347?",
         #      host = "localhost",
         #      database = "sw_gestionale"
         #   )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM prodotti")
        row = cursor.fetchall()

        res = []
        for p in row:
            res.append(ProdottoRecord(p["nome"], p["prezzo"]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllClienti():
        #   cnx = mysql.connector.connect(
        #      user = "root",
        #      password = "ricercaopforreal!347?",
        #      host = "localhost",
        #      database = "sw_gestionale"
        #   )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("""SELECT * FROM clienti""")
        row = cursor.fetchall()

        res = []
        for p in row:
            res.append(ClienteRecord(p["nome"], p["mail"], p["categoria"]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def addProdotto(prodotto):
        #   cnx = mysql.connector.connect(
        #      user = "root",
        #      password = "ricercaopforreal!347?",
        #      host = "localhost",
        #      database = "sw_gestionale"
        #   )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query = """INSERT INTO prodotti (nome, prezzo) 
                   VALUES (%s, %s)"""
        cursor.execute(query, (prodotto.name, prodotto.prezzo_unitario))

        cnx.commit()
        cursor.close()
        cnx.close()
        return

    @staticmethod
    def addCliente(cliente):
        #   cnx = mysql.connector.connect(
        #      user = "root",
        #      password = "ricercaopforreal!347?",
        #      host = "localhost",
        #      database = "sw_gestionale"
        #   )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query = """INSERT INTO clienti (nome, mail, categoria)
                   VALUES (%s, %s, %s)"""
        cursor.execute(query, (cliente.nome, cliente.mail, cliente.categoria))

        cnx.commit()
        cursor.close()
        cnx.close()
        return

    @staticmethod
    def hasProdotto(prodotto):
        #   cnx = mysql.connector.connect(
        #      user = "root",
        #      password = "ricercaopforreal!347?",
        #      host = "localhost",
        #      database = "sw_gestionale"
        #   )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM prodotti WHERE nome = %s"""
        cursor.execute(query, (prodotto.name,))
        row = cursor.fetchall()

        cursor.close()
        cnx.close()
        return len(row) > 0

    @staticmethod
    def hasCliente(cliente):
        #   cnx = mysql.connector.connect(
        #      user = "root",
        #      password = "ricercaopforreal!347?",
        #      host = "localhost",
        #      database = "sw_gestionale"
        #   )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM clienti WHERE mail = %s"""
        cursor.execute(query, (cliente.mail,))
        row = cursor.fetchall()

        cursor.close()
        cnx.close()
        return len(row) > 0

if __name__ == "__main__":
    mydao = DAO()
    mydao.getAllProdotti()