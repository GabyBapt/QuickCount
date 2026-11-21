from PySide6.QtWidgets import QPushButton, QWidget, QSizePolicy, QVBoxLayout, QLabel, QStackedWidget, QFrame, QHBoxLayout, QSpinBox, QStyleFactory, QDoubleSpinBox
from PySide6.QtGui import Qt, QIcon, QFont
from PySide6.QtCore import QSize, Signal, QTimer
from superqt import QLabeledRangeSlider
from PySide6.QtGui import QPalette, QColor



class AnswerBox(QFrame):

    exact_answer_changed = Signal(int)
    range_answer_changed = Signal(int, int)
    

    def __init__(self, gamemode):
        
        
        super().__init__()

        self.gamemode = gamemode

        self.accent = QColor(self.palette().color(QPalette.ColorRole.Highlight).name())
        
        self.hover = self.accent.lighter(120)  
        self.pressed = self.accent.darker(120)

        self.setStyleSheet("""
            QFrame {
                background-color: #252525;
                border: 1px solid #404040;
                border-radius: 8px;
            }
            """)
        self.setMaximumHeight(100)
        
        self.setup_widgets()
        self.setup_layout()
        self.setup_connections()
        
        

        
    def setup_widgets(self):

        self.label = QLabel("Answer :")
        self.label.setFont(QFont("Arial", 30))
        self.label.setStyleSheet("""
                           QLabel {
                               border: None;
                           }
                           """)


        self.exact_spinbox = QSpinBox()
        self.range_slider = QLabeledRangeSlider(Qt.Orientation.Horizontal)


        #self.exact_spinbox.setStyle(QStyleFactory.create("windows"))
        self.exact_spinbox.lineEdit().setPlaceholderText("Enter a number ")
        self.exact_spinbox.clear()
        self.exact_spinbox.setFont(QFont("Arial Black", 10))
        self.exact_spinbox.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        self.exact_spinbox.setMaximumSize(200, 60)


        self.range_slider.setRange(0, 200)
        self.range_slider.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.range_slider.setMinimumSize(200, 80)
        self.range_slider.setEdgeLabelMode(QLabeledRangeSlider.EdgeLabelMode.NoLabel)
        self.range_slider.setBarMovesAllHandles(False)

        
        

        self.selector = QStackedWidget()
        self.selector.addWidget(self.exact_spinbox)
        self.selector.addWidget(self.range_slider)
        self.selector.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.selector.setStyleSheet("""
                                   QStackedWidget {
                                       border: None;
                                   }
                                   """)
        
        if self.gamemode == 0 :
            self.selector.setCurrentWidget(self.exact_spinbox)
        elif self.gamemode == 1 :
            self.selector.setCurrentWidget(self.range_slider)

        self.submit_button = QPushButton("Submit")
        self.submit_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.submit_button.setMinimumSize(140, 80)

        self.submit_button.setStyleSheet(   
            f""" QPushButton {{
                    background-color: {self.accent.name()};
                    color: white;
                    border-radius: 8px;
                    padding: 8px;
                }}
                QPushButton:hover {{
                    background-color: {self.hover.name()}}}
                    
                    
                QPushButton:pressed {{
                    background-color: {self.pressed.name()};
           }}""" )

        

        

        
         
    def setup_layout(self):


        layout = QHBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.label, 3)
        layout.addStretch(1)
        layout.addWidget(self.selector, 7)
        layout.addStretch(1)
        layout.addWidget(self.submit_button, 3)

        self.setLayout(layout)
       

    def setup_connections(self):
        self.exact_spinbox.valueChanged.connect(self.spinbox_police_change)



    def spinbox_police_change(self):
        self.exact_spinbox.setFont(QFont("Arial Black", 30))
        self.exact_spinbox.lineEdit().setFont(QFont("Arial Black", 30))
       
            

    



