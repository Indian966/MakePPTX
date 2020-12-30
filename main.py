from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys

class make_gui(QWidget):
    def __init__(self):
        super().__init__()
        print("Log : App Started")
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('My First GUI')
        self.move(300, 300)
        self.resize(400,400)
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = make_gui()
    sys.exit(app.exec_())
