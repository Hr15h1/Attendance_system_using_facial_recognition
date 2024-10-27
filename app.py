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
import time
import datetime
from facial_recognition_type1 import start_camera
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt, QTimer)
from PySide6.QtGui import (QFont, QKeyEvent)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QMainWindow,
    QGridLayout, QFrame, QPushButton, QSizePolicy, QVBoxLayout, QWidget, QGraphicsScene, QLabel, QLayout, QLCDNumber)
import mysql.connector
from mysql.connector import errors
import csv
import pandas as pd
import sqlite3
from attendance_mark import mark_attendance
from attendance import ViewAttendance
from constants import STUDENTS_DETAILS_CSV
import psycopg2


# try:
#     conn = sqlite3.connect("msccsai_students.db")

#     cursor = conn.cursor()
#     query = """CREATE TABLE IF NOT EXISTS students_details (id INTEGER PRIMARY KEY AUTOINCREMENT, student_name TEXT NOT NULL, student_email TEXT NOT NULL, phone_number TEXT NOT NULL, present_address TEXT NOT NULL, permanent_address TEXT NOT NULL);"""

#     cursor.execute(query)
#     cursor.execute("SELECT COUNT(*) FROM students_details")
#     count = cursor.fetchone()[0]
#     if count > 0:
#         conn.close()
#     elif count == 0:

#         with open("students_details.csv", "r") as file:
#             contents = csv.DictReader(file)
#             students_info = [(i['student_name'], i['student_email'], i['phone_number'], i['present_address'], i['permanent_address']) for i in contents]

#         insert_query = "INSERT INTO students_details (student_name, student_email, phone_number, present_address, permanent_address) VALUES(?, ?, ?, ?, ?)"
#         cursor.executemany(insert_query, students_info)
#         conn.commit()
#     conn.close()
# except sqlite3.Error as e:
#     print(e)
#     if conn:
#         conn.close()
# Connect to existing database or create a new one and connect to it
try:
    mydb = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="admin",
        port="5432"
    )
    mydb.autocommit = True
    mycursor = mydb.cursor()
    mycursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'msccsai_students'")
    result = mycursor.fetchone()
    if not result:
        mycursor.execute("CREATE DATABASE msccsai_students")
    mycursor.close()
    mydb.close()

    mydb = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="admin",
        database="msccsai_students",
        port="5432"
    )
    mycursor = mydb.cursor()
    create_table = 'CREATE TABLE IF NOT EXISTS students_details (id SERIAL PRIMARY KEY, student_name VARCHAR(100), student_email VARCHAR(100), phone_number VARCHAR(12), present_address VARCHAR(255), permanent_address VARCHAR(255));'
    mycursor.execute(create_table)
    count = "SELECT COUNT(*) FROM students_details"
    mycursor.execute(count)
    result = mycursor.fetchone()
    if result[0] > 0:
        mydb.close()
    elif result[0] == 0 or result is None:

        csv_path = pathlib.Path.cwd() / STUDENTS_DETAILS_CSV
        dict_list = []
        with csv_path.open("r") as f:
            file_reader = csv.reader(f)
            for rows in file_reader:
                dict_list.append({'student_name': rows[0], 'student_email': rows[1], 'phone_number': rows[2], 'present_address': rows[3], 'permanent_address': rows[4]})

        for item in dict_list:
            insert_values = 'INSERT INTO students_details(student_name, student_email, phone_number, present_address, permanent_address) VALUES (%s, %s, %s, %s, %s);'
            val = item['student_name'], item['student_email'], item['phone_number'], item['present_address'], item['permanent_address']
            mycursor.execute(insert_values, val)
        mydb.commit()
except mysql.connector.Error as e:
    print(e)
finally:
    if mydb.closed:
        print("Connection closed")
    else:
        mydb.close()
        print("Connection closed")

#Function to mark attendance


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
        self.camera_view = QGraphicsView(self.centralwidget)
        self.camera_view.setObjectName(u"camera_view")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.camera_view.sizePolicy().hasHeightForWidth())
        self.camera_view.setSizePolicy(sizePolicy1)
        self.camera_view.setMinimumSize(QSize(640, 480))
        self.camera_view.setMaximumSize(QSize(640, 480))
        self.camera_view.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"background-color: rgb(154, 153, 150);")

        self.horizontalLayout.addWidget(self.camera_view)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"background-color: rgb(36, 31, 49);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(115, 50))
        self.pushButton_2.setStyleSheet(u"QPushButton#pushButton_2 {\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);  /* Optional: Adds a border */\n"
"	font-weight: bold;\n"
"	background-color: rgb(0, 117, 15);\n"
"}\n"
"QPushButton#pushButton_2:hover {\n"
"	background-color: rgb(4, 219, 32);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.pushButton_2, 0, Qt.AlignRight)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name = QLabel(self.frame)
        self.label_name.setObjectName(u"label_name")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_roll.sizePolicy().hasHeightForWidth())
        self.label_roll.setSizePolicy(sizePolicy3)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy4)
        self.lcdNumber.setMinimumSize(QSize(0, 0))
        self.lcdNumber.setMaximumSize(QSize(387, 86))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable Display"])
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy5)
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
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_roll.setText(QCoreApplication.translate("MainWindow", u"Roll No", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"MARK ATTENDANCE", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"View Attendance", None))
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
        self.s = 1
        self.attendance_marked = False
        self.setFocusPolicy(Qt.StrongFocus)

        self.pushButton.clicked.connect(self.start_camera_wrapper)
        self.pushButton_2.clicked.connect(self.view_attendance)
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
        start_camera(self.camera_view, self.label_name,self.label_roll, self)
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
        
        # elif event.key() in (Qt.Key_Enter, Qt.Key_Return):
        #     mark_attendance(self.label_name, self.label_roll.text())



        else:
            super().keyPressEvent(event)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())