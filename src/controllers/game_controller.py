from random import randrange
from PySide6.QtCore import Signal, QObject, QTimer
from controllers.score_controller import ScoreController

class GameController(QObject):

    draw_signal = Signal(int) #nb item
    hide_signal = Signal()

    def __init__(self, Settings):
        super().__init__()
        self.settings = Settings
        self.draw_time = int(self.settings.value("time", type=float)*1000)
        self.score_controller = ScoreController()
        
        self.draw_timer = QTimer()
        self.draw_timer.setSingleShot(True)
        self.draw_timer.stop()
        self.draw_timer.setInterval(self.draw_time)
        self.draw_timer.timeout.connect(self.hide_items)


    def round_loop(self):
        self.item_count = randrange(self.settings.range[0], self.settings.range[1])
        print("show")

        self.draw_signal.emit(self.item_count)
        self.draw_timer.start()
        

    def hide_items(self):
        self.hide_signal.emit()
        print("hidee")


    def submit_result(self, result):
        self.score_controller.calculate_points()

        


    




        