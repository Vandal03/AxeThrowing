import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class addPlayerView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Add Player')
        
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel("Player Name:")
        layout.addWidget(label, 0, 0, 1, 1)
        nameInput = QLineEdit()
        layout.addWidget(nameInput, 1, 0, 1, 2)
        addPlayerBtn = QPushButton("Add")
        layout.addWidget(addPlayerBtn, 2, 0, 1, 1)
        cancelBtn = QPushButton("Cancel")
        cancelBtn.clicked.connect(self.cancelBtn)
        layout.addWidget(cancelBtn, 2, 1, 1, 1)


    def cancelBtn(self):
        self.close()