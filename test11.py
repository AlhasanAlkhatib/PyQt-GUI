# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    
    x=0
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label1= QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(10, 10, 80, 15))
        self.label1.setText("buton basilmistir")
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(70, 80, 75, 23))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QToolButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(150, 160, 25, 19))
        self.pushButton2.setObjectName("pushButton2")
        self.verticalSlider = QtWidgets.QSlider(Form)
        self.verticalSlider.setGeometry(QtCore.QRect(230, 70, 22, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(220, 40, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton1.setText(_translate("Form", "PushButton"))
        self.pushButton1.clicked.connect(self.clicked)
        self.pushButton2.setText(_translate("Form", "BIIB"))

    def clicked(self):
        self.x=self.x+1
        self.label1.setGeometry((QtCore.QRect(10+self.x, 10+self.x, 80+self.x, 15+self.x)))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
