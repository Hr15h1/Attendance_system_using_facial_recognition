from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QRect,
    QSize, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QGraphicsView, QHBoxLayout, QSpinBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget, QMessageBox)
from facial_recognition_type1 import start_camera
import cv2
import psycopg2
from config_loader import load_config

config = load_config()

class AddStudent(QObject):
    



    def setupUi(self, MainWindow):
        self.alive = False
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1886, 816)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(61, 56, 70);\n"
    "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1886, 811))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, 0, -1)
        self.graphicsView = QGraphicsView(self.horizontalLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QSize(1280, 720))
        self.graphicsView.setMaximumSize(QSize(1280, 720))
        self.graphicsView.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
    "border: 2px solid rgb(255, 255, 255);\n"
    "background-color: rgb(154, 153, 150);\n"
    "border-radius: 7px;")

        self.verticalLayout.addWidget(self.graphicsView)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(190, 42))
        self.pushButton.setMaximumSize(QSize(190, 42))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"QPushButton#pushButton {\n"
    "	color: rgb(255, 255, 255);\n"
    "	border-radius: 5px;\n"
    "	border: 1px solid rgb(0, 0, 0);  /* Optional: Adds a border */\n"
    "	background-color: rgb(26, 95, 180);  /* Set your background color */\n"
    "}\n"
    "\n"
    "QPushButton#pushButton:hover {\n"
    "	background-color: rgb(38, 134, 252);\n"
    "}\n"
    "")

        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.take_photo)
        self.spinBox = QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(70, 16777215))
        self.spinBox.setStyleSheet(u"QSpinBox {\n"
"    background-color: #f0f0f0; /* Light grey background */\n"
"    color: #333333; /* Dark text */\n"
"    border: 1px solid #a6a6a6; /* Grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	border-top-right-radius: 5px;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; /* Position the up button */\n"
"    width: 15px;\n"
"    border-left: 1px solid #a6a6a6;\n"
"    background-color: #e1e1e1;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	border-bottom-right-radius: 5px;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; /* Position the down button */\n"
"    width: 15px;\n"
"    border-left: 1px solid #a6a6a6;\n"
"    background-color: #e1e1e1;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(./icons/up_arrow.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow  {\n"
"    image: url(./icons/down_arrow.png);\n"
"    width: 7px;\n"
"    he"
                        "ight: 7px;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.spinBox)

        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.widget = QWidget(self.horizontalLayoutWidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(580, 797))
        self.widget.setMaximumSize(QSize(77, 78))
        self.widget.setStyleSheet(u"border-radius: 10px;\n"
    "background-color: rgb(36, 31, 49);\n"
    "\n"
    "\n"
    "\n"
    "")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(217, 10, 150, 20))
        self.label.setStyleSheet(u"color: white;\n"
    "font: 900 15pt \"Segoe UI Black\";\n"
    "")
        self.verticalLayoutWidget_3 = QWidget(self.widget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 40, 561, 751))
        self.formLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.row_1 = QHBoxLayout()
        self.row_1.setObjectName(u"row_1")
        self.cell_1 = QVBoxLayout()
        self.cell_1.setSpacing(20)
        self.cell_1.setObjectName(u"cell_1")
        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"font: 900 14pt \"Segoe UI Black\";\n"
    "color: rgb(255, 255, 255)")

        self.cell_1.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QSize(274, 50))
        self.lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
    "text-align: center;\n"
    "background-color: rgb(255, 255, 255);\n"
    "border-radius: 10px;\n"
    "font: 12pt \"Segoe UI\";\n"
    "")
        self.lineEdit.setClearButtonEnabled(True)

        self.cell_1.addWidget(self.lineEdit)


        self.row_1.addLayout(self.cell_1)

        self.cell_2 = QVBoxLayout()
        self.cell_2.setSpacing(20)
        self.cell_2.setObjectName(u"cell_2")
        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet(u"font: 900 14pt \"Segoe UI Black\";\n"
    "color: rgb(255, 255, 255)")

        self.cell_2.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMaximumSize(QSize(274, 50))
        self.lineEdit_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
    "text-align: center;\n"
    "background-color: rgb(255, 255, 255);\n"
    "border-radius: 10px;\n"
    "font: 12pt \"Segoe UI\";\n"
    "")
        self.lineEdit_3.setClearButtonEnabled(True)

        self.cell_2.addWidget(self.lineEdit_3)


        self.row_1.addLayout(self.cell_2)


        self.formLayout.addLayout(self.row_1)

        self.row_2 = QHBoxLayout()
        self.row_2.setObjectName(u"row_2")
        self.cell_3 = QVBoxLayout()
        self.cell_3.setSpacing(20)
        self.cell_3.setObjectName(u"cell_3")
        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet(u"font: 900 14pt \"Segoe UI Black\";\n"
    "color: rgb(255, 255, 255)")

        self.cell_3.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMaximumSize(QSize(274, 50))
        self.lineEdit_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
    "text-align: center;\n"
    "background-color: rgb(255, 255, 255);\n"
    "border-radius: 10px;\n"
    "font: 12pt \"Segoe UI\";\n"
    "")
        self.lineEdit_4.setClearButtonEnabled(True)

        self.cell_3.addWidget(self.lineEdit_4)


        self.row_2.addLayout(self.cell_3)

        self.cell_4 = QVBoxLayout()
        self.cell_4.setSpacing(20)
        self.cell_4.setObjectName(u"cell_4")
        self.label_6 = QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet(u"font: 900 14pt \"Segoe UI Black\";\n"
    "color: rgb(255, 255, 255)")

        self.cell_4.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMaximumSize(QSize(274, 50))
        self.lineEdit_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
    "text-align: center;\n"
    "background-color: rgb(255, 255, 255);\n"
    "border-radius: 10px;\n"
    "font: 12pt \"Segoe UI\";\n"
    "")
        self.lineEdit_5.setClearButtonEnabled(True)

        self.cell_4.addWidget(self.lineEdit_5)


        self.row_2.addLayout(self.cell_4)


        self.formLayout.addLayout(self.row_2)

        self.row_3 = QHBoxLayout()
        self.row_3.setObjectName(u"row_3")
        self.cell_5 = QVBoxLayout()
        self.cell_5.setSpacing(20)
        self.cell_5.setObjectName(u"cell_5")
        self.label_7 = QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet(u"font: 900 14pt \"Segoe UI Black\";\n"
    "color: rgb(255, 255, 255)")

        self.cell_5.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setMaximumSize(QSize(274, 50))
        self.lineEdit_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
    "text-align: center;\n"
    "background-color: rgb(255, 255, 255);\n"
    "border-radius: 10px;\n"
    "font: 12pt \"Segoe UI\";\n"
    "")
        self.lineEdit_6.setClearButtonEnabled(True)

        self.cell_5.addWidget(self.lineEdit_6)


        self.row_3.addLayout(self.cell_5)

        self.cell_6 = QVBoxLayout()
        self.cell_6.setSpacing(20)
        self.cell_6.setObjectName(u"cell_6")
        self.label_8 = QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet(u"font: 900 14pt \"Segoe UI Black\";\n"
    "color: rgb(255, 255, 255)")

        self.cell_6.addWidget(self.label_8)

        self.lineEdit_7 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setMaximumSize(QSize(274, 50))
        self.lineEdit_7.setStyleSheet(u"color: rgb(0, 0, 0);\n"
    "text-align: center;\n"
    "background-color: rgb(255, 255, 255);\n"
    "border-radius: 10px;\n"
    "font: 12pt \"Segoe UI\";\n"
    "")
        self.lineEdit_7.setClearButtonEnabled(True)

        self.cell_6.addWidget(self.lineEdit_7)


        self.row_3.addLayout(self.cell_6)


        self.formLayout.addLayout(self.row_3)

        self.cell_8 = QVBoxLayout()
        self.cell_8.setSpacing(20)
        self.cell_8.setObjectName(u"cell_8")
        self.label_10 = QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet(u"font: 900 14pt \"Segoe UI Black\";\n"
    "color: rgb(255, 255, 255)")

        self.cell_8.addWidget(self.label_10)

        self.lineEdit_9 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setMaximumSize(QSize(317, 50))
        self.lineEdit_9.setStyleSheet(u"color: rgb(0, 0, 0);\n"
    "text-align: center;\n"
    "background-color: rgb(255, 255, 255);\n"
    "border-radius: 10px;\n"
    "font: 12pt \"Segoe UI\";\n"
    "")
        self.lineEdit_9.setClearButtonEnabled(True)

        self.cell_8.addWidget(self.lineEdit_9)


        self.formLayout.addLayout(self.cell_8)


        self.verticalLayout_2.addWidget(self.widget, 0, Qt.AlignTop)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)



    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save details and take photo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Student Details", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Register Number", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Register Number", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Roll Number", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Roll No", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Present Address", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Present Address", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Permanent Address", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Permanent Address", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
    # retranslateUi

    def take_photo(self):
        if not self.lineEdit_4.text().strip():
            return
        self.c = config.CAMERA_ID
        self.alive = True
        self.source = cv2.VideoCapture(self.c)
        flag = start_camera(self.graphicsView, self, "add_student")
        if flag:
            student_details = {"register_number": self.lineEdit.text(), "roll_number": self.lineEdit_3.text(), "name": self.lineEdit_4.text(), "phone_number": self.lineEdit_5.text(), "present_address": self.lineEdit_6.text(), "permanent_address": self.lineEdit_7.text(), "email": self.lineEdit_9.text()}

            try:
                mydb = psycopg2.connect(
                    host=config.DB_HOST,
                    user=config.DB_USER,
                    password=config.DB_PASSWORD,
                    database=config.DB_NAME,
                    port = config.DB_PORT
                )

                query = "INSERT INTO students_details (student_name, student_email, phone_number, present_address, permanent_address) VALUES (%s, %s, %s, %s, %s)"

                values = (student_details["name"], student_details["email"], student_details["phone_number"], student_details["present_address"], student_details["permanent_address"])

                cursor = mydb.cursor()

                cursor.execute(query, values)

                mydb.commit()

                QMessageBox.information(self.centralwidget, "success", "Student details saved successfully")

            except psycopg2.Error as e:
                mydb.rollback()
                QMessageBox.critical(self.centralwidget, "Database Error", f"An error occurred while saving student details: {e}")

            finally:
                cursor.close()
                mydb.close()