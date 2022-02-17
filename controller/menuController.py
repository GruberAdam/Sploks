# Author : Adam Gruber
# Date : 17.02.2022
# Version : 1.0


from PyQt5 import QtWidgets, QtGui, uic

def displayMainMenu(self):
    mainMenuWindow = uic.loadUi("view/menuView.ui", self)

    # Click event listener 
    mainMenuWindow.btnClients.clicked.connect(displayClients)
    mainMenuWindow.btnStock.clicked.connect(displayStock)
    mainMenuWindow.btnStaff.clicked.connect(displayStaff)
    mainMenuWindow.btnContracts.clicked.connect(displayContracts)

    mainMenuWindow.show()


def displayClients(self):
    print("in Clients")

def displayStock(self):
    print("in Stock")

def displayStaff(self):
    print("in Staff")

def displayContracts(self):
    print("in Contracts")



