# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_viewscreen(object):
    def setupUi(self, viewscreen):
        viewscreen.setObjectName("viewscreen")
        viewscreen.resize(700, 440)
        self.centralwidget = QtWidgets.QWidget(viewscreen)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 700, 440))
        self.bg.setStyleSheet("\n"
"background: url(:/ui/main_bg.jpeg)  no-repeat center center fixed;")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.View_attendance = QtWidgets.QPushButton(self.centralwidget)
        self.View_attendance.setGeometry(QtCore.QRect(80, 350, 200, 45))
        self.View_attendance.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.View_attendance.setStyleSheet("QPushButton\n"
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
        self.View_attendance.setObjectName("View_attendance")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(115, 5, 450, 91))
        self.Title.setStyleSheet("image: url(:/ui/attendance.png);")
        self.Title.setText("")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.sub_name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.sub_name_input.setGeometry(QtCore.QRect(350, 200, 250, 40))
        self.sub_name_input.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.sub_name_input.setObjectName("sub_name_input")
        self.subject_name = QtWidgets.QLabel(self.centralwidget)
        self.subject_name.setGeometry(QtCore.QRect(120, 190, 200, 50))
        self.subject_name.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 21pt \"Times New Roman\";")
        self.subject_name.setAlignment(QtCore.Qt.AlignCenter)
        self.subject_name.setObjectName("subject_name")
        self.Enter_details = QtWidgets.QLabel(self.centralwidget)
        self.Enter_details.setGeometry(QtCore.QRect(140, 100, 400, 50))
        self.Enter_details.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 70 24pt \"Tahoma\";")
        self.Enter_details.setAlignment(QtCore.Qt.AlignCenter)
        self.Enter_details.setObjectName("Enter_details")
        self.chech_sheets = QtWidgets.QPushButton(self.centralwidget)
        self.chech_sheets.setGeometry(QtCore.QRect(400, 350, 200, 45))
        self.chech_sheets.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chech_sheets.setStyleSheet("QPushButton\n"
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
        self.chech_sheets.setObjectName("chech_sheets")
        self.Output = QtWidgets.QLabel(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(0, 270, 700, 50))
        self.Output.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 70 19pt \"Tahoma\";")
        self.Output.setText("")
        self.Output.setAlignment(QtCore.Qt.AlignCenter)
        self.Output.setObjectName("Output")
        viewscreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(viewscreen)
        QtCore.QMetaObject.connectSlotsByName(viewscreen)

    def retranslateUi(self, viewscreen):
        _translate = QtCore.QCoreApplication.translate
        viewscreen.setWindowTitle(_translate("viewscreen", "MainWindow"))
        self.View_attendance.setText(_translate("viewscreen", "View Attendance"))
        self.subject_name.setText(_translate("viewscreen", "Subject Name"))
        self.Enter_details.setText(_translate("viewscreen", "Enter The Subject Name"))
        self.chech_sheets.setText(_translate("viewscreen", "Check Sheets"))
import registerscreen_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewscreen = QtWidgets.QMainWindow()
    ui = Ui_viewscreen()
    ui.setupUi(viewscreen)
    viewscreen.show()
    sys.exit(app.exec_())
