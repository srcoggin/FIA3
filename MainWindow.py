from PyQt5.QtWidgets import QMainWindow
from UserInterface import Ui_MainWindow
from datastore import DataStore
from PyQt5.QtWidgets import QMessageBox

ds = DataStore()

class MainWindow():
    def __init__(self):
        msg = QMessageBox()
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        