from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QStackedWidget, QFrame
from PySide6.QtGui import Qt, QIcon, QFont
from PySide6.QtCore import QTimer
from widgets.answerBox import AnswerBox
from controllers.game_controller import GameController
from widgets.gameGrid import GameGrid
from config.settings import settings


class Game(QWidget):
    def __init__(self):
        super().__init__()

        self.settings = settings

        self.setup_widgets()
        self.setup_layout()
       
        self.game_controller = GameController(self.settings)

        self.setup_connections()


    def setup_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        layout.addWidget(self.title_widget, 1)
        layout.addWidget(self.game_frame, 10)
        layout.addWidget(self.answer_box, 3)
        

        self.setLayout(layout)


    def setup_widgets(self):

        self.title_widget = QLabel("Count the number of item on screen", alignment=Qt.AlignmentFlag.AlignHCenter)
        self.title_widget.setFont(QFont("Arial", 30))
        self.title_widget.setStyleSheet("")


        self.game_frame = QFrame()
        self.game_frame.setStyleSheet("""
                   QFrame {
                       background-color: #252525;
                       border: 1px solid #404040;
                       border-radius: 8px;
                   }
                   """)
        self.game_grid = GameGrid()

        self.game_frame.setLayout(QVBoxLayout())
        self.game_frame.layout().addWidget(self.game_grid, 1)

        self.answer_box = AnswerBox(self.settings.value("mode", type=int))


    def setup_connections(self):
        self.game_controller.draw_signal.connect(self.draw_items)
        
        
    def draw_items(self, item_count):

        self.game_grid.draw_items(item_count)
        
