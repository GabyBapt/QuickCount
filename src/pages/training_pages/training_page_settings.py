from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QStackedWidget, QFrame, QHBoxLayout, QRadioButton, QButtonGroup
from PySide6.QtGui import Qt, QIcon, QFont
from PySide6.QtCore import QSize
from widgets.modeSelector import modeSelector
from widgets.rangeSelector import rangeSelector
from widgets.timeSelector import timeSelector
from config.settings import TrainingSettings




class TrainingPageSettings(QWidget):
    
    def __init__(self):

        super().__init__()
       

        
        self.settings = TrainingSettings()
        
        layout = QVBoxLayout()


            
                
        label = QLabel("Settings")

        SettingsBox = QFrame()
        SettingsBox.setFrameShape(QFrame.Shape.StyledPanel)


        settingsLayout = QVBoxLayout()

        self.modeSelectorWidget = modeSelector()
        self.rangeSelectorWidget = rangeSelector()
        self.timeSelectorWidget = timeSelector()

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
        self.rangeSelectorWidget.update_range(self.settings.range)
        self.modeSelectorWidget.update_mode(self.settings.mode)
        self.timeSelectorWidget.update_time(self.settings.time)