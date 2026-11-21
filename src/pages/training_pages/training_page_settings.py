from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QStackedWidget, QFrame, QHBoxLayout, QRadioButton, QButtonGroup
from PySide6.QtGui import Qt, QIcon, QFont
from PySide6.QtCore import QSize
from widgets.modeSelector import modeSelector
from widgets.rangeSelector import rangeSelector
from widgets.timeSelector import timeSelector
from config.settings import settings




class TrainingPageSettings(QWidget):
    
    def __init__(self):

        super().__init__()
       

        
        self.settings = settings


        layout = QVBoxLayout()


            
                
        label = QLabel("Settings")

        SettingsBox = QFrame()
        SettingsBox.setFrameShape(QFrame.Shape.StyledPanel)


        settingsLayout = QVBoxLayout()

        self.modeSelectorWidget = modeSelector()
        self.rangeSelectorWidget = rangeSelector()
        self.timeSelectorWidget = timeSelector()

        self.connect_signals()

        self.startButton = QPushButton("Start")
        self.startButton.setFont(QFont("Arial", 30))
        

        


        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label.setFont(QFont("Arial", 30))



        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignHCenter, stretch=2)
        layout.addWidget(SettingsBox, 14)


        settingsLayout.addWidget(self.modeSelectorWidget, 1)
        settingsLayout.addWidget(self.rangeSelectorWidget, 1)
        settingsLayout.addWidget(self.timeSelectorWidget, 1)
        settingsLayout.addStretch(8)
        settingsLayout.addWidget(self.startButton, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        settingsLayout.addStretch(3)


    
        SettingsBox.setLayout(settingsLayout)
        self.setLayout(layout)

        self.load_settings()


        
    def load_settings(self):
        self.rangeSelectorWidget.update_range(self.settings.value("range"))
        print("Loaded range from settings:", type(self.settings.value("range")[0]))
        self.modeSelectorWidget.update_mode(self.settings.value("mode", type=int))
        self.timeSelectorWidget.update_time(self.settings.value("time", type=float))

    def connect_signals(self):
        self.modeSelectorWidget.mode_changed.connect(self.update_mode)
        self.rangeSelectorWidget.range_changed.connect(self.update_range)
        self.timeSelectorWidget.time_changed.connect(self.update_time)


    def update_mode(self, mode):
        self.settings.setValue("mode", mode)
        self.settings.sync()
        

    def update_range(self, min_value, max_value):
        self.settings.setValue("range", (min_value, max_value))
        self.settings.sync()
        
        

    def update_time(self, time):
        self.settings.setValue("time", time)
        self.settings.sync()
        
        