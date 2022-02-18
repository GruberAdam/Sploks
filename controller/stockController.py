from PyQt5 import QtWidgets, QtGui, uic

class StockUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        print("In stock")
        self.StockWindow = uic.loadUi("view/stockView.ui", self)
        self.StockWindow.show()
