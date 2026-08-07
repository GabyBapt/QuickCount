import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Radiodemo(QScrollArea):

    def __init__(self):
      super().__init__()

      container = QWidget()
      layout = QVBoxLayout()
      label = QLabel(
                     "Ceci est une phrase de test permettant de comparer les différentes fontes disponibles 12 33 35 6783 904"
                  )
      label.setFont(QFont("Arial Black", 20))
      layout.addWidget(label)

      for font in QFontDatabase.families():
         label = QLabel(
               "Ceci est une phrase de test permettant de comparer les différentes fontes disponibles 12 33 35 6783 904"
         )
         label.setFont(QFont(font, 20))
         layout.addWidget(label)

      container.setLayout(layout)

      self.setWidget(container)
      self.setWidgetResizable(True)


def main():
    app = QApplication(sys.argv)

    ex = Radiodemo()
    ex.resize(800, 600)
    ex.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()