import sys
from facial_recognition_type1 import start_camera, stop_camera
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1082, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1063, 720))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1081, 691))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.cameraView = QGraphicsView(self.horizontalLayoutWidget)
        self.cameraView.setObjectName(u"cameraView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cameraView.sizePolicy().hasHeightForWidth())
        self.cameraView.setSizePolicy(sizePolicy1)
        self.cameraView.setMinimumSize(QSize(640, 480))
        self.cameraView.setMaximumSize(QSize(640, 480))

        self.verticalLayout_5.addWidget(self.cameraView)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.startButton = QPushButton(self.horizontalLayoutWidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(210, 59))
        self.startButton.setMaximumSize(QSize(210, 59))
        icon = QIcon(QIcon.fromTheme(u"media-playback-start"))
        self.startButton.setIcon(icon)
        self.startButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.startButton)

        self.stopButton = QPushButton(self.horizontalLayoutWidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(210, 59))
        self.stopButton.setMaximumSize(QSize(210, 59))
        icon1 = QIcon(QIcon.fromTheme(u"media-playback-stop"))
        self.stopButton.setIcon(icon1)
        self.stopButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.stopButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.horizontalLayoutWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy1.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy1)
        self.plainTextEdit.setMinimumSize(QSize(405, 144))
        self.plainTextEdit.setMaximumSize(QSize(405, 244))

        self.verticalLayout_3.addWidget(self.plainTextEdit)

        self.plainTextEdit_2 = QPlainTextEdit(self.horizontalLayoutWidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        sizePolicy1.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy1)
        self.plainTextEdit_2.setMinimumSize(QSize(405, 66))
        self.plainTextEdit_2.setMaximumSize(QSize(405, 66))

        self.verticalLayout_3.addWidget(self.plainTextEdit_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start Camera", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop Camera", None))
    # retranslateUi
    # retranslateUi



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Buttons for starting and stopping the camera
        self.startButton.clicked.connect(self.start_camera_wrapper)
        self.stopButton.clicked.connect(self.stop_camera_wrapper)  # Connect stop button

        self.cap = None  # Video capture object
        self.alive = False
    def start_camera_wrapper(self):
        self.alive = True

        start_camera(self.cameraView, self.plainTextEdit, self)
    def stop_camera_wrapper(self):
        self.alive = False  # Set the flag to False to stop the camera
        stop_camera()


    def closeEvent(self, event):
        self.alive = False
        if self.cap:
            self.cap.release()
        super().closeEvent(event)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())