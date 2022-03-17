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
                print("clicked on person ID : ", id)
                self.detailledUi = CustomerDetailsUi() # Prepare the second window
                self.detailledUi.setupUi(id)
                
        return False
 
class CustomerDetailsUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.customerDetailWindow = uic.loadUi("view/customerDetailsView.ui", self)
        self.edit = False
        
    
    def setupUi(self, id):
        self.id = id

        # Button Listener
        self.customerDetailWindow.btnEditer.clicked.connect(self.editButton)
        self.customerDetailWindow.btnSupprimer.clicked.connect(self.deleteButton)
        self.customerDetailWindow.btnAnnuler.clicked.connect(self.cancelButton)
        self.customerDetailWindow.btnValider.clicked.connect(self.confirmButton)


        self.customer = getCustomerById(self, self.id) # Get the database data

        self.fillTheLabels()

        self.show()

    def fillTheLabels(self):
        # Fill the labels
        print("in")
        self.customerDetailWindow.lblPrenom.setText(str(self.customer[0][2]))
        self.customerDetailWindow.lblNom.setText(str(self.customer[0][1]))
        self.customerDetailWindow.lblAdresse.setText(str(self.customer[0][3]))
        self.customerDetailWindow.lblNPA.setText(str(self.customer[0][8])) 
        self.customerDetailWindow.lblNumero.setText(str(self.customer[0][4]))
        self.customerDetailWindow.lblTelephone.setText(str(self.customer[0][6]))
        self.customerDetailWindow.lblEmail.setText(str(self.customer[0][5]))

    def editButton(self, id):
        print(self.edit)
        if self.edit == False:
            self.edit = True
            
            # Enable text modifications
            self.customerDetailWindow.lblPrenom.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
            self.customerDetailWindow.lblNom.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)   
            self.customerDetailWindow.lblAdresse.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
            self.customerDetailWindow.lblNPA.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
            self.customerDetailWindow.lblNumero.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
            self.customerDetailWindow.lblTelephone.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
            self.customerDetailWindow.lblEmail.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)

            # Enable buttons
            self.customerDetailWindow.btnSupprimer.setEnabled(True)
            self.customerDetailWindow.btnValider.setEnabled(True)
            self.customerDetailWindow.btnAnnuler.setEnabled(True)

        elif self.edit == True:
            self.edit = False

            # Remove text modifications
            self.customerDetailWindow.lblPrenom.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.customerDetailWindow.lblNom.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.customerDetailWindow.lblAdresse.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.customerDetailWindow.lblNPA.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.customerDetailWindow.lblNumero.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.customerDetailWindow.lblTelephone.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.customerDetailWindow.lblEmail.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

            # Enable buttons
            self.customerDetailWindow.btnSupprimer.setEnabled(False)
            self.customerDetailWindow.btnValider.setEnabled(False)
            self.customerDetailWindow.btnAnnuler.setEnabled(False)

            
    def deleteButton(self):
        print("delete")
    
    def confirmButton(self):
        print(self.customerDetailWindow.lblPrenom.text())
        self.updatedCustomer = [self.customer]

    def cancelButton(self):
        self.customerDetailWindow.close()
    
    