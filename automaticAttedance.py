import os, cv2
import csv
import pandas as pd
import datetime
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt,QDateTime
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
WIDTH=0
HEIGHT=0
#path
haarcasecade_path ="C:\\Users\\gkara\\Desktop\\FR_AS_UI\\haarcascade_frontalface_default.xml"
trainimagelabel_path = ("C:\\Users\\gkara\\Desktop\\FR_AS_UI\\TrainingImageLabel\\Trainner.yml")
trainimage_path = "C:\\Users\\gkara\\Desktop\\FR_AS_UI\\TrainingImage"
studentdetail_path = ("C:\\Users\\gkara\\Desktop\\FR_AS_UI\\StudentDetails\\studentdetails.csv")
attendance_path = "C:\\Users\\gkara\\Desktop\\FR_AS_UI\\Attendance"

# Fill Attendance
def FillAttendance(sub,self,text_to_speech):
        now = time.time()
        future = now + 20
        print(now)
        print(future)
        if sub == "":
            t = "Please enter the subject name!!!"
            self.ui.Output.setText(t)
            text_to_speech(t)
        else:
            try:
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                try:
                    recognizer.read(trainimagelabel_path)
                except:
                    e = "Model not found,please train model"
                    self.ui.Output.setText(e)
                    text_to_speech(e)
                facecasCade = cv2.CascadeClassifier(haarcasecade_path)
                df = pd.read_csv(studentdetail_path)
                url = "http://192.168.1.2:8080/video"
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ["Enrollment", "Name"]
                attendance = pd.DataFrame(columns=col_names)
                while True:
                    ___, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = facecasCade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        global Id
                        Id, conf = recognizer.predict(gray[y : y + h, x : x + w])
                        if conf < 40:
                            print(conf)
                            global Subject
                            global aa
                            global date
                            global timeStamp
                            Subject = sub
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime(
                                "%Y-%m-%d"
                            )
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime(
                                "%H:%M:%S"
                            )
                            aa = df.loc[df["Enrollment"] == Id]["Name"].values
                            global tt
                            tt = str(Id) + "-" + aa
                            attendance.loc[len(attendance)] = [
                                Id,
                                aa,
                            ]
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
                            cv2.putText(
                                im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4
                            )
                        else:
                            Id = "Unknown"
                            tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(
                                im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4
                            )
                    attendance = attendance.drop_duplicates(
                        ["Enrollment"], keep="first"
                    )
                    cv2.imshow("Filling Attendance...", im)
                    if (cv2.waitKey(1) == ord('q')):
                        break

                ts = time.time()
                print(aa)
                attendance[date] = 1
                date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
                Hour, Minute, Second = timeStamp.split(":")
                path = os.path.join(attendance_path, sub)
                if not os.path.exists(path):
                    os.mkdir(path)
                fileName = (
                    f"{path}/"
                    + Subject
                    + "_"
                    + date
                    + "_"
                    + Hour
                    + "-"
                    + Minute
                    + "-"
                    + Second
                    + ".csv"
                )
                attendance = attendance.drop_duplicates(["Enrollment"], keep="first")
                print(attendance)
                attendance.to_csv(fileName, index=False)
                m = "Attendance Filled Successfully of " + Subject
                self.ui.Output.setText(m)
                text_to_speech(m)
                cam.release()
                cv2.destroyAllWindows()
                cs = os.path.join(path, fileName)
                print(cs)
                with open(cs, newline="") as file:
                    reader = list(csv.reader(file))
                    WIDTH=len(reader[0])*125+100
                    HEIGHT=len(reader)*50+50
                #Attendance sheet            
                class Attendancesheet(QWidget):  
                    def __init__(self):  
                        super().__init__() 
                        self.setWindowIcon(QtGui.QIcon('icon.png'))
                        self.title = 'Attendance Sheets of '+sub  
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
                        
                        cs = os.path.join(path, fileName)
                        print(cs)
                        with open(cs, newline="") as file:
                            reader = list(csv.reader(file))
                            self.table.setColumnCount(3)
                            self.table.setColumnWidth(0, 125)
                            self.table.setColumnWidth(1, 175)
                            self.table.setColumnWidth(2, 125)
                            self.table.setHorizontalHeaderLabels(reader[0])
                            self.table.setRowCount(len(reader)-1)
                            row = 0
                            for e in reader[1:]:
                                self.table.setItem(row, 0, QTableWidgetItem(e[0]))
                                self.table.setItem(row, 1, QTableWidgetItem(str(e[1])))
                                self.table.setItem(row, 2, QTableWidgetItem(str(e[2])))
                                row += 1 
                        self.table.horizontalHeader().setStretchLastSection(True)
                        self.table.horizontalHeader().setSectionResizeMode(
                        QHeaderView.Stretch)
                self.main=Attendancesheet()
                self.main.show()
              
            except:
                f = "No Face found for attendance"
                self.ui.Output.setText(f)
                text_to_speech(f)
                cv2.destroyAllWindows()
    

def Attf(sub,self,text_to_speech):
    if sub == "":
        t = "Please enter the subject name!!!"
        self.ui.Output.setText(t)
        text_to_speech(t)
    else:
        os.startfile(f"C:\\Users\\gkara\\Desktop\\FR_AS_UI\\Attendance\\{sub}")
