from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QStackedWidget, QFrame
from PySide6.QtGui import Qt, QIcon, QFont
from PySide6.QtCore import QSize
from pages.training_pages.training_page_settings import TrainingPageSettings




class TrainingPageHome(QWidget):
    def __init__(self):
        
        super().__init__()

        
        
        
        
        layout = QVBoxLayout()
    
        
        label = QLabel("Training")

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        


        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label.setFont(QFont("Arial", 30))
        
       
        
        self.button = QPushButton("New Training")
        self.button.setIcon(QIcon("./QuickCount/src/icons/plusIcon.svg"))
        self.button.setFont(QFont("Arial", 30))
        self.button.setIconSize(QSize(40, 40))
        

        self.button.setMinimumSize(100, 50)
        self.button.setMaximumSize(500, 70)
       
        
        
        

        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignHCenter, stretch=1)
        layout.addWidget(separator)
        layout.addStretch(5)
        layout.addWidget(self.button, stretch=4, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addStretch(4)

        self.setLayout(layout)

        
    

    