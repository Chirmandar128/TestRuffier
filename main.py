from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from random import randint

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Determinante ganador')
main_win.resize(300,150)
text = QLabel('Click para descubrir el ganador')
winner = QLabel('¿?')
button = QPushButton('generar')

main_layout = QVBoxLayout()
main_layout.addWidget(text)
main_layout.addWidget(winner)
main_layout.addWidget(button)



def prueba()
    winner.setText(randint(0,100))

button.clicked.connect(prueba)


main_win.setLayout(main_layout)
main_win.show()
app.exec_()


