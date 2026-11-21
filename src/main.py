from PySide6.QtWidgets import *
from PySide6.QtGui import QFont, QFontDatabase
import sys

app = QApplication(sys.argv)
app.setOrganizationName("GabyDev")
app.setApplicationName("QuickCount")

from pages.training_pages.training_page import TrainingPage
from pages.stats_page import StatPage
from widgets.navbar import NavBar




class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        
        
        self.setWindowTitle("My App")
        self.resize(1300, 700)
        self.setUpPages()
        self.navbar = NavBar()
        self.setUpCentral() 
        self.setUpConnections()

        
        self.pages.setCurrentWidget(self.training_page)

        

    def setUpPages(self):
        self.training_page = TrainingPage()
        self.stats_page = StatPage()    
        self.navbar = NavBar()


        self.pages = QStackedWidget()
        self.pages.addWidget(self.training_page)
        self.pages.addWidget(self.stats_page)




    def setUpCentral(self):
        central = QWidget()
        central_layout = QHBoxLayout()


        central_layout.addWidget(self.navbar, 1)
        
        central_layout.addWidget(self.pages, 5)
        

        central.setLayout(central_layout)
        self.setCentralWidget(central)
        
               

    def setUpConnections(self):
        self.navbar.training_page_button.clicked.connect(self.training_page_button_clicked)
        self.navbar.stats_page_button.clicked.connect(self.stats_page_button_clicked)
        self.training_page.game_page.hide_navbar_signal.connect(self.navbar.hide_navbar)

    def training_page_button_clicked(self):
        self.pages.setCurrentIndex(0)
        self.training_page.showHome()

    def stats_page_button_clicked(self):
        self.pages.setCurrentIndex(1)
        




window = MainWindow()
window.show()

app.exec()