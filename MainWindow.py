from PyQt5.QtWidgets import QMainWindow, QMessageBox
from UserInterface import Ui_Form
from datastore import DataStore
import datetime
ds = DataStore()

class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
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
        self.ui.Remove_Patient_Button.clicked.connect(self.Remove_Patient)
        self.ui.List_Of_Patients_button.clicked.connect(self.ShowListOfPatients)
        self.ui.Search_Patients_Button.clicked.connect(self.SearchPatients)

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

    def Home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

    def Patients(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Patients)
    
    def Remove_Patient(self):
        pass

    def ShowListOfPatients(self):
        List = DataStore.ListOfPatients()
        self.ui.List_Of_Patients_Label.setText(List)

    def SearchPatients(self):
        pass