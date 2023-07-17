from PyQt5.QtWidgets import QMainWindow, QMessageBox
from UserInterface import Ui_Form
from datastore import DataStore
import datetime


class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ds = DataStore()
        self.ui = Ui_Form()
        self.ui.setupUi(self.main_win)
        self.currentTime = datetime.datetime.now()
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

        #Setting the "Good, (INSERT)" at the Home page
        self.EveningMorningButtons()

        #Banner Buttons
        self.ui.Exit_Banner_Button.clicked.connect(self.Exit)
        self.ui.About_Banner_Button.clicked.connect(self.About)
        self.ui.Home_Banner_Button.clicked.connect(self.Home)
        self.ui.Patients_Banner_Button.clicked.connect(self.Patients)


        #Patient Page 1 Buttons
        self.ui.Remove_Patient_Button.clicked.connect(self.delete_patient)
        self.ui.List_Of_Patients_button.clicked.connect(self.ShowListOfPatients)
        self.ui.Search_Patients_Button.clicked.connect(self.SearchPatients)
        self.ui.Next_Page_Button_Patients.clicked.connect(self.NextPagePatients)

        #Patient Page 2 Buttons
        self.ui.Previous_Page_Button_Patients2.clicked.connect(self.Patients)
        self.ui.Add_Patient_Button.clicked.connect(self.add_patient)
        self.ui.Update_Patient_Button.clicked.connect(self.Update_Paitient)
    

    #Opens the Window When Ran
    def show(self):
        self.main_win.show()
    
    #Setting the "Good, (INSERT)" at the Home page
    def EveningMorningButtons(self):
        if self.currentTime.hour < 12:
            self.ui.MorningEvening_Label.setText("Morning")
        elif 12 <= self.currentTime.hour < 18:
            self.ui.MorningEvening_Label.setText("Afternoon")
        else:
            self.ui.MorningEvening_Label.setText("Evening")

    #Exits the program
    def Exit(self):
        exit()

    def About(self):
        msg = QMessageBox()
        # Set the Text and Title of the message box
        msg.setText(f"""
        Thank you for using Fighting Fit Physio! 
        This App was Coded and Developed by Will Coggins 
        This App was Devleoped from 13/07/2023 to (Ongoing)
        Please Enjoy my other works such as:
        Fia1, Fia2 and The Award Winning Indie Program of the year (2023) "Brad". 
        All of which and many more fun and 
        serious Python coded projects can be found on my github: 
        @srcoggin 
        Please follow me, and Star my Repos!""")
        msg.setWindowTitle("About Me!")
        #Sets the message box to include a close button
        msg.setStandardButtons(QMessageBox.Close)
        # Shows the message box
        msg.exec()


    def NextPagePatients(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Patients2)

    def Home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

    def Patients(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Patients)

    def ShowListOfPatients(self):
        List = self.ds.ListOfPatients()
        name = ""
        for i in List:
            name += (f"{i[0]} \n")
        self.ui.List_Of_Patients_Label.setText(f"""
List Of Patients:

{name}                                         
""")

    def SearchPatients(self):
        Patient_Info = self.ds.select_matching_user(int(self.ui.Patient_Id_Search_Patient.text()))
        info = ""
        for i in Patient_Info:
            info += """
Patient Id: {}
Patient Name: {} {}
Patient Height: {}
Patient Weight: {}
Patient Address {}
Num of Treatments Taken: {}
    """.format(i[0], i[4], i[5], i[1], i[2], i[3], i[6])
        self.ui.Search_Patient_Label.setText(f"""                         
Patient Info:                                                                          
{info}                          
""")
        
    def add_patient(self):
        self.ds.Add_Patient(id = self.ui.Add_Patient_Id.text(), FirstName = self.ui.Add_Patient__FirstName.text(), LastName = self.ui.Add_Patient_LastName.text(), Height = self.ui.Add_Patient_Height.text(), Weight = self.ui.Add_Patient_Weight.text(), Address = self.ui.Add_Patient_Address.text(), Amountoftreatmentstaken = self.ui.Add_Num_Of_treat.text())
        self.ui.Add_Patient_Id.clear()
        self.ui.Add_Patient__FirstName.clear()
        self.ui.Add_Patient_LastName.clear()
        self.ui.Add_Patient_Height.clear()
        self.ui.Add_Patient_Weight.clear()
        self.ui.Add_Patient_Address.clear()
        self.ui.Add_Num_Of_treat.clear()
        msg = QMessageBox()
        msg.setWindowTitle("Opersation Completed!")
        msg.setText("Done!")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec()

    def delete_patient(self):
        self.ds.Delete_Patient(id = self.ui.Patient_Id_Remove_Patient.text())
        msg = QMessageBox()
        msg.setWindowTitle("Opersation Completed!")
        msg.setText("Done!")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec()

    def Update_Paitient(self):
        self.ds.update_patient(id = self.ui.Update_Patient_Id.text(), FirstName = self.ui.Update_Patient_FirstName.text(), LastName = self.ui.Update_Patient_LastName.text(), Weight = self.ui.Update_Patient_Weight.text(), Height = self.ui.Update_Patient_Height, Address = self.ui.Update_Patient_Address.text(), Amountoftreatmentstaken = self.ui.Update_Num_Of_Treatments.text())