from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QStackedWidget, QFrame
from PySide6.QtGui import Qt, QIcon, QFont
from widgets.answerBox import AnswerBox
from controllers.game_controller import GameController

class Game(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_widgets()
        self.setup_layout()
        self.game_controller = GameController()


    def setup_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        layout.addWidget(self.title_widget, 1)
        layout.addWidget(self.game_canva, 10)
        layout.addWidget(self.answer_box, 3)

        self.setLayout(layout)


    def setup_widgets(self):

        self.title_widget = QLabel("Count the number of item on screen", alignment=Qt.AlignmentFlag.AlignHCenter)
        self.title_widget.setFont(QFont("Arial", 30))
        self.title_widget.setStyleSheet("")


        self.game_canva = QFrame()
        self.game_canva.setStyleSheet("""
                   QFrame {
                       background-color: #252525;
                       border: 1px solid #404040;
                       border-radius: 8px;
                   }
                   """)


        self.answer_box = AnswerBox()
        
        
    def draw_items(self):
        return
