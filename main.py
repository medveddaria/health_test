from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Моё первое приложение')
main_win.move(900, 70)
main_win.resize(400, 200)
main_win.show()

line = QVBoxLayout()
button = QPushButton('Кнопка с секретом!')
line.addWidget(button, alignment=Qt.AlignCenter)
main_win.setLayout(line)

def show_fun_title():
    fun_title = QLabel('Ты просто чудо!')
    line.addWidget(fun_title, alignment = Qt.AlignCenter)
    main_win.setLayout(line)

button.clicked.connect(show_fun_title)

app.exec_()
