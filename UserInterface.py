# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\FIA3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(820, 620)
        Form.setMaximumSize(QtCore.QSize(820, 620))
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(219, 19, 591, 581))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.widget = QtWidgets.QWidget(self.Home)
        self.widget.setGeometry(QtCore.QRect(10, 10, 562, 511))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(120, 50))
        self.label_2.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.MorningEvening_Label = QtWidgets.QLabel(self.widget)
        self.MorningEvening_Label.setMinimumSize(QtCore.QSize(100, 40))
        self.MorningEvening_Label.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MorningEvening_Label.setFont(font)
        self.MorningEvening_Label.setObjectName("MorningEvening_Label")
        self.horizontalLayout_7.addWidget(self.MorningEvening_Label)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(560, 0))
        self.label_4.setMaximumSize(QtCore.QSize(560, 440))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.stackedWidget.addWidget(self.Home)
        self.Patients = QtWidgets.QWidget()
        self.Patients.setObjectName("Patients")
        self.label_5 = QtWidgets.QLabel(self.Patients)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 160, 50))
        self.label_5.setMinimumSize(QtCore.QSize(160, 50))
        self.label_5.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.widget1 = QtWidgets.QWidget(self.Patients)
        self.widget1.setGeometry(QtCore.QRect(10, 60, 310, 110))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setMinimumSize(QtCore.QSize(170, 30))
        self.label_6.setMaximumSize(QtCore.QSize(170, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_12.addWidget(self.label_6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setMinimumSize(QtCore.QSize(100, 30))
        self.label_7.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.Patient_Id_Remove_Patient = QtWidgets.QLineEdit(self.widget1)
        self.Patient_Id_Remove_Patient.setObjectName("Patient_Id_Remove_Patient")
        self.horizontalLayout_11.addWidget(self.Patient_Id_Remove_Patient)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.Remove_Patient_Button = QtWidgets.QPushButton(self.widget1)
        self.Remove_Patient_Button.setMinimumSize(QtCore.QSize(120, 30))
        self.Remove_Patient_Button.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Remove_Patient_Button.setFont(font)
        self.Remove_Patient_Button.setObjectName("Remove_Patient_Button")
        self.horizontalLayout_10.addWidget(self.Remove_Patient_Button)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.stackedWidget.addWidget(self.Patients)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(0, 0, 202, 581))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget2)
        self.label.setMinimumSize(QtCore.QSize(200, 90))
        self.label.setMaximumSize(QtCore.QSize(200, 90))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.LogoButton = QtWidgets.QPushButton(self.widget2)
        self.LogoButton.setMinimumSize(QtCore.QSize(140, 70))
        self.LogoButton.setMaximumSize(QtCore.QSize(140, 70))
        self.LogoButton.setObjectName("LogoButton")
        self.horizontalLayout_3.addWidget(self.LogoButton)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.Home_Banner_Button = QtWidgets.QPushButton(self.widget2)
        self.Home_Banner_Button.setMinimumSize(QtCore.QSize(180, 50))
        self.Home_Banner_Button.setMaximumSize(QtCore.QSize(180, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Home_Banner_Button.setFont(font)
        self.Home_Banner_Button.setObjectName("Home_Banner_Button")
        self.horizontalLayout_2.addWidget(self.Home_Banner_Button)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem14)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.Patients_Banner_Button = QtWidgets.QPushButton(self.widget2)
        self.Patients_Banner_Button.setMinimumSize(QtCore.QSize(180, 50))
        self.Patients_Banner_Button.setMaximumSize(QtCore.QSize(180, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Patients_Banner_Button.setFont(font)
        self.Patients_Banner_Button.setObjectName("Patients_Banner_Button")
        self.horizontalLayout_4.addWidget(self.Patients_Banner_Button)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem16)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem17)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem18)
        self.Treatments_Banner_Buttons = QtWidgets.QPushButton(self.widget2)
        self.Treatments_Banner_Buttons.setMinimumSize(QtCore.QSize(180, 50))
        self.Treatments_Banner_Buttons.setMaximumSize(QtCore.QSize(180, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Treatments_Banner_Buttons.setFont(font)
        self.Treatments_Banner_Buttons.setObjectName("Treatments_Banner_Buttons")
        self.horizontalLayout_5.addWidget(self.Treatments_Banner_Buttons)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem19)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem20)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem21)
        self.Appointment_Banner_Buttons = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(180)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.Appointment_Banner_Buttons.sizePolicy().hasHeightForWidth())
        self.Appointment_Banner_Buttons.setSizePolicy(sizePolicy)
        self.Appointment_Banner_Buttons.setMinimumSize(QtCore.QSize(180, 50))
        self.Appointment_Banner_Buttons.setMaximumSize(QtCore.QSize(180, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Appointment_Banner_Buttons.setFont(font)
        self.Appointment_Banner_Buttons.setObjectName("Appointment_Banner_Buttons")
        self.horizontalLayout_6.addWidget(self.Appointment_Banner_Buttons)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem22)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem23)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem24)
        self.Exit_Banner_Button = QtWidgets.QPushButton(self.widget2)
        self.Exit_Banner_Button.setMinimumSize(QtCore.QSize(80, 50))
        self.Exit_Banner_Button.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Exit_Banner_Button.setFont(font)
        self.Exit_Banner_Button.setObjectName("Exit_Banner_Button")
        self.horizontalLayout.addWidget(self.Exit_Banner_Button)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem25)
        self.About_Banner_Button = QtWidgets.QPushButton(self.widget2)
        self.About_Banner_Button.setMinimumSize(QtCore.QSize(80, 50))
        self.About_Banner_Button.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.About_Banner_Button.setFont(font)
        self.About_Banner_Button.setObjectName("About_Banner_Button")
        self.horizontalLayout.addWidget(self.About_Banner_Button)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem26)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem27)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Home:"))
        self.label_3.setText(_translate("Form", "Good,"))
        self.MorningEvening_Label.setText(_translate("Form", "blub"))
        self.label_4.setText(_translate("Form", "\n"
"Introducing Fighting Fit Physio, your trusted provider of exceptional physiotherapy services in the beautiful Bundaberg region. At Fighting Fit Physio, we are dedicated to helping our patients regain their strength, mobility, and overall well-being.\n"
"At Fighting Fit Physio, we understand that every individual is different, and we take the time to listen to your specific goals and concerns. Our friendly team fosters a supportive environment where you can feel comfortable and confident throughout your treatment process.\n"
"Conveniently located in the heart of the Bundaberg region, our modern clinic provides a warm and inviting space for your physiotherapy sessions. We also offer telehealth services, allowing you to receive expert guidance and support from the comfort of your own home."))
        self.label_5.setText(_translate("Form", "Patients:"))
        self.label_6.setText(_translate("Form", "Remove Patients:"))
        self.label_7.setText(_translate("Form", "Patient Id:"))
        self.Remove_Patient_Button.setText(_translate("Form", "Remove Paitent"))
        self.label.setText(_translate("Form", "Fighting Fit Physio"))
        self.LogoButton.setText(_translate("Form", "LOGO"))
        self.Home_Banner_Button.setText(_translate("Form", "Home"))
        self.Patients_Banner_Button.setText(_translate("Form", "Patients"))
        self.Treatments_Banner_Buttons.setText(_translate("Form", "Treatments"))
        self.Appointment_Banner_Buttons.setText(_translate("Form", "Appointments"))
        self.Exit_Banner_Button.setText(_translate("Form", "Exit"))
        self.About_Banner_Button.setText(_translate("Form", "About"))
