from random import randrange
from PySide6.QtCore import Signal, QObject

class ScoreController(QObject):


    score_update = Signal(int) 


    def __init__(self):
        self.score = 0



    def addScore(self, points):
        self.score += points

    def resetScore(self):
        self.score = 0

    
        