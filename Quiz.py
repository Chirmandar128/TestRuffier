from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox


app = QApplication([])


window = QWidget()
mensaje = QMessageBox()
window.resize(200,120)

text = QLabel('Cuando fue fundado algonova')

rb1 = QRadioButton('2013')
rb2 = QRadioButton('2010')
rb3 = QRadioButton('2016')
rb4 = QRadioButton('2019')


h_layout1 = QHBoxLayout()
h_layout1.addWidget(rb1, alignment=Qt.AlignCenter)
h_layout1.addWidget(rb2, alignment=Qt.AlignCenter)


h_layout2 = QHBoxLayout()
h_layout2.addWidget(rb3, alignment=Qt.AlignCenter)
h_layout2.addWidget(rb4, alignment=Qt.AlignCenter)



main_layout = QVBoxLayout()
main_layout.addWidget(text)
main_layout.addLayout(h_layout1)
main_layout.addLayout(h_layout2)
window.setLayout(main_layout)

def correcto():
    mensaje.setText('correcto!!!')
    mensaje.show()
    window.close()

def incorrecto():
    mensaje.setText('incorrecto')
    mensaje.show()


rb3.clicked.connect(correcto)
rb1.clicked.connect(incorrecto)
rb2.clicked.connect(incorrecto)
rb4.clicked.connect(incorrecto)



window.show()
app.exec_()