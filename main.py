from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTextEdit, QDesktopWidget, QVBoxLayout
import sys
from PPTX_DataSet_Maker import make_ppt

class make_gui(QWidget):
    def __init__(self):
        super().__init__()
        print("Log : App Started")

        self.initUI()

    def initUI(self):

        btn = QPushButton('Return', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        # btn.clicked.connect()

        self.lbl1 = QLabel('Enter your sentence:')
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        self.lbl2 = QLabel()
        # text = '\n'.join(f.test())
        # self.lbl2.setText(text)


        self.te.textChanged.connect(self.text_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def text_changed(self):
        directory = self.te.toPlainText()
        f = make_ppt()
        text = '\n'.join(f.test(directory))
        self.lbl2.setText('The target directory is \n' + text)

    def center(self): # 가운데 정렬
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = make_gui()
    sys.exit(app.exec_())
