from PySide6.QtCore import QThread, QObject, Signal, QTimer
from PySide6.QtGui import QImage, QPixmap
import cv2
import numpy as np
import time

class CameraWorker(QObject):
    frame_captured = Signal(np.ndarray)
    finished = Signal()

    def __init__(self, camera_id):
        super().__init__()
        self.camera_id = camera_id
        self.alive = False

    def start_camera(self):
        self.alive = True
        self.cap = cv2.VideoCapture(self.camera_id)

        while self.alive:
            ret, frame = self.cap.read()
            if ret:

                frame = cv2.flip(frame, 1)
                self.height, self.width, img_channels = frame.shape
                bytesPerLine = img_channels * self.width
                self.q_image = QImage(frame.data, self.width, self.height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                time.sleep(0.4)
                self.frame_captured.emit(self.q_image)
        self.cap.release()
        self.finished.emit()

    def stop_camera(self):
        self.alive = False
