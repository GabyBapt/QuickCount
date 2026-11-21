from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout
from PySide6.QtGui import QFont, Qt

class GameGrid(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_widgets()
        self.setup_layout()

    def setup_widgets(self):
        return

    def setup_layout(self):
        layout = QGridLayout()
        
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)

    def draw_items(self, item_count):
        return
