import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from View import mainMenu, addPlayer
from Tests import modelTests as t

app = QApplication(sys.argv)
window = mainMenu.mainMenu()
window.show()
app.exec()







