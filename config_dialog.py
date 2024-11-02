from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtWidgets import (QDialog, QFormLayout, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget, QComboBox, QMessageBox)

from config_loader import load_config

import device

config = load_config()
cameras = device.getDeviceList()

class ConfigurationDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.show_config_values()
        self.load_device_list()


    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(571, 453)
        Dialog.setStyleSheet(u"background-color: rgb(61, 56, 70);")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 571, 451))
        self.frame.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(0, 0, 0);\n"
"	text-align: center;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	padding: 5px 1px\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QComboBox {\n"
"    padding: 5px;\n"
"    background-color: #FFFFFF;\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(./icons/down_arrow.png);\n"
"    width: 12px; \n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #888; \n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #5A9;\n"
"    background-color: #FFFFFF;\n"
"    color: #333;\n"
"    selection-background-color: #5A9;\n"
"    selection-color: #FFF;\n"
"}\n"
"QComboBox:editable {\n"
"    background: white;\n"
"    color: black;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 0, 131, 31))
        self.label.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255)")
        self.formLayoutWidget = QWidget(self.frame)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 40, 560, 362))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(27)
        self.formLayout.setVerticalSpacing(16)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(300, 25))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QSize(300, 25))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_3 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QSize(300, 25))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_4 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QSize(300, 25))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMinimumSize(QSize(300, 25))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_5)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_7 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setMinimumSize(QSize(300, 25))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_7)

        self.label_9 = QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_8 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setMinimumSize(QSize(300, 25))

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_10 = QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_10)

        self.lineEdit_9 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setMinimumSize(QSize(300, 25))

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_9)

        self.comboBox = QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.comboBox)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 410, 90, 37))
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setStyleSheet(u"QPushButton#pushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(0, 0, 0);  /* Optional: Adds a border */\n"
"	background-color: rgb(26, 95, 180);  /* Set your background color */\n"
"    \n"
"	font: 700 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"	background-color: rgb(38, 134, 252);\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Configuration", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Name of Database", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Database host", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Database port", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Select Camera", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Path to students details csv", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Path for exporting attendance", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Path to photos directory", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

    def show_config_values(self):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Configuration", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>You could enter the name of an existing database, or we could create a new on for you according to the name you give us, inside your database management system.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>You have to enter the username to your database management system.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>You have to enter the password to your database management system.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Enter the host name that you have used when you first installed  the database management system. By default it will be 'localhost'.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Enter the port that was selected for you when the database management system was first installed.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Select the camera that you want to use. If your device has only one, it will default to that one but if your device is connected with multiple cameras, the first one will be selected by default.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>If you plan to enter the details of your students without using the application, specify the path to that CSV file.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Type out the path to the folder you want to export the excel file. You could also create a folder at the required location and the copy its path and paste it here.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Specify the path to photos directory which the facial recognition model will use. Note: The photos directory must contain folders named after each student and must contain only that particular student's photos.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Path to photos directory", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.lineEdit.setText(config.DB_NAME)
        self.lineEdit_2.setText(config.DB_USER)
        self.lineEdit_3.setText(config.DB_PASSWORD)
        self.lineEdit_4.setText(config.DB_HOST)
        self.lineEdit_5.setText(config.DB_PORT)
        self.lineEdit_7.setText(config.STUDENTS_DETAILS_CSV)
        self.lineEdit_8.setText(config.EXPORT_PATH)
        self.lineEdit_9.setText(config.PHOTO_DATABASE)

    def load_device_list(self):
        for camera in cameras:
            self.comboBox.addItem(camera[0])

        self.comboBox.setCurrentIndex(config.CAMERA_ID)


    def save_config_values(self):
        config.DB_NAME = self.lineEdit.text()
        config.DB_USER = self.lineEdit_2.text()
        config.DB_PASSWORD = self.lineEdit_3.text()
        config.DB_HOST = self.lineEdit_4.text()
        config.DB_PORT = self.lineEdit_5.text()
        config.STUDENTS_DETAILS_CSV = self.lineEdit_7.text()
        config.EXPORT_PATH = self.lineEdit_8.text()
        config.PHOTO_DATABASE = self.lineEdit_9.text()
        config.CAMERA_ID = self.comboBox.currentIndex()

        try: 
            with open("config.py", "w") as file:
                file.write(f"DB_NAME = \"{config.DB_NAME}\"\n")
                file.write(f"DB_USER = \"{config.DB_USER}\"\n")
                file.write(f"DB_PASSWORD = \"{config.DB_PASSWORD}\"\n")
                file.write(f"DB_HOST = \"{config.DB_HOST}\"\n")
                file.write(f"DB_PORT = \"{config.DB_PORT}\"\n")
                file.write(f"STUDENTS_DETAILS_CSV = \"{config.STUDENTS_DETAILS_CSV}\"\n")
                file.write(f"EXPORT_PATH = \"{config.EXPORT_PATH}\"\n")
                file.write(f"PHOTO_DATABASE = \"{config.PHOTO_DATABASE}\"\n")
                file.write(f"CAMERA_ID = {config.CAMERA_ID}\n")
            QMessageBox.information(self, "Success", "Configuration saved successfully. Please restart the application for changes to take effect.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error saving configuration: {str(e)}")

