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
        self.ui.Treatments_Banner_Buttons.clicked.connect(self.Treatments)
        self.ui.Appointment_Banner_Buttons.clicked.connect(self.Appointments)


        #Patient Page 1 Buttons
        self.ui.Remove_Patient_Button.clicked.connect(self.delete_patient)
        self.ui.List_Of_Patients_button.clicked.connect(self.ShowListOfPatients)
        self.ui.Search_Patients_Button.clicked.connect(self.SearchPatients)
        self.ui.Next_Page_Button_Patients.clicked.connect(self.NextPagePatients)

        #Patient Page 2 Buttons
        self.ui.Previous_Page_Button_Patients2.clicked.connect(self.Patients)
        self.ui.Add_Patient_Button.clicked.connect(self.add_patient)
        self.ui.Update_Patient_Button.clicked.connect(self.Update_Patient)

        #Treatment Page 1 Buttons
        self.ui.Next_Page_Treatments.clicked.connect(self.NextPageTreatments)
        self.ui.List_Of_Treatments_Button.clicked.connect(self.ShowListOfTreatments)
        self.ui.Search_Treatments_Button.clicked.connect(self.SearchTreatments)
        self.ui.Remove_Treatment_Button.clicked.connect(self.Remove_Treatment)

        #Treatment Page 2 Buttons
        self.ui.Previous_Page_Treatments.clicked.connect(self.Treatments)
        self.ui.Add_Treatment_Button.clicked.connect(self.add_treatment)
        self.ui.Update_Treatment_Button.clicked.connect(self.Update_Treatment)

        #Appointments Page 1 Buttons
        self.ui.List_Of_Appointments_Button.clicked.connect(self.ShowListOfAppointments)  
        self.ui.Next_Page_Appointments.clicked.connect(self.NextPageAppointments)  
        self.ui.Add_Appointment_Button.clicked.connect(self.add_appointment)
        self.ui.Remove_Appointment.clicked.connect(self.Remove_Appointment)

        #Appointments Page 2 Buttons
        self.ui.Previous_Page_Appointments.clicked.connect(self.Appointments)
        self.ui.Search_Appointment_Button.clicked.connect(self.SearchAppointments)


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

    def NextPageAppointments(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Apointmenets_Page2)


    def Appointments(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Appointments)

    #Exits the program
    def Exit(self):
        exit()

    def Treatments(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Treatments)       

    def NextPageTreatments(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Treatments_Page_2) 

    def About(self):
        msg = QMessageBox()
        # Set the Text and Title of the message box
        msg.setText(f"""
        Thank you for using Fighting Fit Physio! 
        This App was Coded and Developed by Will Coggins 
        This App was Devleoped from 13/07/2023 to 19/07/2023
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


    def SearchTreatments(self):
        Treatment_id = self.ui.Treatment_id_Search.text()
        Treatments = self.ds.Matching_Treatment_id()
        if Treatment_id not in Treatments:
            self.error()
        else:
            Treatment_info = self.ds.select_matching_treatment(self.ui.Treatment_id_Search.text())
            info = ""
            for i in Treatment_info:
                info += """
Treatment Id: {}
Treatment Name: {}
Treatment Desc: {}
Treatment Cost: {}
                """.format(i[0], i[3], i[2], i[1])
            self.ui.Search_Treatment_Label.setText(f"""
Treatment Info:
{info}       
""")

    def ShowListOfTreatments(self):
        List = self.ds.ListOfTreatments()
        name = ""
        for i in List:
            name += (f"{i[0]}, Id: {i[1]} \n")
        self.ui.List_Of_Treatments_Label.setText(f"""
List Of Treatments:                   
{name}       
""")
        

    def ShowListOfAppointments(self):
        List = self.ds.ListOfAppointments()
        name = ""
        for i in List:
            name += (f"Id: {i[0]}, Patient Id: {i[1]}, Room Id: {i[2]} \n")
        self.ui.List_Of_Appointments_Label.setText(f"""
List Of Appointments:
{name}                                                                    
""")
        


    def Remove_Appointment(self):
        Appointment_id = self.ui.Remove_Appointment_Id.text()
        Appointments = self.ds.Matching_Appointment_Id()
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are you sure!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_clicked = msg.exec()
        if button_clicked == QMessageBox.Yes:
            if Appointment_id not in Appointments:
                self.error()
            else:
                self.ds.Delete_Appointment(id = self.ui.Remove_Appointment_Id.text())
                self.succesful_popup()
        elif button_clicked == QMessageBox.No:
            QMessageBox.close
        else:
            QMessageBox.close


    def Remove_Treatment(self):
        Treatment_id = self.ui.Remove_Treatment_Id.text()
        Treatments = self.ds.Matching_Treatment_id()
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are you sure!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_clicked = msg.exec()
        if button_clicked == QMessageBox.Yes:
            if Treatment_id not in Treatments:
                self.error()
            else:
                self.ds.Delete_Treatment(id = self.ui.Remove_Treatment_Id.text())
                self.succesful_popup()
        elif button_clicked == QMessageBox.No:
            QMessageBox.close
        else:
            QMessageBox.close

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
            name += (f"{i[0]}, Id: {i[1]} \n")
        self.ui.List_Of_Patients_Label.setText(f"""
List Of Patients:
{name}                      
""")

    def error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Operation Failed")
        msg.setText("    That Id Does Not Exsist!        ")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec()

    def ADD_Error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Operation Failed")
        msg.setText("    That Id Already Exsists!        ")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec()

    def SearchPatients(self):
        patient_id = self.ui.Patient_Id_Search_Patient.text()
        patients = self.ds.Matching_Patient_id()
        if patient_id not in patients:
            self.error()
        else:
            Patient_Info = self.ds.select_matching_user(self.ui.Patient_Id_Search_Patient.text())
            info = ""
            for i in Patient_Info:
                info += """
Patient Id: {}
Patient Name: {} {}
Patient Height: {}
Patient Weight: {}
Patient Address: {}
Num of Treatments Taken: {}
    """.format(i[0], i[4], i[5], i[1], i[2], i[3], i[6])
            self.ui.Search_Patient_Label.setText(f"""                         
Patient Info:                                                                          
{info}                          
""")
        

    def succesful_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Opersation Completed!")
        msg.setText("Done!")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec()

    def add_treatment(self):
        Treatment_id = self.ui.Add_Treatment_Id.text()
        Treatments = self.ds.Matching_Treatment_id()
        if Treatment_id not in Treatments:
            self.ds.Add_Treatment(
            id = self.ui.Add_Treatment_Id.text(),
            Cost = self.ui.Add_Treatment_Cost.text(),
            Description = self.ui.Add_Treatment_Desc.text(),
            TreatmentName = self.ui.Add_Treatment_Name.text()
            )
            self.ui.Add_Treatment_Id.clear()
            self.ui.Add_Treatment_Cost.clear()
            self.ui.Add_Treatment_Desc.clear()
            self.ui.Add_Treatment_Name.clear()
            self.succesful_popup()
        else:
            self.ADD_Error()

    def add_patient(self):
        patient_id = self.ui.Add_Patient_Id.text()
        patients = self.ds.Matching_Patient_id()        
        if patient_id not in patients:
            self.ds.Add_Patient(

            id = self.ui.Add_Patient_Id.text(), 
            FirstName = self.ui.Add_Patient__FirstName.text(), 
            LastName = self.ui.Add_Patient_LastName.text(), 
            Height = self.ui.Add_Patient_Height.text(), 
            Weight = self.ui.Add_Patient_Weight.text(), 
            Address = self.ui.Add_Patient_Address.text(), 
            Amountoftreatmentstaken = self.ui.Add_Num_Of_treat.text()
            )
            self.ui.Add_Patient_Id.clear()
            self.ui.Add_Patient__FirstName.clear()
            self.ui.Add_Patient_LastName.clear()
            self.ui.Add_Patient_Height.clear()
            self.ui.Add_Patient_Weight.clear()
            self.ui.Add_Patient_Address.clear()
            self.ui.Add_Num_Of_treat.clear()
            self.succesful_popup()
        else:
            self.ADD_Error()

    def add_appointment(self):
        appointment_id = self.ui.Add_Appointment_Id.text()
        appointments = self.ds.Matching_Appointment_Id()
        if appointment_id not in appointments:
            self.ds.Add_Appointment(
            id = self.ui.Add_Appointment_Id.text(),
            Date = self.ui.Add_Appointment_Date.text(),
            Result = self.ui.Add_Appointment_Result.text(),
            PatientId = self.ui.Add_Appointment_Patient_Id.text(),
            RoomId = self.ui.Add_Room_Id.text(),
            Paid = self.ui.Add_Appointment_Paid.text()
            )
            self.ui.Add_Appointment_Paid.clear()
            self.ui.Add_Appointment_Patient_Id.clear()
            self.ui.Add_Appointment_Id.clear()
            self.ui.Add_Appointment_Date.clear()
            self.ui.Add_Appointment_Result.clear()
            self.ui.Add_Room_Id.clear()
            self.succesful_popup()
        else:
            self.ADD_Error()



    def delete_patient(self):
        patient_id = self.ui.Patient_Id_Remove_Patient.text()
        patients = self.ds.Matching_Patient_id()
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are you sure!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_clicked = msg.exec()
        if button_clicked == QMessageBox.Yes:
            if patient_id not in patients:
                self.error()
            else:
                self.ds.Delete_Patient(id = self.ui.Patient_Id_Remove_Patient.text())
                self.succesful_popup()
        elif button_clicked == QMessageBox.No:
            QMessageBox.close
        else:
            QMessageBox.close


    
    def SearchAppointments(self):
        if self.ui.Search_By_Id_Radio.isChecked():
            Date = 0
            RoomId = 0
            PatientId = 0
            id = self.ui.Search_Appointment_Id.text()
            SelectedValue = 1
            self.ds.SearchAppointment(id, SelectedValue, RoomId, PatientId, Date)
            appointment_info = self.ds.SearchAppointment(id, SelectedValue, RoomId, PatientId, Date)
            info = ""
            for i in appointment_info:
                info += ("""
Id: {}
Date: {}
Result: {}
Patient Id: {}
Room Id: {}
Paid: {}
""").format(i[0], i[1], i[2], i[3], i[4], i[5])
            self.ui.Search_Appointment_Label.setText(f"""
Appointment:
{info}                                                         
""")
        elif self.ui.Search_By_Paid_Id_Radio.isChecked():
            Date = 0
            RoomId = 0
            id = 0
            PatientId = 0
            SelectedValue = 2
            self.ds.SearchAppointment(id, SelectedValue, RoomId, PatientId, Date)
            appointment_info = self.ds.SearchAppointment(id, SelectedValue, RoomId, PatientId, Date)
            info = ""
            for i in appointment_info:
                info += ("""
Id: {}
Date: {}
Result: {}
Patient Id: {}
Room Id: {}
Paid: {}                                         
""").format(i[0], i[1], i[2], i[3], i[4], i[5])
            self.ui.Search_Appointment_Label.setText(f"""
Appointments:
{info}                                             
""")
        elif self.ui.Search_By_Room_Id_Radio.isChecked():
            Date= 0
            RoomId = self.ui.Search_Room_Id.text()
            PatientId = 0
            id = 0
            SelectedValue = 3
            self.ds.SearchAppointment(id, SelectedValue, RoomId, PatientId, Date)
            appointment_info = self.ds.SearchAppointment(id, SelectedValue, RoomId, PatientId, Date)
            info = ""
            for i in appointment_info:
                info += ("""
Id: {}
Date: {}
Result: {}
Patient Id: {}
Room Id: {}
Paid: {}                                         
""").format(i[0], i[1], i[2], i[3], i[4], i[5])
            self.ui.Search_Appointment_Label.setText(f"""
Appointment/s:
{info}                                             
""")
        elif self.ui.Search_By_Paitnet_Id_Radio.isChecked():
            Date = 0
            RoomId = 0
            id = 0
            SelectedValue = 4
            PatientId = self.ui.Search_Appointment_Patient_Id.text()
            self.ds.SearchAppointment(id, SelectedValue, RoomId, PatientId, Date)
            appointment_info = self.ds.SearchAppointment(id, SelectedValue, RoomId, PatientId, Date)
            info = ""
            for i in appointment_info:
                info += ("""
Id: {}
Date: {}
Result: {}
Patient Id: {}
Room Id: {}
Paid: {}                                         
""").format(i[0], i[1], i[2], i[3], i[4], i[5])
            self.ui.Search_Appointment_Label.setText(f"""
Appointment/s:
{info}                                             
""")
        elif self.ui.Search_By_Date_Radio.isChecked():
            Date = self.ui.Search_Appointment_Date.text()
            RoomId = 0
            id = 0
            SelectedValue = 5
            PatientId = self.ui.Search_Appointment_Patient_Id.text()
            self.ds.SearchAppointment(id, SelectedValue, RoomId, PatientId, Date)
            appointment_info = self.ds.SearchAppointment(id, SelectedValue, RoomId, PatientId, Date)
            info = ""
            for i in appointment_info:
                info += ("""
Id: {}
Date: {}
Result: {}
Patient Id: {}
Room Id: {}
Paid: {}                                         
""").format(i[0], i[1], i[2], i[3], i[4], i[5])
            self.ui.Search_Appointment_Label.setText(f"""
Appointment/s:
{info}                                             
""")

    def Update_Treatment(self):
        Treatment_id = self.ui.Update_Patient_Id.text()
        Treatments = self.ds.Matching_Treatment_id()
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are you sure!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_clicked = msg.exec()
        if button_clicked == QMessageBox.Yes:
            if Treatment_id not in Treatments:
                self.error()
            else:
                if self.ui.Update_Treatment_Cost_Radio.isChecked():
                    id = self.ui.Update_Treatment_Id.text()
                    UpdatedValue = self.ui.Update_Treatment_Cost.text()
                    UpdatedSelection = 1
                    self.ds.update_treatment(id, UpdatedSelection, UpdatedValue)
                    self.ui.Update_Treatment_Cost.clear()
                    self.succesful_popup()

                elif self.ui.Update_Treatment_Desc_Radio.isChecked():
                    id = self.ui.Update_Treatment_Id.text()
                    UpdatedValue = self.ui.Update_Treatment_Desc.text()
                    UpdatedSelection = 2
                    self.ds.update_treatment(id, UpdatedSelection, UpdatedValue)
                    self.ui.Update_Treatment_Desc.clear()
                    self.succesful_popup()

                elif self.ui.Update_Treatment_Name_Radio.isChecked():
                    id = self.ui.Update_Treatment_Id.text()
                    UpdatedValue = self.ui.Update_Treatment_Name.text()
                    UpdatedSelection = 3
                    self.ds.update_treatment(id, UpdatedSelection, UpdatedValue)
                    self.ui.Update_Treatment_Name.clear()
                    self.succesful_popup()

        elif button_clicked == QMessageBox.No:
            QMessageBox.close
        else:
            QMessageBox.close


    def Update_Patient(self):
        patient_id = self.ui.Update_Patient_Id.text()
        patients = self.ds.Matching_Patient_id()
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are you sure!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_clicked = msg.exec()
        if button_clicked == QMessageBox.Yes:
            if patient_id not in patients:
                self.error()
            else:
                if self.ui.Patient_Update_Name_Radio.isChecked():
                    id = self.ui.Update_Patient_Id.text()
                    UpdatedValue = self.ui.Update_Patient_FirstName.text()
                    UpdatedSelection = 1
                    self.ds.update_patient(id, UpdatedSelection, UpdatedValue)
                    self.ui.Update_Patient_FirstName.clear()
                    self.succesful_popup()


                elif self.ui.Patient_Update_LastName_Radio.isChecked():
                    id = self.ui.Update_Patient_Id.text()
                    UpdatedValue = self.ui.Update_Patient_LastName.text()
                    UpdatedSelection = 2
                    self.ds.update_patient(id, UpdatedSelection, UpdatedValue)
                    self.ui.Update_Patient_LastName.clear()
                    self.succesful_popup()

                elif self.ui.Patient_Update_Address_Radio.isChecked():
                    id = self.ui.Update_Patient_Id.text()
                    UpdatedValue = self.ui.Update_Patient_Address.text()
                    UpdatedSelection = 3
                    self.ds.update_patient(id, UpdatedSelection, UpdatedValue)
                    self.ui.Update_Patient_Address.clear()
                    self.succesful_popup()


                elif self.ui.Patient_Update_Height_Radio.isChecked():
                    id = self.ui.Update_Patient_Id.text()
                    UpdatedValue = self.ui.Update_Patient_Height.text()
                    UpdatedSelection = 4
                    self.ds.update_patient(id, UpdatedSelection, UpdatedValue)
                    self.ui.Update_Patient_Height.clear()
                    self.succesful_popup()


                elif self.ui.Patient_Update_Weight_Radio.isChecked():
                    id = self.ui.Update_Patient_Id.text()
                    UpdatedValue = self.ui.Update_Patient_Weight.text()
                    UpdatedSelection = 5
                    self.ds.update_patient(id, UpdatedSelection, UpdatedValue)
                    self.ui.Update_Patient_Weight.clear()
                    self.succesful_popup()


                elif self.ui.Patient_Update_Treatments_Radio.isChecked():
                    id = self.ui.Update_Patient_Id.text()
                    UpdatedValue = self.ui.Update_Num_Of_Treatments.text()
                    UpdatedSelection = 6
                    self.ds.update_patient(id, UpdatedSelection, UpdatedValue)
                    self.ui.Update_Num_Of_Treatments.clear()
                    self.succesful_popup()
        elif button_clicked == QMessageBox.No:
            QMessageBox.close
        else:
            QMessageBox.close



