from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QStackedWidget, QFrame
from PySide6.QtGui import Qt, QIcon, QFont
from PySide6.QtCore import QSize
from pages.training_pages.training_page_home import TrainingPageHome
from pages.training_pages.training_page_settings import TrainingPageSettings
from pages.training_pages.training_page_game import TrainingPageGame
from pages.training_pages.training_page_results import TrainingPageResults




class TrainingPage(QWidget):
    def __init__(self):


        


        super().__init__()
        self.stack = QStackedWidget()
        self.home_page = TrainingPageHome()
        self.settings_page = TrainingPageSettings()
        self.game_page = TrainingPageGame()
        self.results_page = TrainingPageResults()

        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.settings_page)
        self.stack.addWidget(self.game_page)
        self.stack.addWidget(self.results_page)

        self.showHome()

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

        self.home_page.button.clicked.connect(self.showSettings)
        self.settings_page.startButton.clicked.connect(self.showGame)


    def showHome(self):
        self.stack.setCurrentWidget(self.home_page)
        

    def showSettings(self):
        self.stack.setCurrentWidget(self.settings_page)
        

    def showGame(self):
        self.game_page.gather_settings()
        self.stack.setCurrentWidget(self.game_page)
        self.game_page.pre_game()

        
    