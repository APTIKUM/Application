from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
from TXT import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        # название окна его размеры впрочем как и всегда
        self.setWindowTitle('Тест Руфье 3')
        self.resize(size_win_w, size_win_h)


    def initUI(self):
        # отрисование всего там копок линий и короче всего
        self.lbl_score = QLabel('Индекс Руфье: ' + str(final_index))
        self.lbl_score.setFont(QFont('Arial', 10))
        self.lbl_works_heart = QLabel('Работоспособность сердца: ' + final_heart)
        self.lbl_works_heart.setFont(QFont('Arial', 10))

        self.h_line = QVBoxLayout()

        self.h_line.addWidget(self.lbl_score, alignment = Qt.AlignCenter)
        self.h_line.addWidget(self.lbl_works_heart, alignment = Qt.AlignCenter)

        self.setLayout(self.h_line)


    def connects(self):
        pass



app = QApplication([])
mw = FinalWin()
app.exec_()