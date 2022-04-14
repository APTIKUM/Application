from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
from time import *
from TXT import *

class TestWin(QWidget):
    # конструктор который сразу отрисовывает всё
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        #self.connects()
        self.show()


    def set_appear(self):
        #название окна, его размеры и в какой точке оно будет находиться
        self.setWindowTitle('Тест Руфье')
        self.resize(1000, 600)
        #self.move(200, 100)


    def initUI(self):
        # медот корый отрисовывает всё(кнопки линии и др)
        self.btn_next = QPushButton(mw2_button4, self)
        self.btn_test1 = QPushButton(mw2_button1, self)
        self.btn_test2 = QPushButton(mw2_button2, self)
        self.btn_test3 = QPushButton(mw2_button3, self)

        self.text_name = QLabel(mw2_name)
        self.text_age = QLabel(mw2_age)
        self.text_age.setFont(QFont('Arial', 10))
        self.text_test1 = QLabel(mw2_test1)
        self.text_test1.setFont(QFont('Arial', 10))
        self.text_test2 = QLabel(mw2_test2)
        self.text_test2.setFont(QFont('Arial', 10))
        self.text_test3 = QLabel(mw2_test3)
        self.text_test3.setFont(QFont('Arial', 10))
        self.text_timer = QLabel(str(mw2_timer))
        self.text_timer.setFont(QFont('Arial', 50))

        self.timing = time()

        self.line_name = QLineEdit()#'txt_hintname'
        self.line_age = QLineEdit()#'txt_hintage'
        self.line_test1 = QLineEdit()#'txt_hinttest1'
        self.line_test2 = QLineEdit()#'txt_hinttest2'
        self.line_test3 = QLineEdit()#'txt_hinttest3'

        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        #это про касания кнопок
        pass

app = QApplication([])
mw = TestWin()
app.exec_()