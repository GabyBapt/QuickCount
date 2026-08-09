from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QStackedWidget
from PySide6.QtGui import Qt, QIcon, QFont
from PySide6.QtCore import Signal
from widgets.countdown import Countdown
from widgets.game import Game
from config.settings import TrainingSettings

class TrainingPageGame(QWidget):

    hide_navbar_signal = Signal(bool)

    def __init__(self):

        super().__init__()
        self.stack = QStackedWidget()
        self.countdown = Countdown()
        self.settings = TrainingSettings()
        self.game = Game(self.settings)

        self.stack.addWidget(self.countdown)
        self.stack.addWidget(self.game)

        self.stack.setCurrentWidget(self.countdown)

        
        
        self.setup_layout()
        self.setup_connections()
        


    def setup_layout(self):

        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)


    def setup_connections(self):
        self.countdown.start_game.connect(self.start_game)

        
    def pre_game(self):
        self.hide_navbar_signal.emit(True)
        self.gather_settings()
        self.countdown.start_countdown()
        
    


    def gather_settings(self):
        self.settings = self



    def start_game(self):
        self.stack.setCurrentWidget(self.game)
        self.game.game_controller.round_loop()