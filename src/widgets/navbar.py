from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QFont


class NavBar(QFrame):


    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("""
            QFrame {
                background-color: #252525;
                border: 1px solid #404040;
                border-radius: 8px;
            }
            """)
        self.setMinimumWidth(150)
        self.setMaximumWidth(250)
        self.navbar_layout = QVBoxLayout()
        
        
                
        self.training_page_button = QPushButton("Training")
        self.training_page_button.setFont(QFont("Arial", 17))
        self.training_page_button.setFlat(False)

        self.stats_page_button = QPushButton("Stats")
        self.stats_page_button.setFont(QFont("Sheriff", 17))

        

        self.navbar_layout.addWidget(QLabel("___"), 1)
        self.navbar_layout.addStretch(1)
        self.navbar_layout.addWidget(self.training_page_button, 5)
        self.navbar_layout.addWidget(self.stats_page_button, 5)
        self.navbar_layout.addStretch(10)
    
        self.setLayout(self.navbar_layout)

    def hide_navbar(self, hide: bool):
        self.setHidden(hide)
        print("hide")


