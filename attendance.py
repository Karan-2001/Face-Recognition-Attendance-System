import sys
import pyttsx3
import show_attendance
import takeImage
import trainImage
import automaticAttedance
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt,QDateTime
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from splashscreen import Ui_splashscreen
from registerscreen import Ui_Registerscreen
from mainscreen import Ui_Mainscreen
from attendance_screen import Ui_attendance_screen
from viewscreen import Ui_viewscreen

# Text to Speech
def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

#path
haarcasecade_path ="C:\\Users\\gkara\\Desktop\\FR_AS_UI\\haarcascade_frontalface_default.xml"
trainimagelabel_path = ("C:\\Users\\gkara\\Desktop\\FR_AS_UI\\TrainingImageLabel\\Trainner.yml")
trainimage_path = "C:\\Users\\gkara\\Desktop\\FR_AS_UI\\TrainingImage"
studentdetail_path = ("C:\\Users\\gkara\\Desktop\\FR_AS_UI\\StudentDetails\\studentdetails.csv")
attendance_path = "C:\\Users\\gkara\\Desktop\\FR_AS_UI\\Attendance"

counter=0

# Student Attendance view Screen
class Viewscreen(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_viewscreen()
		self.ui.setupUi(self)
		self.setWindowTitle("View Attendance")
		self.setWindowIcon(QtGui.QIcon('icon.png'))
		self.ui.View_attendance.clicked.connect(self.view_attendance_clicked)
		self.ui.chech_sheets.clicked.connect(self.check_sheets_clicked)

	def view_attendance_clicked(self):
		self.ui.Output.setText("")
		subject_name=self.ui.sub_name_input.text()
		show_attendance.calculate_attendance(subject_name,self,text_to_speech)

	def check_sheets_clicked(self):
		subject_name=self.ui.sub_name_input.text()
		show_attendance.Att_sheets(subject_name,self,text_to_speech)

#Student Attendance Screen
class Attendancescreen(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_attendance_screen()
		self.ui.setupUi(self)
		self.setWindowTitle("Attendance")
		self.setWindowIcon(QtGui.QIcon('icon.png'))
		self.ui.Fill_attendance.clicked.connect(self.fill_attendance_clicked)
		self.ui.chech_sheets.clicked.connect(self.check_sheets_clicked)

	def fill_attendance_clicked(self):
		self.ui.Output.setText("")
		subject_name=self.ui.sub_name_input.text()
		automaticAttedance.FillAttendance(subject_name,self,text_to_speech)

	def check_sheets_clicked(self):
		subject_name=self.ui.sub_name_input.text()
		automaticAttedance.Attf(subject_name,self,text_to_speech)

# Student Registration Screen
class Registerscreen(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Registerscreen()
		self.ui.setupUi(self)
		self.setWindowTitle("Register New Student")
		self.setWindowIcon(QtGui.QIcon('icon.png'))
		self.ui.Take_image.clicked.connect(self.Take_images_clicked)
		self.ui.Train_image.clicked.connect(self.Train_images_clicked)

	def Take_images_clicked(self):
		self.ui.Output.setText("")
		number=self.ui.number_input.text()
		name=self.ui.name_input.text()
		takeImage.TakeImage(number,name,haarcasecade_path,trainimage_path,self,text_to_speech)

	def Train_images_clicked(self):
		trainImage.TrainImage(haarcasecade_path,trainimage_path,trainimagelabel_path,self,text_to_speech)

# For adding clicklable event to Qlable
def clickable(widget):
    class Filter(QObject):
            clicked = pyqtSignal()
            def eventFilter(self, obj, event):
               if obj == widget:
                   if event.type() == QEvent.MouseButtonRelease:
                       if obj.rect().contains(event.pos()):
                           self.clicked.emit()
                           return True
               return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

# Main Screen    
class Mainscreen(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Mainscreen()
		self.ui.setupUi(self)
		timer = QTimer(self)
		timer.timeout.connect(self.showTime)
		timer.start(1000)
		self.setWindowIcon(QtGui.QIcon('icon.png'))
		self.setWindowTitle("Face Recognition Attendance System")
		clickable(self.ui.about).connect(self.about_clicked)
		self.ui.Register.clicked.connect(self.Register_clicked)
		self.ui.Take_attendance.clicked.connect(self.Take_attendance_clicked)
		self.ui.view_attendance.clicked.connect(self.view_attendance_clicked)
	
	def about_clicked(self):
		print("about clicked")

	def showTime(self):
		current_time = QTime.currentTime()
		current_date = QDate.currentDate()
		date=current_date.toString(Qt.DefaultLocaleLongDate)
		datetime = QDateTime.currentDateTime()
		day=datetime.toString()[:3]
		hrs=current_time.toString(Qt.DefaultLocaleLongDate)[-2:]
		label_time = current_time.toString('hh:mm:ss')
		self.ui.Time.setText(day+"   "+label_time+" "+hrs)
		self.ui.date.setText(date)

	def Register_clicked(self):
		self.main=Registerscreen()
		self.main.show()
        
	def Take_attendance_clicked(self):
		self.main=Attendancescreen()
		self.main.show()

	def view_attendance_clicked(self):
		self.main=Viewscreen()
		self.main.show()

# Splash Screen
class Splashscreen(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_splashscreen()
		self.ui.setupUi(self)
		self.timer=QtCore.QTimer()
		self.timer.timeout.connect(self.progress)
		self.timer.start(25)
		self.gif()
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.shadow=QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(20)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0,0,0,60))
		self.ui.BG.setGraphicsEffect(self.shadow)
        
	def gif(self):
		self.ui.movie = QtGui.QMovie("C:/Users/gkara/Desktop/FR_AS_UI/ezgif.com-gif-maker.gif")
		self.ui.gif.setMovie(self.ui.movie)
		self.ui.movie.start()

	def progress(self):
		global counter
		self.ui.progressBar.setValue(counter)
		if counter>100:
			self.timer.stop()
			self.main = Mainscreen()
			self.main.show()
			self.close()
		counter+=1

app=QApplication(sys.argv)
attendance=Splashscreen()
attendance.show()
sys.exit(app.exec_())







