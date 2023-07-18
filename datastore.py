import os
import sqlite3


class DataStore:
    def __init__(self):
        self.db_file = os.path.join(os.getcwd(), "FIA3.db")
        self.db = sqlite3.connect(r"C:\Users\Will\Documents\GitHub\FIA3\FIA3.db")
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()


    def ListOfTreatments(self):
        self.cursor.execute(
            """
                SELECT TreatmentName, Id FROM Treatment
            """
        )
        QList = self.cursor.fetchall()
        return QList

    def Matching_Treatment_id(self):
        self.cursor.execute(
            """
                SELECT id FROM Treatment
            """
        )
        QList = self.cursor.fetchall()
        id = ""
        for i in QList:
            id +="{}".format(i)
        return id

    def Matching_Patient_id(self):
        self.cursor.execute(
            """
                SELECT id FROM Patients
            """
        )
        QList = self.cursor.fetchall()
        id = ""
        for i in QList:
            id +="{}".format(i)
        return id

    def select_matching_treatment(self, treatmentid):
        self.cursor.execute(
            """
                SELECT * FROM Treatment
                WHERE Id LIKE :treatmentid
            """,
            {"treatmentid": treatmentid}
        )
        QList = self.cursor.fetchall()
        return QList

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
    

    def Add_Treatment(self, id, TreatmentName, Description, Cost):
        self.cursor.execute(
            """
                INSERT INTO Treatment (id, Cost, Description, TreatmentName)
                VALUES (:id, :Cost, :Description, :TreatmentName)
            """,
            {"id": id, "Cost": Cost, "Description": Description, "TreatmentName": TreatmentName}
        )
        self.db.commit()


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
            SELECT FirstName ||" "|| LastName AS "Name", id FROM Patients
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


    def Delete_Treatment(self, id):
        self.cursor.execute(
            """
                DELETE FROM Treatment
                WHERE (:id) = id
            """,
            {"id": id}
        )
        self.db.commit()



    def update_treatment(self, id, UpdatetdSelection, UpdatedValue):
        if UpdatetdSelection == 1:
            self.cursor.execute(
                """
                    UPDATE Treatment SET Cost = (:UpdatedValue)
                    WHERE (:id) = id
                """,
                {"UpdatedValue": UpdatedValue, "id": id}
            )
            self.db.commit()

        elif UpdatetdSelection == 2:
            self.cursor.execute(
                """
                    UPDATE Treatment SET Description = (:UpdatedValue)
                    WHERE (:id) = id
                """,
                {"UpdatedValue": UpdatedValue, "id": id}
            )
            self.db.commit()

        elif UpdatetdSelection == 3:
            self.cursor.execute(
                """
                    UPDATE Treatment SET TreatmentName = (:UpdatedValue)
                    WHERE (:id) = id
                """,
                {"UpdatedValue": UpdatedValue, "id": id}
            )
            self.db.commit()


    def update_patient(self, id, UpdatedSelection, UpdatedValue):
        print(UpdatedSelection)
        if UpdatedSelection == 1:
            self.cursor.execute(
                """
                    UPDATE Patients SET FirstName = (:UpdatedValue)
                    WHERE (:id) = id
                """,
                {"UpdatedValue": UpdatedValue, "id": id}
            )
            self.db.commit()
        elif UpdatedSelection == 2:
            self.cursor.execute(
                """
                    UPDATE Patients SET LastName = (:UpdatedValue)
                    WHERE (:id) = id
                """,
                {"UpdatedValue": UpdatedValue, "id": id}
            )
            self.db.commit()

        elif UpdatedSelection == 3:
            self.cursor.execute(
                """
                    UPDATE Patients SET Address = (:UpdatedValue)
                    WHERE (:id) = id
                """,
                {"UpdatedValue": UpdatedValue, "id": id}
            )
            self.db.commit()
        elif UpdatedSelection == 4:
            self.cursor.execute(
                """
                    UPDATE Patients SET Height = (:UpdatedValue)
                    WHERE (:id) = id
                """,
                {"UpdatedValue": UpdatedValue, "id": id}
            )
            self.db.commit()
        elif UpdatedSelection == 5:
            self.cursor.execute(
                """
                    UPDATE Patients SET Weight = (:UpdatedValue)
                    WHERE (:id) = id
                """,
                {"UpdatedValue": UpdatedValue, "id": id}
            )
            self.db.commit()
        elif UpdatedSelection == 6:
            self.cursor.execute(
                """
                    UPDATE Patients SET Amountoftreatmentstaken = (:UpdatedValue)
                    WHERE (:id) = id
                """,
                {"UpdatedValue": UpdatedValue, "id": id}
            )
            self.db.commit()