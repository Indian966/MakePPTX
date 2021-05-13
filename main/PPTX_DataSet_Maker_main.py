from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTextEdit, QVBoxLayout
import sys
from main.PPTX_DataSet_Maker import make_ppt

class Thread(QThread) :
    # sig = pyqtSignal(str)
    def __init__(self, directory):
        super().__init__()
        self.directory = directory

    def run(self) :
        print("Log : save directory button")
        f = make_ppt()
        # f.ppt_work(self.directory)
        try :
            f.ppt_work(self.directory)
        except :
            print("Log : Failed making pptx")

class make_gui(QWidget):
    def __init__(self):
        super().__init__()
        self.thread = Thread(self)
        print("Log : App Started")
        self.initUI()

    def initUI(self):
        # 버튼
        self.dir_return = QPushButton('Return', self)
        self.dir_return.clicked.connect(self.text_changed)
        self.save_return = QPushButton('Return', self)
        self.save_return.clicked.connect(self.ppt_work) ## 피피티 만드는 함수 호출

        # 레이블, 텍스트박스
        self.lbl1 = QLabel('Enter target directory :')
        self.sub_dir_lbl = QLabel()
        self.save_lbl = QLabel('Enter save directory :')
        self.dir_input_te = QTextEdit()
        self.dir_input_te.setAcceptRichText(False)
        self.save_dir_te = QTextEdit()
        self.save_dir_te.setAcceptRichText(False)

        # 버티컬 레이아웃
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.dir_input_te)
        vbox.addWidget(self.dir_return)
        vbox.addWidget(self.sub_dir_lbl)
        vbox.addWidget(self.save_lbl)
        vbox.addWidget(self.save_dir_te)
        vbox.addWidget(self.save_return)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def text_changed(self):
        target_dir = self.dir_input_te.toPlainText() # 입력한 경로
        f = make_ppt()
        text = '\n'.join(f.pre_view(target_dir))

        self.sub_dir_lbl.setText('The sub directory is :\n' + text)

    def ppt_work(self):
        directory = self.save_dir_te.toPlainText()
        self.i = Thread(directory) #쓰레드에 경로 할당
        self.i.start()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = make_gui()
    sys.exit(app.exec_())
