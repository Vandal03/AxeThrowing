import sys
import os
import csv
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from View.addPlayer import addPlayerView


class mainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Set Window Details
        self.setWindowTitle("Abe's Axes")
       
        self.setContentsMargins(0,0,0,0)
        #mainMenuGrid = QGridLayout()
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(1,1,1,0)
        


        playerLabel = QLabel("Player Name:")
        playerText = QLineEdit()
        addPlayerForm = QHBoxLayout()
        addPlayerForm.addWidget(playerLabel)
        addPlayerForm.addWidget(playerText)
        addPlayerForm.setContentsMargins(0,0,0,0)
        mainLayout.addLayout(addPlayerForm)

        player1label = QLabel("Players:")
        mainLayout.addWidget(player1label)
        #Add Player
        addPlayerBtn = QPushButton("Add Player")
        addPlayerBtn.clicked.connect(self.addPlayerBtnClick)
        mainLayout.addWidget(addPlayerBtn)
        #mainMenuGrid.addWidget(addPlayerBtn, 0, 0)


        #Set Window Layout########
        testWidget = QWidget()
        testWidget.setLayout(mainLayout)
        
        
        #testWidget.setLayout(mainMenuGrid)
        mainMenu.setCentralWidget(self, testWidget)
        mainLayout.setSpacing(0)
        

#Button Events
    def addPlayerBtnClick(self):
        print("Add Player")
        self.window = addPlayerView()
        self.window.show()
    

