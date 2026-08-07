from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QStackedWidget, QFrame, QHBoxLayout, QSpinBox, QStyleFactory, QDoubleSpinBox
from PySide6.QtGui import Qt, QIcon, QFont
from PySide6.QtCore import QSize, Signal
from superqt import QLabeledDoubleSlider

class timeSelector(QWidget):

    time_changed = Signal(float)

    def __init__(self):
        super().__init__()

       
        self.setup_widgets()
        self.setup_layout()
        self.setup_connections()


        
    def setup_widgets(self):
        self.label = QLabel("Counting Time :") 
        self.label.setFont(QFont("Arial", 17)) 

        self.slider = QLabeledDoubleSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 10)
        


        self.time_spinbox = QDoubleSpinBox()
 
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
        