import sys
import os
sys.path.append(os.getcwd() + "\\packages") # Importing packages file
from PyQt5 import QtWidgets, uic

from controller import *

class Sploks(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        menuController
        uic.loadUi("view/menuView.ui", self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Sploks()
app.exec_()