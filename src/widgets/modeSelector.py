from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QStackedWidget, QFrame, QHBoxLayout, QRadioButton, QButtonGroup
from PySide6.QtGui import Qt, QIcon, QFont
from PySide6.QtCore import QSize, Signal

class modeSelector(QWidget):

    mode_changed = Signal(int)

    def __init__(self):
        super().__init__()

       
        self.setup_widgets()
        self.setup_layout()
        self.setup_connections()


        self.modeIndex = None
                                
        
    def setup_widgets(self):
        self.label = QLabel("Game Mode :") 
        self.label.setFont(QFont("Arial", 17)) 

        self.button_group = QButtonGroup()
        self.exact_button = QRadioButton("Exact Count")
        self.range_button = QRadioButton("Range")   

        self.button_group.addButton(self.exact_button, 0)
        self.button_group.addButton(self.range_button, 1)



        self.exact_button.setFont(QFont("Arial", 17))
        self.range_button.setFont(QFont("Arial", 17))

    def setup_layout(self):
        layout = QHBoxLayout()
 
        layout.addWidget(self.label, 3)
        
        layout.addWidget(self.exact_button, 4)
        layout.addWidget(self.range_button, 4)
       
    


        self.setLayout(layout)

    def setup_connections(self):
        self.button_group.buttonClicked.connect(self.on_button_pressed)
        

    def on_button_pressed(self):
        self.mode_changed.emit(self.button_group.checkedId())

    def update_mode(self, modeId):
        self.modeIndex = 0
        self.button_group.button(modeId).setChecked(True)
        

