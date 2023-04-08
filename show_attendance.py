import pandas as pd
from glob import glob
import os
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
WIDTH=0
HEIGHT=0

def calculate_attendance(Subject,self,text_to_speech):
    if Subject=="":
        t='Please enter the subject name.'
        self.ui.Output.setText(t)
        text_to_speech(t)
        return None
    if not os.path.exists(f"C:\\Users\\gkara\\Desktop\\FR_AS_UI\\Attendance\\{Subject}"):
        t='Subject not found '
        print("Error")
        self.ui.Output.setText(t)
        text_to_speech(t)
        return None

    os.chdir(f"C:\\Users\\gkara\\Desktop\\FR_AS_UI\\Attendance\\{Subject}")
    filenames = glob(f"C:\\Users\\gkara\\Desktop\\FR_AS_UI\\Attendance\\{Subject}\\{Subject}*.csv")
    df = [pd.read_csv(f) for f in filenames]
    newdf = df[0]
    for i in range(1, len(df)):
        newdf = newdf.merge(df[i], how="outer")
    newdf.fillna(0, inplace=True)
    newdf["Attendance"] = 0
    for i in range(len(newdf)):
        newdf["Attendance"].iloc[i] = str(int(round(newdf.iloc[i, 2:-1].mean() * 100)))+'%'
    newdf.to_csv("attendance.csv", index=False)
    cs=f"C:\\Users\\gkara\\Desktop\\FR_AS_UI\\Attendance\\{Subject}\\attendance.csv"
    print(cs)
    with open(cs) as file:
        reader = list(csv.reader(file))
        WIDTH=len(reader[0])*135+50
        HEIGHT=len(reader)*50+50
        
    # Attendance Screen
    class Attendancesheet(QWidget):  
        def __init__(self):  
            super().__init__() 
            self.setWindowIcon(QtGui.QIcon('icon.png'))
            self.title = 'Attendance Sheets of '+Subject  
            self.left = 0  
            self.top = 0  
            self.width = WIDTH  
            self.height = HEIGHT
            self.setWindowTitle(self.title)  
            self.setGeometry(self.left, self.top, self.width, self.height)  
            self.creatingTable()  
            self.layout = QVBoxLayout()  
            self.layout.addWidget(self.table)  
            self.setLayout(self.layout)  
            self.show()  

        #Creating the table  
        def creatingTable(self):  
            self.table = QTableWidget(self)
            
            self.table.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 70 14pt \"Tahoma\";")
            
            cs=f"C:\\Users\\gkara\\Desktop\\FR_AS_UI\\Attendance\\{Subject}\\attendance.csv"
            print(cs)
            with open(cs) as file:
                reader = list(csv.reader(file))
                print(reader)
                self.table.setColumnCount(len(reader[0]))
                for c in range(len(reader[0])):
                        self.table.setColumnWidth(c, 135)

                self.table.setHorizontalHeaderLabels(reader[0])
                self.table.setRowCount(len(reader)-1)

                row = 0

                for e in reader[1:]:
                    for c in range(len(reader[0])):
                        self.table.setItem(row, c, QTableWidgetItem(e[c]))
                    row += 1 
            self.table.horizontalHeader().setStretchLastSection(True)
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.main=Attendancesheet()
    self.main.show()

def Att_sheets(sub,self,text_to_speech):
    if sub == "":
        t="Please enter the subject name!!!"
        self.ui.Output.setText(t)
        text_to_speech(t)
    else:
        os.startfile(
        f"C:\\Users\\gkara\\Desktop\\FR_AS_UI\\Attendance\\{sub}"
        
        )

