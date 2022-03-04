from PyQt5 import QtWidgets, QtGui, uic
from model.customersModel import *
class CustomersUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.customersWindow = uic.loadUi("view/customersView.ui", self)

        self.customers = getCustomers(self)
        
        for customer in self.customers:
            self.customersWindow.tableCustomers.insertRow(customer[0] - 1)

            self.customersWindow.tableCustomers.setItem(customer[0] - 1, 0, QtWidgets.QTableWidgetItem(str(customer[1]))) # Sets the ID
            self.customersWindow.tableCustomers.setItem(customer[0] - 1, 1, QtWidgets.QTableWidgetItem(str(customer[2]))) # Sets the LastName
            self.customersWindow.tableCustomers.setItem(customer[0] - 1, 2, QtWidgets.QTableWidgetItem(str(customer[3]))) # Sets the FirstName
            self.customersWindow.tableCustomers.setItem(customer[0] - 1, 3, QtWidgets.QTableWidgetItem(str(customer[8]))) # Sets the NPA
            self.customersWindow.tableCustomers.setItem(customer[0] - 1, 4, QtWidgets.QTableWidgetItem(str(customer[9]))) # Sets the Locality
            self.customersWindow.tableCustomers.setItem(customer[0] - 1, 5, QtWidgets.QTableWidgetItem(str(customer[4]))) # Sets the Phone number
            self.customersWindow.tableCustomers.setItem(customer[0] - 1, 6, QtWidgets.QTableWidgetItem(str(customer[5]))) # Sets the email
            self.customersWindow.tableCustomers.setItem(customer[0] - 1, 7, QtWidgets.QTableWidgetItem(str(customer[6]))) # Sets the mobile phone
        
        print("Customer data loaded")
        self.customersWindow.show()