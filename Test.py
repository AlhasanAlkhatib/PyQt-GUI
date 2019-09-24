import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Sicaklik'))
layout.addWidget(QPushButton('Nem'))
window.setLayout(layout)
window.show()
app.exec_()
