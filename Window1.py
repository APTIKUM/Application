from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGridLayout, QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)
from TXT import *
from Window2 import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear() # устанавливает, как будет выглядеть окно
        self.initUI() # создаём и настраиваем графические элементы
        self.connects() # устанавливает связи между элементами
        self.show() # старт


    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        #self.move(win_x, win_y)


    def initUI(self): 
        self.hello_text = QLabel(txt_hello)
        self.hello_text.setFont(QFont('Arial', 10))
        self.instruction = QLabel(txt_instruction)
        self.instruction.setFont(QFont('Arial', 10))
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)


    def connects(self): 
        self.button.clicked.connect(self.next_click)


    def next_click(self):
        self.hide()
        self.tw = TestWin()
        #создание следующего окна


app = QApplication([])
mw = MainWin()
app.exec_()