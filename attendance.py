from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QTableView, QMessageBox)
from PySide6.QtSql import QSqlDatabase, QSqlTableModel

class viewAttendance(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"View Attendance")
        MainWindow.resize(612, 546)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"                background-color: #2F2F2F;  /* Dark gray background */\n"
"            }\n"
"            \n"
"            QWidget {\n"
"                color: #FFFFFF;              /* White text */\n"
"                background-color: #2F2F2F;  /* Dark gray background */\n"
"            }\n"
"\n"
"            QComboBox {\n"
"                background-color: #3E3E3E;  /* Slightly lighter gray for combo box */\n"
"                color: #FFFFFF;              /* White text in combo box */\n"
"                border: 1px solid #555555;   /* Gray border */\n"
"            }\n"
"\n"
"            QComboBox QAbstractItemView {\n"
"                background-color: #4D4D4D;  /* Even lighter gray for dropdown items */\n"
"                color: #FFFFFF;              /* White text for items */\n"
"                selection-background-color: #555555; /* Highlight selection */\n"
"            }\n"
"\n"
"            QComboBox:hover {\n"
"                border: 1px solid #888888;   /* Border color when h"
                        "overed */\n"
"            }\n"
"\n"
"            QPushButton {\n"
"                background-color: #3E3E3E;  /* Button background */\n"
"                color: #FFFFFF;              /* Button text */\n"
"                border: 1px solid #555555;   /* Button border */\n"
"                padding: 5px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #4D4D4D;  /* Button hover state */\n"
"            }\n"
"\n"
"            QLineEdit {\n"
"                background-color: #4D4D4D;  /* Input field background */\n"
"                color: #FFFFFF;              /* Input text */\n"
"                border: 1px solid #555555;   /* Border for input fields */\n"
"            }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.year_dropdown = QComboBox(self.centralwidget)
        self.year_dropdown.addItem("")
        self.year_dropdown.setObjectName(u"year_dropdown")
        self.year_dropdown.setMaximumSize(QSize(130, 16777215))
        self.year_dropdown.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid #5A9;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #E6F7FF;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:down.png); /* Replace with your own image path */\n"
"    width: 12px;  /* Adjust the width as needed */\n"
"    height: 12px; /* Adjust the height as needed */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #888; /* Optional border around the dropdown */\n"
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
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"    color: black;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.year_dropdown)

        self.month_dropdown = QComboBox(self.centralwidget)
        self.month_dropdown.addItem("")
        self.month_dropdown.addItem("")
        self.month_dropdown.addItem("")
        self.month_dropdown.addItem("")
        self.month_dropdown.addItem("")
        self.month_dropdown.addItem("")
        self.month_dropdown.addItem("")
        self.month_dropdown.addItem("")
        self.month_dropdown.addItem("")
        self.month_dropdown.addItem("")
        self.month_dropdown.addItem("")
        self.month_dropdown.addItem("")
        self.month_dropdown.addItem("")
        self.month_dropdown.setObjectName(u"month_dropdown")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.month_dropdown.sizePolicy().hasHeightForWidth())
        self.month_dropdown.setSizePolicy(sizePolicy)
        self.month_dropdown.setMinimumSize(QSize(0, 30))
        self.month_dropdown.setMaximumSize(QSize(140, 16777215))
        self.month_dropdown.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid #5A9;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #E6F7FF;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:down.png); /* Replace with your own image path */\n"
"    width: 12px;  /* Adjust the width as needed */\n"
"    height: 12px; /* Adjust the height as needed */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #888; /* Optional border around the dropdown */\n"
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
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"    color: black;\n"
"}\n"
"")
        self.month_dropdown.setEditable(False)
        self.month_dropdown.setMaxVisibleItems(7)

        self.horizontalLayout_5.addWidget(self.month_dropdown)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        self.pushButton.clicked.connect(self.view_attendance_table)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(28, 113, 216);\n"
"    color: white;\n"
"    border: 2px solid #388E3C;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4CAF50;\n"
"    border: 2px solid #2E7D32;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #388E3C;\n"
"    border: 2px solid #1B5E20;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #D3D3D3;\n"
"    color: #A0A0A0;\n"
"    border: 2px solid #A0A0A0;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.attendance_table = QTableView(self.centralwidget)
        self.attendance_table.setObjectName(u"attendance_table")
        self.attendance_table.setStyleSheet(u"QTableWidget, QTableView {\n"
"    border: 2px solid #5A9;\n"
"    border-radius: 5px;\n"
"    gridline-color: #888;\n"
"    color: black;\n"
"    background-color: #F5F5F5;\n"
"    selection-background-color: #5A9;\n"
"    selection-color: #FFF;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #5A9;\n"
"    color: white;\n"
"    padding: 4px;\n"
"    border: 1px solid #CCC;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTableWidget::item, QTableView::item {\n"
"    padding: 5px;\n"
"    border: 1px solid #D3D3D3;\n"
"}\n"
"\n"
"QTableWidget::item:selected, QTableView::item:selected {\n"
"    background-color: #5A9;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #5A9;\n"
"    border: 2px solid #CCC;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #E6E6E6;\n"
"    width: 12px;\n"
"    margin: 22px 0 22px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #888;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:verti"
                        "cal, QScrollBar::sub-line:vertical {\n"
"    background: #CCC;\n"
"    height: 22px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    background: #666;\n"
"}\n"
"")
        self.attendance_table.horizontalHeader().setCascadingSectionResizes(False)

        self.horizontalLayout_6.addWidget(self.attendance_table)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        self.save_button.clicked.connect(self.save_changes)
        self.save_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(28, 113, 216);\n"
"    color: white;\n"
"    border: 2px solid #388E3C;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4CAF50;\n"
"    border: 2px solid #2E7D32;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #388E3C;\n"
"    border: 2px solid #1B5E20;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #D3D3D3;\n"
"    color: #A0A0A0;\n"
"    border: 2px solid #A0A0A0;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.save_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 612, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.populate_years()  # Populate the years in the combo box

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.year_dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Year", None))

        self.month_dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Month", None))
        self.month_dropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"January", None))
        self.month_dropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"February", None))
        self.month_dropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"March", None))
        self.month_dropdown.setItemText(4, QCoreApplication.translate("MainWindow", u"April", None))
        self.month_dropdown.setItemText(5, QCoreApplication.translate("MainWindow", u"May", None))
        self.month_dropdown.setItemText(6, QCoreApplication.translate("MainWindow", u"June", None))
        self.month_dropdown.setItemText(7, QCoreApplication.translate("MainWindow", u"July", None))
        self.month_dropdown.setItemText(8, QCoreApplication.translate("MainWindow", u"August", None))
        self.month_dropdown.setItemText(9, QCoreApplication.translate("MainWindow", u"September", None))
        self.month_dropdown.setItemText(10, QCoreApplication.translate("MainWindow", u"October", None))
        self.month_dropdown.setItemText(11, QCoreApplication.translate("MainWindow", u"November", None))
        self.month_dropdown.setItemText(12, QCoreApplication.translate("MainWindow", u"December", None))

        self.month_dropdown.setCurrentText(QCoreApplication.translate("MainWindow", u"Select Month", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

    def populate_years(self):
        current_year = 2024
        years = [str(year) for year in range(current_year - 20, current_year + 3)]  # Last 50 years
        self.year_dropdown.addItems(years)  # Populate the combo box

    def view_attendance_table(self):
        print("Viewing attendance table")
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("msccsai_students.db")
        if not self.db.open():
            QMessageBox.critical(self.centralwidget, "Error", "Failed to connect to the database")
            return
        year = self.year_dropdown.currentText()
        month = self.month_dropdown.currentText()
        if year == "Select Year" or month == "Select Month":
            return
        self.db.open()
        self.model = QSqlTableModel()
        self.model.setTable(f"{month}_{year}")
        self.model.select()
        self.attendance_table.setModel(self.model)

    def save_changes(self):
        if self.model.submitAll():
            QMessageBox.information(self.centralwidget, "Success", "Changes saved successfully")
        else:
            QMessageBox.warning(self.centralwidget, "Error", "Failed to save changes")



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    attendance_window = QMainWindow()
    ui = viewAttendance()
    ui.setupUi(attendance_window)
    attendance_window.show()
    sys.exit(app.exec())
