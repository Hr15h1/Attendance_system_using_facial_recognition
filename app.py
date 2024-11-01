"""
This module implements an attendance system using facial recognition. It utilizes PySide6 for the GUI, OpenCV for camera operations, 
and SQLite for database management. The application allows users to start and stop the camera, mark attendance, and view attendance records.
Classes:
    Ui_MainWindow: Sets up the main window UI components.
    MainWindow: Inherits from QMainWindow and Ui_MainWindow, handles the main application logic.
Functions:
    setupUi(self, MainWindow): Sets up the UI components for the main window.
    retranslateUi(self, MainWindow): Sets the text for the UI components.
    start_camera_wrapper(self): Wrapper function to start the camera.
    stop_camera_wrapper(self): Wrapper function to stop the camera.
    view_attendance(self): Opens a new window to view attendance records.
    closeEvent(self, event): Overrides the close event to release the camera.
    keyPressEvent(self, event): Overrides the key press event to handle specific key presses.
Attributes:
    conn: SQLite connection object.
    cursor: SQLite cursor object.
    query: SQL query string to create the students_details table.
    count: Number of records in the students_details table.
    students_info: List of student details read from the CSV file.
    insert_query: SQL query string to insert student details into the students_details table.
    cap: Video capture object.
    alive: Boolean flag to indicate if the camera is running.
    scene: QGraphicsScene object for displaying the camera feed.
    source: Video source for the camera.
    s: Integer representing the camera source index.
"""

import pathlib
import sys
import cv2
import datetime
from facial_recognition_type1 import start_camera
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt, QTimer)
from PySide6.QtGui import (QFont, QKeyEvent)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QMainWindow,
    QGridLayout, QFrame, QPushButton, QSizePolicy, QVBoxLayout, QWidget, QGraphicsScene, QLabel, QLayout, QLCDNumber)
from config_dialog import ConfigurationDialog
import csv
import ctypes
from attendance_mark import mark_attendance
from config_loader import load_config
from attendance import ViewAttendance
from student_registration import AddStudent
import psycopg2

config = load_config()

# Connect to existing database or create a new one and connect to it
try:
    # Create a new database if it does not exist
    mydb = psycopg2.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        port=config.DB_PORT
    )
    # Enable autocommit to create the database
    mydb.autocommit = True
    mycursor = mydb.cursor()
    # Check if the database exists
    mycursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'msccsai_students'")
    result = mycursor.fetchone()
    # Create the database if it does not exist
    if not result:
        mycursor.execute("CREATE DATABASE msccsai_students")
    mycursor.close()
    mydb.close()
    # Connect to the created database
    mydb = psycopg2.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME,
        port=config.DB_PORT
    )
    mycursor = mydb.cursor()
    # Create the students_details table if it does not exist
    create_table = 'CREATE TABLE IF NOT EXISTS students_details (id SERIAL PRIMARY KEY, student_name VARCHAR(100), student_email VARCHAR(100), phone_number VARCHAR(12), present_address VARCHAR(255), permanent_address VARCHAR(255));'
    mycursor.execute(create_table)
    count = "SELECT COUNT(*) FROM students_details"
    mycursor.execute(count)
    result = mycursor.fetchone()
    if result[0] > 0:
        mydb.close()
    elif result[0] == 0 or result is None:
        # Insert student details from the CSV file into the students_details table
        csv_path = pathlib.Path.cwd() / config.STUDENTS_DETAILS_CSV
        if csv_path.stat().st_size == 0:
            print("CSV file is empty")
            ctypes.windll.user32.MessageBoxW(0, "The CSV file is empty or does not exist. You can add student details through the application.", "CSV File Empty", 0)
        else:
            dict_list = []
            with csv_path.open("r") as f:
                file_reader = csv.reader(f)
                for rows in file_reader:
                    dict_list.append({'student_name': rows[0], 'student_email': rows[1], 'phone_number': rows[2], 'present_address': rows[3], 'permanent_address': rows[4]})
            if not dict_list:
                ctypes.windll.user32.MessageBoxW(0, "The CSV file is empty or does not exist. You can add student details through the application.", "CSV File Empty", 0)
                
            else:
                for item in dict_list:
                    insert_values = 'INSERT INTO students_details(student_name, student_email, phone_number, present_address, permanent_address) VALUES (%s, %s, %s, %s, %s);'
                    val = item['student_name'], item['student_email'], item['phone_number'], item['present_address'], item['permanent_address']
                    mycursor.execute(insert_values, val)
                mydb.commit()
                ctypes.windll.user32.MessageBoxW(0, "The student details from the csv file has been added successfully", "Student Details Added", 0)
except psycopg2.Error as e:
    print(e)
finally:
    if mydb.closed:
        print("Connection closed")
    else:
        mydb.close()
        print("Connection closed")

#Function to mark attendance

#Main window UI setup
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1075, 647)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(61, 56, 70);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, 5, -1)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setMinimumSize(QSize(104, 40))
        self.pushButton_4.setStyleSheet(u"QPushButton#pushButton_4 {\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);  /* Optional: Adds a border */\n"
"	background-color: rgb(255, 94, 94);\n"
"	\n"
"	font: 700 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton#pushButton_4:hover {\n"
"	background-color: rgb(4, 219, 32);\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_4)

        self.camera_view = QGraphicsView(self.centralwidget)
        self.camera_view.setObjectName(u"camera_view")
        sizePolicy1.setHeightForWidth(self.camera_view.sizePolicy().hasHeightForWidth())
        self.camera_view.setSizePolicy(sizePolicy1)
        self.camera_view.setMinimumSize(QSize(640, 480))
        self.camera_view.setMaximumSize(QSize(640, 480))
        self.camera_view.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"background-color: rgb(154, 153, 150);")

        self.verticalLayout_8.addWidget(self.camera_view)


        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(386, 594))
        self.frame.setStyleSheet(u"background-color: rgb(36, 31, 49);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(100, 50))
        self.pushButton_2.setStyleSheet(u"QPushButton#pushButton_2 {\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);  /* Optional: Adds a border */\n"
"	background-color: rgb(0, 117, 15);\n"
"}\n"
"QPushButton#pushButton_2:hover {\n"
"	background-color: rgb(4, 219, 32);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.pushButton_2, 0, Qt.AlignRight)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setMinimumSize(QSize(100, 50))
        self.pushButton_3.setStyleSheet(u"QPushButton#pushButton_3 {\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);  /* Optional: Adds a border */\n"
"	background-color: rgb(255, 145, 135);\n"
"	\n"
"	font: 900 9pt \"Segoe UI\";\n"
"}\n"
"QPushButton#pushButton_3:hover {\n"
"	background-color: rgb(255, 103, 103)\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed {\n"
"	background-color: rgb(255, 32, 32)\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.pushButton_3, 0, Qt.AlignRight)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name = QLabel(self.frame)
        self.label_name.setObjectName(u"label_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy2)
        self.label_name.setMinimumSize(QSize(0, 0))
        self.label_name.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(12)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"text-align: center;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")

        self.verticalLayout.addWidget(self.label_name)

        self.label_roll = QLabel(self.frame)
        self.label_roll.setObjectName(u"label_roll")
        sizePolicy2.setHeightForWidth(self.label_roll.sizePolicy().hasHeightForWidth())
        self.label_roll.setSizePolicy(sizePolicy2)
        self.label_roll.setMinimumSize(QSize(0, 0))
        self.label_roll.setMaximumSize(QSize(16777215, 50))
        self.label_roll.setFont(font)
        self.label_roll.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"text-align: center;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")

        self.verticalLayout.addWidget(self.label_roll)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(30)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.lcdNumber = QLCDNumber(self.frame)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy3)
        self.lcdNumber.setMinimumSize(QSize(0, 0))
        self.lcdNumber.setMaximumSize(QSize(387, 86))
        font1 = QFont()
        font1.setFamilies([u"Courier New"])
        font1.setBold(True)
        self.lcdNumber.setFont(font1)
        self.lcdNumber.setLayoutDirection(Qt.LeftToRight)
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	background-color: black;\n"
"	color: #f8f8ff;  \n"
"	font-family: 'Courier New';  \n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"	font-size: 24px;\n"
"	font-weight: bold;  \n"
"}")
        self.lcdNumber.setFrameShape(QFrame.WinPanel)
        self.lcdNumber.setFrameShadow(QFrame.Raised)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(4)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 0.000000000000000)
        self.lcdNumber.setProperty("intValue", 0)

        self.verticalLayout_5.addWidget(self.lcdNumber)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy4)
        self.pushButton.setMinimumSize(QSize(150, 50))
        self.pushButton.setMaximumSize(QSize(150, 50))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton#pushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);  /* Optional: Adds a border */\n"
"	background-color: rgb(26, 95, 180);  /* Set your background color */\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"	background-color: rgb(38, 134, 252);\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)


        self.horizontalLayout.addWidget(self.frame)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)



        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_roll.setText(QCoreApplication.translate("MainWindow", u"Roll No", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"MARK ATTENDANCE", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"View Attendance", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Add student", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Edit Config", None))
    # retranslateUi


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Buttons for starting and stopping the camera

        self.cap = None  # Video capture object
        self.alive = False
        self.scene = QGraphicsScene()
        self.camera_view.setScene(self.scene)
        self.source = None
        self.s = config.CAMERA_ID
        self.attendance_marked = False
        self.setFocusPolicy(Qt.StrongFocus)

        self.pushButton.clicked.connect(self.start_camera_wrapper)
        self.pushButton_2.clicked.connect(self.view_attendance)
        self.pushButton_3.clicked.connect(self.add_student)
        self.pushButton_4.clicked.connect(self.open_config_dialog)

        # Wrapper functions for starting and stopping the camera

    def countdown(self, s):
 
        self.total_seconds = s
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_lcd)
        self.timer.start(1000)

    def update_lcd(self):
        if self.total_seconds > 0:
            timer = datetime.timedelta(seconds=self.total_seconds)
            self.lcdNumber.display(str(timer))
            self.total_seconds -= 1
        else:
            self.timer.stop()
            self.lcdNumber.display("0")
            if not self.attendance_marked:

                mark_attendance(self.label_name, self.label_roll.text())
                self.attendance_marked = True
            self.total_seconds = 0
            self.stop_camera_wrapper()


    def start_camera_wrapper(self):
        self.alive = True
        self.source = cv2.VideoCapture(self.s)
        start_camera(self.camera_view, self, "mark_attendance", self.label_name ,self.label_roll)
        self.attendance_marked = False


    def stop_camera_wrapper(self):
        self.alive = False  # Set the flag to False to stop the camera
        self.scene.clear()
        self.camera_view.setScene(self.scene)
        if self.source is not None:
            self.source.release()


    def view_attendance(self):
        self.window2 = QMainWindow()
        self.ui = ViewAttendance()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def add_student(self):
        self.window3 = QMainWindow()
        self.ui = AddStudent()
        self.ui.setupUi(self.window3)
        self.window3.show()


    # Override the closeEvent method to release the camera

    def closeEvent(self, event):
        self.alive = False
        if self.cap:
            self.cap.release()
        super().closeEvent(event)


    # Override the keyPressEvent method to close the window when the escape key is pressed
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()
        else:
            super().keyPressEvent(event)


    def open_config_dialog(self):
        print("open config function called.")
        self.dialog1 = ConfigurationDialog(self.centralwidget)
        self.dialog1.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())