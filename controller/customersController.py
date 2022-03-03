from PyQt5 import QtWidgets, QtGui, uic
from controller import keyPressController
from model.customersModel import *
class CustomersUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.customers = getCustomers(self)
        self.customersWindow = uic.loadUi("view/customersView.ui", self)
        self.customersWindow.show()