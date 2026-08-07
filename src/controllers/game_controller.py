from random import randrange
from PySide6.QtCore import Signal, QObject
from controllers.score_controller import ScoreController

class GameController(QObject):

    draw_signal = Signal(int, int) #nb item, time

    def __init__(self):
        self.settings = 0
        self.score_controller = ScoreController()


    def round_loop(self):
        self.item_count = randrange(self.settings.range)
        draw_time = self.settings.time

        self.draw_signal.emit(self.item_count, draw_time)

    def submit_result(self, result):
        self.score_controller.calculate_points()

        


    




        