# Author : Adam Gruber
# Date : 17.02.2022
# Version : 1.0

from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtCore import Qt

from controller import customersController, stockController, staffController, contractsController

def displayMainMenu(self):
    mainMenuWindow = uic.loadUi("view/menuView.ui", self)

    # Click event listener 
    mainMenuWindow.btnClients.clicked.connect(displayClients)
    mainMenuWindow.btnStock.clicked.connect(displayStock)
    mainMenuWindow.btnStaff.clicked.connect(displayStaff)
    mainMenuWindow.btnContracts.clicked.connect(displayContracts)

    mainMenuWindow.show()

# Redirects to the right function based on the key pressed
def keyPressEvent(self, e):
    print(e.key())

    if e.key() == Qt.Key.Key_A: # When user presses the "a" key
        displayClients(self)
    if e.key() == Qt.Key.Key_S: # When user presses the "s" key
        displayStock(self)
    if e.key() == Qt.Key.Key_D: # When user presses the "d" key
        displayStaff(self)
    if e.key() == Qt.Key.Key_F: # When user presses the "f" key
        displayContracts(self)

# Redirects in the customers controller
def displayClients(self):
    customersController.CustomersUi()

# Redirects in the stock controller
def displayStock(self):
    stockController.StockUi() 

# Redirects in the staff controller
def displayStaff(self):
    staffController.StaffUi()

# Redirects in the contracts controller
def displayContracts(self):
    contractsController.ContractsUi()



