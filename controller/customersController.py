from PyQt5 import QtWidgets, QtGui, uic, QtCore
from model.customersModel import *
class CustomersUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.customersWindow = uic.loadUi("view/customersView.ui", self) 

        self.customers = getCustomers(self)

        self.customersWindow.tableCustomers.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        for index, customer in enumerate(self.customers):
            self.customersWindow.tableCustomers.verticalHeader().setVisible(False) # Hides the row number
            self.customersWindow.tableCustomers.insertRow(index) # Inserts the row

            # Fills the table
            self.customersWindow.tableCustomers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(customer[0]))) # Sets the ID
            self.customersWindow.tableCustomers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(customer[1]))) # Sets the LastName
            self.customersWindow.tableCustomers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(customer[2]))) # Sets the FirstName
            self.customersWindow.tableCustomers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(customer[3]))) # Sets the Address
            self.customersWindow.tableCustomers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(customer[8]))) # Sets the NPA
            self.customersWindow.tableCustomers.setItem(index, 5, QtWidgets.QTableWidgetItem(str(customer[9]))) # Sets the Locality
            self.customersWindow.tableCustomers.setItem(index, 6, QtWidgets.QTableWidgetItem(str(customer[4]))) # Sets the Phone number
            self.customersWindow.tableCustomers.setItem(index, 7, QtWidgets.QTableWidgetItem(str(customer[5]))) # Sets the email
            self.customersWindow.tableCustomers.setItem(index, 8, QtWidgets.QTableWidgetItem(str(customer[6]))) # Sets the mobile phone

        self.customersWindow.tableCustomers.viewport().installEventFilter(self) # Event listener
        print("Customer data loaded")
        
        self.customersWindow.show()

    def eventFilter(self, source, event):
        if self.customersWindow.tableCustomers.selectedIndexes() != []: # Checks that the user clicked on a cell
            if event.type() == QtCore.QEvent.MouseButtonDblClick: # If user double clicked

                row = self.customersWindow.tableCustomers.currentRow() # gets row clicked
                id = self.customersWindow.tableCustomers.item(row, 0).text() # gets ID based on click
                

                

                
            
        return False
 