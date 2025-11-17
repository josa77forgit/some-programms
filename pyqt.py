#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QApplication, QHBoxLayout, QRadioButton, QPushButton, QWidget, QLabel, QVBoxLayout

def show_win():
    win = QMessageBox()
    win.setText('Верно! Вы выиграли!')
    win.exec_()

def show_lose():
    win = QMessageBox()
    win.setText('Нет, оказывается, это синий кит')
    win.exec_()

#создание приложения и главного окна
app = QApplication([])
window = QWidget()
window.resize(300, 150)
window.setWindowTitle('Викторина')
question = QLabel('Какое животное в мире самое большое?')
box = QHBoxLayout()
box.addWidget(question, alignment = Qt.AlignCenter)
#создание виджетов главного окна
answer1 = QRadioButton('Касатка')
answer2 = QRadioButton('Слон')
answer3 = QRadioButton('Синий кит')
answer4 = QRadioButton('Белый медведь')
box1 = QHBoxLayout()
box2 = QHBoxLayout()
box1.addWidget(answer1, alignment = Qt.AlignCenter)
box1.addWidget(answer2, alignment = Qt.AlignCenter)
box2.addWidget(answer3, alignment = Qt.AlignCenter)
box2.addWidget(answer4, alignment = Qt.AlignCenter)
main_boxLO = QVBoxLayout()
main_boxLO.addLayout(box)
main_boxLO.addLayout(box1)
main_boxLO.addLayout(box2)
window.setLayout(main_boxLO)
answer1.clicked.connect(show_lose)
answer2.clicked.connect(show_lose)
answer3.clicked.connect(show_win)
answer4.clicked.connect(show_lose)
#расположение виджетов по лэйаутам
#обработка нажатий на переключатели
 
#отображение окна приложения
window.show()
app.exec_()