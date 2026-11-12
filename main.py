from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

app = QApplication([])

main_win = QWidget()
button = QPushButton('hola')

main_layout = QVBoxLayout()
main_layout.addWidget(button)

main_win.setLayout(main_layout)
main_win.show()
app.exec_()


