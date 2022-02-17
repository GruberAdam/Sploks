# Author : Adam Gruber
# Date : 17.02.2022
# Version : 1.0

import sys
import os
sys.path.append(os.getcwd() + "\\packages") # Importing packages file
from PyQt5 import QtWidgets

from controller import menuController

class Sploks(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        menuController.displayMainMenu(self) # Calls function in controller


app = QtWidgets.QApplication(sys.argv)
window = Sploks()
app.exec_()