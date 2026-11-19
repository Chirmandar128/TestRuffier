from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

app = QApplication([])

main_win = QWidget()
button = QPushButton('hola')
button2 = QPushButton('hola')
button3 = QPushButton('hola')
button4 = QPushButton('hola')

main_layout = QVBoxLayout()
main_layout.addWidget(button)
main_layout.addWidget(button2)
main_layout.addWidget(button3)
main_layout.addWidget(button4)

main_win.setLayout(main_layout)
main_win.show()
app.exec_()


