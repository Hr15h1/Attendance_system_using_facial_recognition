from PySide6.QtCore import QThread, QObject, Signal
from PySide6.QtGui import QImage, QPixmap
import csv
import cv2
from deepface import DeepFace

import numpy as np

class StartModel(QObject):
    finished = Signal()
    progress = Signal(QImage)
    result_list = Signal(list)

    def __init__(self, main_window):
        super().__init__()
        self.alive = True
        self.main_window = main_window
    def start_model(self):
        csv_file = "students.csv"

        # Initialize an empty dictionary
        students_dict = {}

        # Read the data from the CSV file into the dictionary
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Assuming the first column is the key and the second column is the value
                key = int(row["ID"])  # Convert the key to an integer
                value = row["Name"]
                students_dict[key] = value

        while self.alive:
            try:
                
            # Specify the CSV file name
                # q_image = self.main_window.q_image.convertToFormat(QImage.Format_RGB32)
                # camera_frame = qimage2ndarray.rgb_view(q_image)
                q_image = self.main_window.q_image.convertToFormat(QImage.Format_RGB32)
                width = q_image.width()
                height = q_image.height()
                ptr = q_image.bits()
                camera_frame = np.array(ptr, dtype = np.uint8).reshape((height, width, 4))
                camera_frame = camera_frame[:, :, :3]
                camera_frame = np.ascontiguousarray(camera_frame)
                result = DeepFace.find(camera_frame, db_path = "./database", enforce_detection = False, model_name = "Dlib", detector_backend = "dlib", align = True, distance_metric = "euclidean", anti_spoofing = True, refresh_database = True, silent = False)
                
                name = result[0]['identity'][0].split('\\')[1]

                if name:
                    xmin = int(result[0]['source_x'][0])
                    ymin = int(result[0]['source_y'][0])
                    w = result[0]['source_w'][0]
                    h = result[0]['source_h'][0]

                    xmax = int(xmin + w)
                    ymax = int(ymin + h)

                    cv2.rectangle(camera_frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
                    cv2.rectangle(camera_frame, (xmin, ymin - 25), (xmax, ymin),(255, 255, 255), -1)
                    cv2.putText(camera_frame, name, (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0),2, cv2.LINE_AA)


                for k in students_dict.keys():
                        if students_dict[k] == name:
                            roll_no = k
                            break

                self.result_list.emit([name, roll_no])

            except Exception as e:
                q_image = self.main_window.q_image.convertToFormat(QImage.Format_RGB32)
                width = q_image.width()
                height = q_image.height()
                ptr = q_image.bits()
                camera_frame = np.array(ptr, dtype = np.uint8).reshape((height, width, 4))
                camera_frame = camera_frame[:, :, :3]
                camera_frame = np.ascontiguousarray(camera_frame)
                spoof_result = DeepFace.extract_faces(camera_frame, detector_backend = "opencv", enforce_detection = False, align = False, anti_spoofing = True)
                if len(spoof_result) > 0:
                    x_min = spoof_result[0]['facial_area']['x']
                    y_min = spoof_result[0]['facial_area']['y']
                    x_max = x_min + spoof_result[0]['facial_area']['w']
                    y_max = y_min + spoof_result[0]['facial_area']['h']
                    cv2.rectangle(camera_frame, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)
                    cv2.rectangle(camera_frame, (x_min, y_min - 25), (x_max, y_min), (255, 255, 255), -1)
                    cv2.putText(camera_frame, "Spoofing Detected", (x_min, y_min), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

            self.height, self.width, img_channel = camera_frame.shape
            bytes_per_line = img_channel * self.width
            self.q_image = QImage(camera_frame.data, self.width, self.height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
            self.progress.emit(self.q_image)

        self.finished.emit()