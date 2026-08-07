from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QStackedWidget, QFrame, QHBoxLayout, QSpinBox, QStyleFactory, QDoubleSpinBox
from PySide6.QtGui import Qt, QIcon, QFont
from PySide6.QtCore import QSize, Signal, QTimer
from superqt import QLabeledDoubleSlider

class Countdown(QWidget):

    start_game = Signal()


    def __init__(self):
        
        super().__init__()
        self.setup_widgets()
        self.setup_layout()
        self.setHidden(True)
        
        
        


        
    def setup_widgets(self):

        self.remaining_time = 5
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.countdown_update)

        self.label = QLabel("5")
        
        self.label.setFont(QFont("Arial Black", 200))
        self.label.setStyleSheet("color: #151515")
         
    def setup_layout(self):
        
        countdown_layout = QVBoxLayout()
        countdown_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        countdown_layout.addStretch(3)
        countdown_layout.addWidget(self.label, 3)
        countdown_layout.addStretch(3)

        self.setLayout(countdown_layout)

    def start_countdown(self):
        
        self.setHidden(False)
        self.timer.start()
        
    def countdown_update(self):
        if self.remaining_time>0:
            self.remaining_time -= 1
            self.label.setText(str(self.remaining_time)) 
            if self.remaining_time == 0:
                self.start_game.emit()
                self.timer.stop()
                self.setHidden(True)
            

    