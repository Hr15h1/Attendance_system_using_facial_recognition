"""
This module provides a GUI application for viewing and exporting attendance data using facial recognition.
Classes:
    ViewAttendance: A class to set up and manage the attendance viewing window.
Functions:
    setupUi(MainWindow): Sets up the user interface for the main window.
    retranslateUi(MainWindow): Sets the text for the UI elements.
    populate_years(): Populates the year dropdown with a range of years.
    view_attendance_table(): Displays the attendance data in a table view.
    save_changes(): Saves any changes made to the attendance data.
    export_attendance(start_date, end_date): Exports the attendance data to an Excel file.
    open_date_dialog(): Opens a dialog to select the date range for exporting attendance data.
Attributes:
    centralwidget (QWidget): The central widget of the main window.
    gridLayout (QGridLayout): The main layout for the central widget.
    verticalLayout (QVBoxLayout): A vertical layout to arrange UI elements.
    horizontalLayout_5 (QHBoxLayout): A horizontal layout for the year and month dropdowns and view button.
    year_dropdown (QComboBox): A dropdown to select the year.
    month_dropdown (QComboBox): A dropdown to select the month.
    pushButton (QPushButton): A button to view the attendance data.
    horizontalLayout_6 (QHBoxLayout): A horizontal layout for the attendance table.
    attendance_table (QTableView): A table view to display the attendance data.
    horizontalLayout_4 (QHBoxLayout): A horizontal layout for the export and save buttons.
    pushButton_2 (QPushButton): A button to export the attendance data.
    save_button (QPushButton): A button to save changes to the attendance data.
    menubar (QMenuBar): The menu bar of the main window.
    statusbar (QStatusBar): The status bar of the main window.
    db (QSqlDatabase): The database connection.
    model (QSqlTableModel): The model for the attendance table view.
"""


from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, QObject, Qt)
from PySide6.QtWidgets import (QComboBox, QGridLayout, QHBoxLayout,
    QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QDialog,
    QVBoxLayout, QWidget, QMessageBox, QTableWidget, QTableWidgetItem)
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from exportDialog import ExportDialog

from config_loader import load_config
import pandas as pd
import calendar
import psycopg2
import datetime


config = load_config()


class ViewAttendance(QObject):

    
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
"    image: url(./icons/down_arrow.png); /* Replace with your own image path */\n"
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
"    image: url(./icons/down_arrow.png); /* Replace with your own image path */\n"
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
        self.day_dropdown = QComboBox(self.centralwidget)
        self.day_dropdown.setObjectName(u"day_dropdown")
        self.day_dropdown.setMaximumSize(QSize(120, 16777215))
        self.day_dropdown.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid #5A9;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #E6F7FF;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(./icons/down_arrow.png); /* Replace with your own image path */\n"
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

        self.horizontalLayout_5.addWidget(self.day_dropdown)

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
        self.attendance_tableWidget = QTableWidget(self.centralwidget)
        self.attendance_tableWidget.setObjectName(u"attendance_tableWidget")
        self.attendance_tableWidget.setStyleSheet(u"QTableWidget, QTableView {\n"
"    border: 2px solid #5A9;\n"
"    color: black;\n"
"    border-radius: 5px;\n"
"    gridline-color: #888;\n"
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
"}")

        self.horizontalLayout_6.addWidget(self.attendance_tableWidget)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.open_date_dialog)
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
        self.populate_days()  # Populate the days in the combo box
        self.day_dropdown.insertItem(0, "Select Day")
        self.day_dropdown.setCurrentIndex(0)
        self.attendance_tableWidget.setEditTriggers(QTableWidget.EditTrigger.DoubleClicked)
        
        self.attendance_tableWidget.cellChanged.connect(self.table_changes)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.year_dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Year", None))
        self.day_dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Day", None))
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
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

    def populate_years(self):
        current_year = 2024
        years = [str(year) for year in range(current_year - 20, current_year + 3)]  # Last 50 years
        self.year_dropdown.addItems(years)  # Populate the combo box

    def populate_days(self):
        days = [str(day) for day in range(1, 32)]
        self.day_dropdown.addItems(days)


    def view_attendance_table(self):
        self.attendance_tableWidget.blockSignals(True)
        if QSqlDatabase.contains("qt_sql_default_connection"):
            QSqlDatabase.removeDatabase("qt_sql_default_connection")
        
        self.db = QSqlDatabase.addDatabase("QPSQL")
        self.db.setHostName("localhost")
        self.db.setDatabaseName("msccsai_students")
        self.db.setUserName("postgres")
        self.db.setPassword("admin")
        if not self.db.open():
            QMessageBox.critical(self.centralwidget, "Error", "Failed to connect to the database")
            return
        
        # query = QSqlQuery(self.db)
        year = self.year_dropdown.currentText()
        month = self.month_dropdown.currentText()
        month_num = datetime.datetime.strptime(month, "%B").month
        day = str(self.day_dropdown.currentText()).zfill(2)
        self.table_name = f"{month}_{year}"
        if year == "Select Year" or month == "Select Month":
            return
        if day == "Select Day":
            query = f"SELECT * FROM {self.table_name}"
        else:
            date = f"{year}-{month_num}-{day}"
            query = f"SELECT * FROM {self.table_name} WHERE date = '{date}'"


        self.model = QSqlQueryModel()
        self.model.setQuery(query, self.db)



        self.attendance_tableWidget.setRowCount(self.model.rowCount())
        self.attendance_tableWidget.setColumnCount(self.model.columnCount())
        self.attendance_tableWidget.setHorizontalHeaderLabels([self.model.headerData(i, Qt.Horizontal) for i in range(self.model.columnCount())])

        for row in range(self.model.rowCount()):
            for column in range(self.model.columnCount()):
                item = QTableWidgetItem(str(self.model.data(self.model.index(row, column))))
                self.attendance_tableWidget.setItem(row, column, item)


        
        self.attendance_tableWidget.blockSignals(False)


        return
        

    def table_changes(self, row, column):
        new_value = self.attendance_tableWidget.item(row, column).text()
        column_name = self.model.headerData(column, Qt.Horizontal)
        primary_key_value = self.attendance_tableWidget.item(row, 0).text()

        
        query = QSqlQuery(self.db)
        query.prepare(f"UPDATE {self.table_name} SET {column_name} = :new_value WHERE attendance_id = :primary_key_value")
        query.bindValue(":new_value", new_value)
        query.bindValue(":primary_key_value", primary_key_value)

        if not query.exec():
            QMessageBox.warning(self.centralwidget, "Error", "Failed to update the database")
        else:
            QMessageBox.information(self.centralwidget, "Success", "Changes saved successfully")
        
        
        return

    def export_attendance(self, start_date, end_date):
        sheet_added = False
        conn = psycopg2.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database = config.DB_NAME
        )
        # test_conn = sqlite3.connect("testdatabase.db") # For testing purposes
        start_month = start_date.month()
        end_month = end_date.month()
        start_year = start_date.year()
        end_year = end_date.year()

        with pd.ExcelWriter(f"{config.EXPORT_PATH}attendance.xlsx", engine = 'openpyxl') as writer:
            for year in range(start_year, end_year + 1):
                for month in range(1, 13):
                    if (year == start_year and month < start_month) or (year == end_year and month > end_month):
                        continue
                    try:
                        table_name = f"{calendar.month_name[month].lower()}_{year}"

                        cursor = conn.cursor()
                        cursor.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '{table_name}')")
                        table_exists = cursor.fetchone()[0]

                        if not table_exists:
                            QMessageBox.warning(self.centralwidget, "Error", f"Table {table_name} does not exist")
                            continue


                        df = pd.read_sql(f"SELECT attendance_id, student_rollno, student_name, date, morning, afternoon FROM {table_name}", conn)
                        # df = pd.read_sql(f"SELECT * FROM {table_name}", test_conn) # For testing purposes
                        df.to_excel(writer, sheet_name = table_name, index = False)
                        sheet_added = True
                    except Exception as e:
                        QMessageBox.warning(self.centralwidget, "Error", f"Table {table_name} does not exist")
            if not sheet_added:
                QMessageBox.warning(self.centralwidget, "Error", "No data to export")
        conn.close()
        QMessageBox.information(self.centralwidget, "Success", "Attendance exported successfully")
        return
            

    def open_date_dialog(self):
        dialog = ExportDialog(self.centralwidget)
        if dialog.exec() == QDialog.Accepted:
            start_date, end_date = dialog.get_date()
            # print(calendar.month_name[start_date.month()], end_date.year())
            self.export_attendance(start_date, end_date)
        else:
            print("Cancelled")





# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     attendance_window = QMainWindow()
#     ui = ViewAttendance()
#     ui.setupUi(attendance_window)
#     attendance_window.show()
#     sys.exit(app.exec())
