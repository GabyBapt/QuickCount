from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QStackedWidget, QFrame, QHBoxLayout, QSpinBox, QStyleFactory
from PySide6.QtGui import Qt, QIcon, QFont
from PySide6.QtCore import QSize, Signal
from superqt import QLabeledSlider

class RoundCountSelector(QWidget):

    round_count_changed = Signal(int)

    def __init__(self):
        super().__init__()

       
        self.setup_widgets()
        self.setup_layout()
        self.setup_connections()


        
    def setup_widgets(self):
        self.label = QLabel("Number of round :") 
        self.label.setFont(QFont("Arial", 17)) 

        self.slider = QLabeledSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(5, 50)
        


        self.time_spinbox = QSpinBox()
 
        style = QStyleFactory.create("Windows")

        self.time_spinbox.setStyle(style)

        





    def setup_layout(self):
        layout = QHBoxLayout()
 
        layout.addWidget(self.label, 3)
        
        layout.addWidget(self.slider, 7)
        layout.addWidget(self.time_spinbox, 1)
        
    


        self.setLayout(layout)

    def setup_connections(self):
       self.slider.sliderMoved.connect(self.slider_movement)
       self.time_spinbox.valueChanged.connect(self.spinbox_update)
      

    def slider_movement(self, value):
        self.time_spinbox.setValue(value)

    def spinbox_update(self, value):
        self.slider.setValue(value)

    def update_time(self, time): 

        self.time_spinbox.blockSignals(True)
       

        self.time_spinbox.setValue(time)
        self.slider.setValue(time)

        self.time_spinbox.blockSignals(False)
        