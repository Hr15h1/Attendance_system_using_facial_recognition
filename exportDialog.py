from PySide6.QtCore import (QCoreApplication, QDate,
    QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QComboBox, QDialog,
    QDialogButtonBox, QFrame, QLabel, QLayout,
    QSizePolicy, QVBoxLayout, QWidget)

from PySide6.QtCore import (QCoreApplication, QDate,
    QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QComboBox, QDialog,
    QDialogButtonBox, QFrame, QHBoxLayout, QLabel,
    QLayout, QSizePolicy, QVBoxLayout, QWidget)

class ExportDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.populate_months()
        self.populate_years()



    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(401, 300)
        Dialog.setStyleSheet(u"QDialog {\n"
"	background-color: #2F2F2F\n"
"}")
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 401, 291))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid #5A9;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #E6F7FF;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:down.png);\n"
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
"}\n"
"QLabel {\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"	color: white;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.frame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 30, 361, 201))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout.addWidget(self.comboBox_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox_3 = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_2.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_2.addWidget(self.comboBox_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"QPushButton {\n"
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
"QPushButton:disabled {\n"
"    background-color: #D3D3D3;\n"
"    color: #A0A0A0;\n"
"    border: 2px solid #A0A0A0;\n"
"}")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select start date:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Select end date:", None))
    # retranslateUi

    
    def populate_years(self):
        current_year = 2024
        years = [str(year) for year in range(current_year - 20, current_year + 3)]  # Last 50 years
        self.comboBox_2.addItems(years)
        self.comboBox_4.addItems(years)

    def populate_months(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.comboBox.addItems(months)
        self.comboBox_3.addItems(months)

    def get_date(self):
        start_date = QDate(int(self.comboBox_2.currentText()), self.comboBox.currentIndex() + 1, 1)
        end_date = QDate(int(self.comboBox_4.currentText()), self.comboBox_3.currentIndex() + 1, 1)
        return start_date, end_date

    
