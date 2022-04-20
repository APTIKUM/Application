from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont, QPixmap  # проверка типов вводимых значений
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from TXT import *

class FinalWin(QWidget):
    def __init__(self, exp):
        ''' окно, в котором проводится опрос '''
        super().__init__()

        # получаем данные об эксперименте
        self.exp = exp

        # создаём и настраиваем графические элементы:
        self.initUI()

        # устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()

        # старт:
        self.show()

    def set_appear(self):
        # название окна его размеры впрочем как и всегда
        self.setWindowTitle('Тест Руфье 3')
        self.resize(win_width, win_height)

    def initUI(self):
        # отрисование всего там копок линий и короче всего
        self.final_index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        self.lbl_score = QLabel('Ваш индекс Руфье: ' + str(self.final_index))
        self.lbl_score.setFont(QFont('Arial', 36))
        self.pixmap = QPixmap('cell.jpg')
        self.lbl = QLabel()
        self.lbl.setPixmap(self.pixmap)
        self.h_line = QVBoxLayout()
        self.h_line.addWidget(self.lbl)
        self.h_line.addWidget(self.lbl_score, alignment = Qt.AlignCenter)
        self.setLayout(self.h_line)