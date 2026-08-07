from PySide6.QtWidgets import QPushButton, QWidget, QLabel, QVBoxLayout

class StatPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Hello")
        start_button = QPushButton("Start Stats")

        start_button.show()

        layout.addWidget(label)
        layout.addWidget(start_button)

        self.setLayout(layout)
        start_button.clicked.connect(self.stat_start)
        
    def stat_start(self):
        print("statatsss")
