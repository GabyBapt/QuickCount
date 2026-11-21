from PySide6.QtWidgets import  QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSpinBox, QStyleFactory
from PySide6.QtGui import Qt, QFont
from PySide6.QtCore import Signal
from superqt import QLabeledRangeSlider



class rangeSelector(QWidget):

    range_changed = Signal(int, int)
    


    def __init__(self):
        super().__init__()
        self.style = QStyleFactory.create("Windows")
        self.setup_widgets()
        self.setup_layout()
        self.setup_connections()
    


    def setup_widgets(self):
        self.range_label = QLabel("Number of Objects :") 
        self.range_label.setFont(QFont("Arial", 17))

        self.slider = QLabeledRangeSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 200)
        self.slider.setBarMovesAllHandles(False)

        self.mini_label = QLabel("Minimum :")
        self.mini_label.setFont(QFont("Arial", 12))
        self.maxi_label = QLabel("Maximum :")
        self.maxi_label.setFont(QFont("Arial", 12))

        self.min_spinbox = QSpinBox()
        self.max_spinbox = QSpinBox()
        
        self.min_spinbox.setRange(0, 200)
        self.max_spinbox.setRange(0, 200)
        style = QStyleFactory.create("windowsvista")

        #self.max_spinbox.setStyle(self.style)
        #self.min_spinbox.setStyle(self.style)


    def setup_layout(self):
        layout = QVBoxLayout()
        
        first_layer_layout = QHBoxLayout()
        second_layer_layout = QHBoxLayout()

        first_layer_layout.addWidget(self.range_label, 3)
               
        first_layer_layout.addWidget(self.slider, 8)



        
        
        second_layer_layout.addStretch(8)
        second_layer_layout.addWidget(self.mini_label, 2)
        second_layer_layout.addWidget(self.min_spinbox, 1)
        second_layer_layout.addStretch(5)
        second_layer_layout.addWidget(self.maxi_label, 2)
        second_layer_layout.addWidget(self.max_spinbox, 1)

        layout.addLayout(first_layer_layout)
        layout.addLayout(second_layer_layout)

        self.setLayout(layout)




    def setup_connections(self):
        self.slider.sliderMoved.connect(self.slider_movement)

        self.min_spinbox.valueChanged.connect(self.spinbox_update)
        self.max_spinbox.valueChanged.connect(self.spinbox_update)

    def slider_movement(self, value):

        min = value[0]
        max = value[1]


        self.min_spinbox.blockSignals(True)
        self.max_spinbox.blockSignals(True)

        self.min_spinbox.setValue(min)
        self.max_spinbox.setValue(max)

        self.min_spinbox.blockSignals(False)
        self.max_spinbox.blockSignals(False)

        self.range_changed.emit(min, max)

        

    def spinbox_update(self):

        min = self.min_spinbox.value()
        max = self.max_spinbox.value()

        if min>max : 
            min, max = max, min
            self.min_spinbox.setValue(min)
            self.max_spinbox.setValue(max)
        
        self.slider.setValue((min, max))
        self.range_changed.emit(min, max)


    def update_range(self, value):
        min = value[0]
        max = value[1]


        self.min_spinbox.blockSignals(True)
        self.max_spinbox.blockSignals(True)

        self.min_spinbox.setValue(min)
        self.max_spinbox.setValue(max)
        self.slider.setValue(value)

        self.min_spinbox.blockSignals(False)
        self.max_spinbox.blockSignals(False)
