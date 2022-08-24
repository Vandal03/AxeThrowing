import csv
import os


class player():
    def __init__(self):
        self.gamesWon = 0
        self.gamesPlayed = 0


class customPlayer(player):
    def __init__(self, playerName):
        super().__init__()
        self.name = playerName


class randomPlayer(player):
    def __init__(self):
        super().__init__()

        