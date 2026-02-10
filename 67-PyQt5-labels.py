# PyQt5 introduction
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My cool first GUI")
    self.setGeometry(700,300,500,500)
    self.setWindowIcon(QIcon("Images/images.jpg"))

    label = QLabel("Hello", self)
    label.setFont(QFont("Arial",25))
    label.setGeometry(0,0,500,100)
    label.setStyleSheet("color: black;"
                        "background-color: #6fdcf7;"
                        "font-weight: bold;"
                        "font-style: italic;"
                        "text-decoration: underline;")
    
    #label.setAlignment(Qt.AlignTop)      # VERTICALLY TOP
    #label.setAlignment(Qt.AlignBottom)   # VERTICALLY BOTTOM
    #label.setAlignment(Qt.AlignVCenter)  # VERTICALLY BOTTOM

    #label.setAlignment(Qt.AlignRight)    # HORIZONTALY RIGHT
    #label.setAlignment(Qt.AlignLeft)     # HORIZONTALY Left
    #label.setAlignment(Qt.AlignHCenter)  # HORIZONTALY CENTER

    #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  #CENTER & CENTER
    label.setAlignment(Qt.AlignCenter) # CENTER & CENTER

def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()

