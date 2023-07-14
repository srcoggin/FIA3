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

    def add_user(self, first_name, surname, age):
        self.cursor.execute(
            """
                INSERT INTO User (firstName, surname, age)
                VALUES (:first_name, :surname, :age)
            """,
            {'first_name': first_name, 'surname': surname, "age": age}
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