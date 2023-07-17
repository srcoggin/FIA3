import os
import sqlite3


class DataStore:
    def __init__(self):
        self.db_file = os.path.join(os.getcwd(), "FIA3.db")
        self.db = sqlite3.connect(self.db_file)
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

    def Add_Patient(self, id, FirstName, LastName, Height, Weight, Address, Amountoftreatmentstaken):
        self.cursor.execute(
            """
                INSERT INTO Patients (id, Height, FirstName, LastName, Weight, Address, Amountoftreatmentstaken)
                VALUES (:id, :Height, :FirstName, :LastName, :Weight, :Address, :Amountoftreatmentstaken);
            """,
            {"id": id, "FirstName": FirstName, "LastName": LastName, "Height": Height, "Weight": Weight, "Address": Address, "Amountoftreatmentstaken": Amountoftreatmentstaken}
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
    
    def Delete_Patient(self, id):
        self.cursor.execute(
        """
            DELETE FROM Patients
            WHERE (:id) = id
        """,
        {"id": id}
        )
        self.db.commit()

    def update_patient(self, id, FirstName, LastName, Height, Weight, Address, Amountoftreatmentstaken):
        if FirstName == "" and LastName == "" and Height == "" and Weight == "" and Address == "" and Amountoftreatmentstaken != "":
            self.cursor.execute(
                """
                    UPDATE Patients SET Amountoftreatmentstaken = (:Amountoftreatmentstaken) 
                    WHERE (:id) = id
                """,
                {"Amountoftreatmentstaken": Amountoftreatmentstaken, "id": id}
            )
            self.db.commit()