import sys
from facial_recognition_type1 import start_camera, stop_camera
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QKeyEvent)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QMainWindow,
    QPlainTextEdit,QGridLayout, QFrame, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget, QGraphicsScene, QLabel)


class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         if not MainWindow.objectName():
#             MainWindow.setObjectName(u"MainWindow")
#         MainWindow.resize(1082, 720)
#         sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
#         MainWindow.setSizePolicy(sizePolicy)
#         MainWindow.setMinimumSize(QSize(1063, 720))
#         MainWindow.setMaximumSize(QSize(16777215, 16777215))
#         self.centralwidget = QWidget(MainWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
#         self.horizontalLayoutWidget = QWidget(self.centralwidget)
#         self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
#         self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1081, 691))
#         self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget)
#         self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
#         self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_5 = QVBoxLayout()
#         self.verticalLayout_5.setObjectName(u"verticalLayout_5")
#         self.cameraView = QGraphicsView(self.horizontalLayoutWidget)
#         self.cameraView.setObjectName(u"cameraView")
#         sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#         sizePolicy1.setHorizontalStretch(0)
#         sizePolicy1.setVerticalStretch(0)
#         sizePolicy1.setHeightForWidth(self.cameraView.sizePolicy().hasHeightForWidth())
#         self.cameraView.setSizePolicy(sizePolicy1)
#         self.cameraView.setMinimumSize(QSize(640, 480))
#         self.cameraView.setMaximumSize(QSize(640, 480))
#         self.cameraView.setStyleSheet(u"QGraphicsView#cameraView{\n"
# "		\n"
# "	border-color: rgb(131, 131, 131);\n"
# "   background-color: rgb(172, 172, 172);\n"
# "}")

#         self.verticalLayout_5.addWidget(self.cameraView)

#         self.horizontalLayout_6 = QHBoxLayout()
#         self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
#         self.startButton = QPushButton(self.horizontalLayoutWidget)
#         self.startButton.setObjectName(u"startButton")
#         self.startButton.setMinimumSize(QSize(210, 59))
#         self.startButton.setMaximumSize(QSize(210, 59))
#         font = QFont()
#         font.setPointSize(12)
#         self.startButton.setFont(font)
#         self.startButton.setStyleSheet(u"QPushButton#startButton{\n"
# "		\n"
# "	border-radius: 10px;\n"
# "	border-color: rgb(0, 0, 0);\n"
# "	color: rgb(0, 0, 0);\n"
# "	background-color: rgb(203, 254, 197);\n"
# "\n"
# "}\n"
# "QPushButton#startButton:hover {	\n"
# "	background-color: rgb(148, 255, 135);\n"
# "}")
#         icon = QIcon()
#         icon.addFile(u"icons/formkit--start (1).png", QSize(), QIcon.Normal, QIcon.Off)
#         self.startButton.setIcon(icon)
#         self.startButton.setIconSize(QSize(25, 25))

#         self.horizontalLayout_6.addWidget(self.startButton)

#         self.stopButton = QPushButton(self.horizontalLayoutWidget)
#         self.stopButton.setObjectName(u"stopButton")
#         self.stopButton.setMinimumSize(QSize(210, 59))
#         self.stopButton.setMaximumSize(QSize(210, 59))
#         self.stopButton.setFont(font)
#         self.stopButton.setAutoFillBackground(False)
#         self.stopButton.setStyleSheet(u"QPushButton#stopButton{\n"
# "		\n"
# "	border-radius: 10px;\n"
# "	border-color: rgb(0, 0, 0);\n"
# "	color: rgb(0, 0, 0);\n"
# "	background-color: rgb(253, 201, 201);\n"
# "\n"
# "}\n"
# "QPushButton#stopButton:hover {	\n"
# "	background-color: rgb(255, 145, 145);\n"
# "}")
#         icon1 = QIcon()
#         icon1.addFile(u"icons/material-symbols--stop.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.stopButton.setIcon(icon1)
#         self.stopButton.setIconSize(QSize(30, 30))

#         self.horizontalLayout_6.addWidget(self.stopButton)


#         self.verticalLayout_5.addLayout(self.horizontalLayout_6)


#         self.horizontalLayout_5.addLayout(self.verticalLayout_5)

#         self.verticalLayout_3 = QVBoxLayout()
#         self.verticalLayout_3.setSpacing(0)
#         self.verticalLayout_3.setObjectName(u"verticalLayout_3")
#         self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
#         # self.plainTextEdit = QPlainTextEdit(self.horizontalLayoutWidget)
#         # self.plainTextEdit.setObjectName(u"plainTextEdit")
#         # sizePolicy1.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
#         self.label = QLabel(self.horizontalLayoutWidget)
#         self.label.setObjectName(u"label")
#         sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
#         self.label.setSizePolicy(sizePolicy1)
#         self.label.setMinimumSize(QSize(429, 60))
#         self.label.setMaximumSize(QSize(429, 60))
#         font1 = QFont()
#         font1.setFamilies([u"Bell MT"])
#         font1.setPointSize(24)
#         font1.setBold(True)
#         self.label.setFont(font1)


#         self.verticalLayout_3.addWidget(self.label)

#         self.plainTextEdit_2 = QPlainTextEdit(self.horizontalLayoutWidget)
#         self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
#         sizePolicy1.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
#         self.plainTextEdit_2.setSizePolicy(sizePolicy1)
#         self.plainTextEdit_2.setMinimumSize(QSize(429, 66))
#         self.plainTextEdit_2.setMaximumSize(QSize(429, 66))
#         self.plainTextEdit_2.setStyleSheet(u"QPlainTextEdit#plainTextEdit_2{\n"
# "		\n"
# "	border-color: rgb(131, 131, 131);\n"
# "	font: 700 24pt \"Segoe UI\";\n"
# "	color: rgb(255, 255, 255);\n"
# "\n"
# "}")

#         self.verticalLayout_3.addWidget(self.plainTextEdit_2)


#         self.horizontalLayout_5.addLayout(self.verticalLayout_3)

#         MainWindow.setCentralWidget(self.centralwidget)
#         # self.statusbar = QStatusBar(MainWindow)
#         # self.statusbar.setObjectName(u"statusbar")
#         # MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)

#         QMetaObject.connectSlotsByName(MainWindow)
#     # setupUi

#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#         self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start Camera", None))
#         self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop Camera", None))
#     # retranslateUi

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

        self.cap = None  # Video capture object
        self.alive = False
        self.scene = QGraphicsScene()
        self.camera_view.setScene(self.scene)

        self.setFocusPolicy(Qt.StrongFocus)

    def start_camera_wrapper(self):
        self.alive = True

        start_camera(self.camera_view, self.label_name,self.label_roll, self)
    def stop_camera_wrapper(self):
        self.alive = False  # Set the flag to False to stop the camera
        self.scene.clear()
        stop_camera()


    def closeEvent(self, event):
        self.alive = False
        if self.cap:
            self.cap.release()
        super().closeEvent(event)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()
        
        elif event.key() in (Qt.Key_Enter, Qt.Key_Return):
            print(f"Name is : {self.label_name.text()} and roll no is {self.label_roll.text()}")

            #Add logic to mark attendance to the database here


        else:
            super().keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())