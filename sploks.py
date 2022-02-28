# Author : Adam Gruber
# Date : 17.02.2022
# Version : 1.0

import sys
import os
sys.path.append(os.getcwd() + "\\packages") # Importing packages file
from PyQt5 import QtWidgets

from controller import mainMenuController

class Sploks(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        mainMenuController.displayMainMenu(self) # Calls function in controller

    # Event listener when a key is pressed
    def keyPressEvent(self, e):
        mainMenuController.keyPressEvent(self, e)

app = QtWidgets.QApplication(sys.argv)
window = Sploks()
app.exec_()