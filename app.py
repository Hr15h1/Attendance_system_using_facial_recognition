import sys
import cv2
from facial_recognition_type1 import start_camera
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QKeyEvent)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QMainWindow,
    QGridLayout, QFrame, QPushButton, QSizePolicy, QVBoxLayout, QWidget, QGraphicsScene, QLabel)
# import mysql.connector
# from mysql.connector import errors
import csv
import pandas as pd
import sqlite3
from attendance_mark import mark_attendance


conn = sqlite3.connect("msccsai_students.db")

cursor = conn.cursor()
query = """CREATE TABLE IF NOT EXISTS students_details (id INTEGER PRIMARY KEY AUTOINCREMENT, student_name TEXT NOT NULL, student_email TEXT NOT NULL, phone_number TEXT NOT NULL, present_address TEXT NOT NULL, permanent_address TEXT NOT NULL);"""

cursor.execute(query)

with open("students_details.csv", "r") as file:
    contents = csv.DictReader(file)
    students_info = [(i['student_name'], i['student_email'], i['phone_number'], i['present_address'], i['permanent_address']) for i in contents]

insert_query = "INSERT INTO students_details (student_name, student_email, phone_number, present_address, permanent_address) VALUES(?, ?, ?, ?, ?)"
cursor.executemany(insert_query, students_info)
conn.commit()
conn.close()
#Connect to existing database or create a new one and connect to it
# try:
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="admin",
#         database = "msccsai_students"

# except 
#     mydb = mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="admin",
#     )
#     mycursor = mydb.cursor()
#     mycursor.execute("CREATE DATABASE msccsai_students")
#     mydb.close()
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="admin",
#         database = "msccsai_students"
#     )



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

        #Create a grid layout
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        #Create a horizontal layout
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        #Create a camera view
        self.camera_view = QGraphicsView(self.centralwidget)
        self.camera_view.setObjectName(u"camera_view")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.camera_view.sizePolicy().hasHeightForWidth())
        self.camera_view.setSizePolicy(sizePolicy1)
        self.camera_view.setMinimumSize(QSize(640, 480))
        self.camera_view.setMaximumSize(QSize(640, 480))

        #Set the style sheet for the camera view
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
        font = QFont()
        font.setPointSize(12)
        self.label_roll.setFont(font)
        self.label_roll.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"text-align: center;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.verticalLayout.addWidget(self.label_roll)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.start_button = QPushButton(self.frame)
        self.start_button.setObjectName(u"start_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy3)
        self.start_button.setMinimumSize(QSize(100, 50))
        self.start_button.setMaximumSize(QSize(100, 50))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.start_button.setFont(font1)
        self.start_button.setStyleSheet(u"QPushButton#start_button {\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);  /* Optional: Adds a border */\n"
"	background-color: rgb(0, 117, 15);\n"
"}\n"
"QPushButton#start_button:hover {\n"
"	background-color: rgb(4, 219, 32);\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.start_button)

        self.stop_button = QPushButton(self.frame)
        self.stop_button.setObjectName(u"stop_button")
        sizePolicy3.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy3)
        self.stop_button.setMinimumSize(QSize(100, 50))
        self.stop_button.setMaximumSize(QSize(100, 50))
        self.stop_button.setFont(font1)
        self.stop_button.setStyleSheet(u"QPushButton#stop_button {\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);  /* Optional: Adds a border */\n"
"	background-color: rgb(168, 22, 22);  /* Set your background color */\n"
"}\n"
"QPushButton#stop_button:hover {\n"
"	background-color: rgb(245, 32, 32);\n"
"}")

        self.verticalLayout_5.addWidget(self.stop_button)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        self.pushButton.setMinimumSize(QSize(150, 50))
        self.pushButton.setMaximumSize(QSize(150, 50))
        self.pushButton.setFont(font1)

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


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_roll.setText(QCoreApplication.translate("MainWindow", u"Roll No", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"MARK ATTENDANCE", None))
    # retranslateUi


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Buttons for starting and stopping the camera
        self.start_button.clicked.connect(self.start_camera_wrapper)
        self.stop_button.clicked.connect(self.stop_camera_wrapper)  # Connect stop button
        self.pushButton.clicked.connect(lambda: mark_attendance(self.label_name, self.label_roll.text()))

        self.cap = None  # Video capture object
        self.alive = False
        self.scene = QGraphicsScene()
        self.camera_view.setScene(self.scene)
        self.source = None
        self.s = 1

        self.setFocusPolicy(Qt.StrongFocus)

    # Wrapper functions for starting and stopping the camera
    def start_camera_wrapper(self):
        self.alive = True
        self.source = cv2.VideoCapture(self.s)
        start_camera(self.camera_view, self.label_name,self.label_roll, self)
    def stop_camera_wrapper(self):
        self.alive = False  # Set the flag to False to stop the camera
        self.scene.clear()
        if self.source is not None:
            self.source.release()


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
        
        elif event.key() in (Qt.Key_Enter, Qt.Key_Return):
            mark_attendance(self.label_name, self.label_roll.text())



        else:
            super().keyPressEvent(event)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())