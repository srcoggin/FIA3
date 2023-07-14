import os
import sqlite3


class DataStore:
    def __init__(self):
        self.db_file = os.path.join(os.getcwd(), "FIA3.db")
        self.db = sqlite3.connect(r"C:\Users\Will\Documents\GitHub\FIA3\FIA3.db")
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def select_matching_user(self, patientid):
        self.cursor.execute(
            """
                SELECT * FROM Patients
                WHERE Id LIKE :patientid
    
            """,
            {'patientid': patientid}
        )
        QList = self.cursor.fetchall()
        return QList

    def add_user(self, id, first_name, surname, height, weight, address, numott):
        self.cursor.execute(
            """
                INSERT INTO Patients (id, FirstName, LastName, Height, Weight, Address, amountoftreatmentstaken)
                VALUES (:id, :first_name, :surname, :height, :weight, :address, :numott)
            """,
            {"id": id, "FirstName": first_name, "LastName": surname, "Height": height, "Weight": weight, "Address": address, "amountoftreatmentstaken": numott}
        )
        self.db.commit()

    def ListOfPatients(self):
        self.cursor.execute(
        """
            SELECT FirstName ||" "|| LastName AS "Name" FROM Patients
        """
        )
        QList = self.cursor.fetchall()
        return QList