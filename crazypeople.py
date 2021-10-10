from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,QMessageBox, QRadioButton

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс!!!')
question = QLabel('В каком году канал получил золотую кнопку от ютуб')
bt_ans1 = QRadioButton('2005')
bt_ans2 = QRadioButton('2010')
bt_ans3 = QRadioButton('2015')
bt_ans4 = QRadioButton('2020')
layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(bt_ans1, alignment = Qt.AlignCenter)
layoutH2.addWidget(bt_ans2, alignment = Qt.AlignCenter)
layoutH3.addWidget(bt_ans3, alignment = Qt.AlignCenter)
layoutH3.addWidget(bt_ans4, alignment = Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout(layout_main)

def show_win():
    victory_win = QMessageBox()
    victory_win.setText('o right!')
    victory_win.exec_()

def show_lose():
    victory_win = QMessageBox()
    victory_win.setText('NO!!!')  
    victory_win.exec_()  

bt_ans3.clicked.connect(show_win)
bt_ans1.clicked.connect(show_lose)
bt_ans2.clicked.connect(show_lose)
bt_ans4.clicked.connect(show_lose)

main_win.show()
app.exec_()