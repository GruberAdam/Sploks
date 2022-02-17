from PyQt5 import QtWidgets, QtGui, uic

class CustomersWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        print("in")
        customersView = uic.loadUi("view/customersView.ui", self)
        customersView.show()
