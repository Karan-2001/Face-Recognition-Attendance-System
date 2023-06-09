# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Registerscreen(object):
    def setupUi(self, Registerscreen):
        Registerscreen.setObjectName("Registerscreen")
        Registerscreen.resize(700, 440)
        self.centralwidget = QtWidgets.QWidget(Registerscreen)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 700, 440))
        self.bg.setStyleSheet("\n"
"background: url(:/ui/main_bg.jpeg)  no-repeat center center fixed;")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(25, 0, 650, 91))
        self.Title.setStyleSheet("image: url(:/ui/register your face (2).png);")
        self.Title.setText("")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Enter_details = QtWidgets.QLabel(self.centralwidget)
        self.Enter_details.setGeometry(QtCore.QRect(210, 90, 280, 50))
        self.Enter_details.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 70 24pt \"Tahoma\";")
        self.Enter_details.setAlignment(QtCore.Qt.AlignCenter)
        self.Enter_details.setObjectName("Enter_details")
        self.Number = QtWidgets.QLabel(self.centralwidget)
        self.Number.setGeometry(QtCore.QRect(130, 160, 200, 50))
        self.Number.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 21pt \"Times New Roman\";")
        self.Number.setAlignment(QtCore.Qt.AlignCenter)
        self.Number.setObjectName("Number")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(130, 230, 200, 50))
        self.Name.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 21pt \"Times New Roman\";")
        self.Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Name.setObjectName("Name")
        self.number_input = QtWidgets.QLineEdit(self.centralwidget)
        self.number_input.setGeometry(QtCore.QRect(350, 170, 250, 35))
        self.number_input.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.number_input.setObjectName("number_input")
        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(350, 240, 250, 35))
        self.name_input.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.name_input.setObjectName("name_input")
        self.Output = QtWidgets.QLabel(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(0, 290, 700, 50))
        self.Output.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 70 19pt \"Tahoma\";")
        self.Output.setText("")
        self.Output.setAlignment(QtCore.Qt.AlignCenter)
        self.Output.setObjectName("Output")
        self.Take_image = QtWidgets.QPushButton(self.centralwidget)
        self.Take_image.setGeometry(QtCore.QRect(90, 370, 200, 45))
        self.Take_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Take_image.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(170, 255, 255);\n"
"    font: 75 18pt \"Times New Roman\";\n"
"    border-radius: 12px;\n"
"}\n"
"QPushButton:hover\n"
"{font: 75 20pt \"Times New Roman\";\n"
"    background-color: rgb(75, 225, 225);\n"
"}\n"
"QPushButton:pressed \n"
"{\n"
"    background-color: rgb(52, 143, 255);\n"
"}")
        self.Take_image.setObjectName("Take_image")
        self.Train_image = QtWidgets.QPushButton(self.centralwidget)
        self.Train_image.setGeometry(QtCore.QRect(410, 370, 200, 45))
        self.Train_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Train_image.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(170, 255, 255);\n"
"    font: 75 18pt \"Times New Roman\";\n"
"    border-radius: 12px;\n"
"}\n"
"QPushButton:hover\n"
"{font: 75 20pt \"Times New Roman\";\n"
"    background-color: rgb(75, 225, 225);\n"
"}\n"
"QPushButton:pressed \n"
"{\n"
"    background-color: rgb(52, 143, 255);\n"
"}")
        self.Train_image.setObjectName("Train_image")
        Registerscreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(Registerscreen)
        QtCore.QMetaObject.connectSlotsByName(Registerscreen)

    def retranslateUi(self, Registerscreen):
        _translate = QtCore.QCoreApplication.translate
        Registerscreen.setWindowTitle(_translate("Registerscreen", "MainWindow"))
        self.Enter_details.setText(_translate("Registerscreen", "Enter Your Details"))
        self.Number.setText(_translate("Registerscreen", "Enrollment No."))
        self.Name.setText(_translate("Registerscreen", "Name"))
        self.Take_image.setText(_translate("Registerscreen", "Take Image"))
        self.Train_image.setText(_translate("Registerscreen", "Train Image"))
import registerscreen_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registerscreen = QtWidgets.QMainWindow()
    ui = Ui_Registerscreen()
    ui.setupUi(Registerscreen)
    Registerscreen.show()
    sys.exit(app.exec_())
