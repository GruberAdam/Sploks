from PyQt5 import QtWidgets, QtGui, uic
from model.customersModel import *
class CustomersUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.customersWindow = uic.loadUi("view/customersView.ui", self)

        self.customers = getCustomers(self)
        for customer in self.customers:
            print(customer[0])
            #self.customersWindow.tableCustomers.setItem(customer[0] - 1, customer[0], QtWidgets.QTableWidgetItem(customer[0]))
            
            print("worked")
        print(self.customersWindow.tableCustomers.showMaximized)
        self.customersWindow.show()