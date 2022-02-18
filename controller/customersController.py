from PyQt5 import QtWidgets, QtGui, uic

class CustomersUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        print("In clients")
        self.customersWindow = uic.loadUi("view/customersView.ui", self)
        self.customersWindow.show()
