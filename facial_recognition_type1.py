"""
This module implements an attendance system using facial recognition.
Functions:
    start_camera(camera_view, name_label, roll_label, main_window):
        Starts the camera and performs facial recognition to mark attendance.
Parameters:
    camera_view (QGraphicsView): The view where the camera feed will be displayed.
    name_label (QLabel): The label to display the recognized name.
    roll_label (QLabel): The label to display the recognized roll number.
    main_window (QMainWindow): The main window of the application containing the video source and control flags.
Details:
    - Uses OpenCV for video capture and display.
    - Uses DeepFace for facial recognition.
    - Reads student data from a CSV file.
    - Displays recognized faces with bounding boxes and names.
    - Marks attendance by updating the labels with the recognized name and roll number.
    - Handles anti-spoofing detection.
    - Allows quitting the camera feed by pressing 'q', 'Q', or 'Esc' key.
"""
import os
import cv2
from deepface import DeepFace

from datetime import datetime
import csv

from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QGraphicsScene

from config_loader import load_config

year = datetime.now().year
title = datetime.now().strftime("%B_%Y")

config = load_config()



#Function to start the camera and perform facial recognition
def start_camera(camera_view, main_window, purpose, name_label = None, roll_label = None):


    if purpose == "mark_attendance":
        source = main_window.source
        scene = QGraphicsScene()
        camera_view.setScene(scene)

        # Specify the CSV file name
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

        

        
        frame_displayed = False
        while main_window.alive:
            has_frame, frame = source.read()
            if not has_frame:
                break
            frame = cv2.flip(frame, 1)

            if not frame_displayed:
                frame_displayed = True

            try:
                # Perform face recognition by passing each frame to the models
                #refresh_database = False so that the model may work without the photos in the database
                #silent = True to suppress the warnings
                #To add more photos, add them to the database folder and set refresh_database = True
                result1 = DeepFace.find(frame, db_path = "./database", enforce_detection = False, model_name = "Dlib", detector_backend = "dlib", align = True, distance_metric = "euclidean", anti_spoofing = True, refresh_database = True, silent = False)
                # result1 = DeepFace.find(frame, db_path = "./database", enforce_detection = False, model_name = "VGG-Face", detector_backend = "ssd", align = False, distance_metric = "euclidean_l2", anti_spoofing = True, refresh_database = True, silent = False)
                # result3 = DeepFace.find(frame, db_path = "./database", enforce_detection = False, model_name = "ArcFace", detector_backend = "yunet", align = True, distance_metric = "euclidean_l2", anti_spoofing = True, refresh_database = False, silent = True)
                # result4 = DeepFace.find(frame, db_path = "./database", enforce_detection = False, model_name = "GhostFaceNet", detector_backend = "opencv", align = False, distance_metric = "cosine", anti_spoofing = True, refresh_database = False, silent = True)
                # result5 = DeepFace.find(frame, db_path = "./database", enforce_detection = False, model_name = "SFace", detector_backend = "ssd", align = True, distance_metric = "euclidean", anti_spoofing = True, refresh_database = False, silent = True)
                # result6 = DeepFace.find(frame, db_path = "./database", enforce_detection = False, model_name = "Facenet512", detector_backend = "retinaface", align = True, distance_metric = "cosine", anti_spoofing = True, refresh_database = False, silent = True)
                # result7 = DeepFace.find(frame, db_path = "./database", enforce_detection = False, model_name = "Facenet", detector_backend = "yunet", align = True, distance_metric = "euclidean_l2", anti_spoofing = True, refresh_database = False, silent = True)

                if len(result1[0]['identity']) > 0:
                    
                    n1 = result1[0]['identity'][0].split('\\')[1]
                else:
                    n1 = 'empty'
                # if len(result2[0]['identity']) > 0:
                    
                #     n2 = result2[0]['identity'][0].split('\\')[1]
                # else:
                #     n2 = 'empty'
                # if len(result3[0]['identity']) > 0:
                    
                #     n3 = result3[0]['identity'][0].split('\\')[1]
                # else:
                #     n3 = 'empty'
                # if len(result4[0]['identity']) > 0:
                    
                #     n4 = result4[0]['identity'][0].split('\\')[1]
                # else:
                #     n4 = 'empty'
                # if len(result5[0]['identity']) > 0:
                    
                #     n5 = result5[0]['identity'][0].split('\\')[1]
                # else:
                #     n5 = 'empty'
                # if len(result6[0]['identity']) > 0:
                    
                #     n6 = result6[0]['identity'][0].split('\\')[1]
                # else:
                #     n6 = 'empty'
                # if len(result7[0]['identity']) > 0:
                    
                #     n7 = result7[0]['identity'][0].split('\\')[1]
                # else:
                #     n7 = 'empty'

            

                # n = [n1, n2, n3, n4, n5] #list of names generated by the models

                # name = max(set(n), key = n.count) #get the most common name from the list n


                # If the name is empty, assign the first non-empty name from list n
                # if name == 'empty':
                #     for names in n:
                #         if names != 'empty':
                #             name = names


                if len(result1[0]['identity']) > 0:
                    name = n1
                    # Get the bounding box coordinates
                    xmin = int(result1[0]['source_x'][0])
                    ymin = int(result1[0]['source_y'][0])
                    w = result1[0]['source_w'][0]
                    h = result1[0]['source_h'][0]

                    xmax = int(xmin + w)
                    ymax = int(ymin + h)

                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
                    cv2.rectangle(frame, (xmin, ymin - 25), (xmax, ymin),(255, 255, 255), -1)
                    cv2.putText(frame, name, (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0),2, cv2.LINE_AA)
                        


                    #Mark attendance
                    
                    name_label.setText(f"Name: {name}")

                    for k in students_dict.keys():
                            if students_dict[k] == name:
                                roll_no = k
                                break

                    roll_label.setText(f"Roll No: {roll_no}")




                    height, width, _ = frame.shape
                    bytes_per_line = 3 * width
                    q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

                    pixmap = QPixmap.fromImage(q_img)
                    scene.clear()
                    scene.addPixmap(pixmap)
                    
                    key1 = cv2.waitKey(1)

                    if key1 == ord('q') or key1 == ord('Q') or key1 == 27:
                        main_window.alive = False
                        break
                
            except ValueError as e:
                #Perform spoof detection if any of the models in the try block detects anti_spoofing
                spoof_result = DeepFace.extract_faces(frame, detector_backend = "opencv", enforce_detection = False, align = False, anti_spoofing = True)
                if len(spoof_result) > 0:
                    x_min = spoof_result[0]['facial_area']['x']
                    y_min = spoof_result[0]['facial_area']['y']
                    x_max = x_min + spoof_result[0]['facial_area']['w']
                    y_max = y_min + spoof_result[0]['facial_area']['h']
                    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)
                    cv2.rectangle(frame, (x_min, y_min - 25), (x_max, y_min), (255, 255, 255), -1)
                    cv2.putText(frame, "Spoofing Detected", (x_min, y_min), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
            
            # Display the frame

            height, width, _ = frame.shape
            bytes_per_line = 3 * width
            q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

            pixmap = QPixmap.fromImage(q_img)
            scene.clear()
            scene.addPixmap(pixmap)        

            key = cv2.waitKey(1)
            if key == ord('q') or key == ord('Q') or key == 27:
                main_window.alive = False

    #start the camera to add student
    elif purpose == "add_student":
        source = main_window.source
        k = main_window.spinBox.value()
        source.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        source.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        scene = QGraphicsScene()
        camera_view.setScene(scene)


        while main_window.alive:
            has_frame, frame = source.read()
            if not has_frame:
                break
            frame = cv2.flip(frame, 1)

            # Perform face detection
            face = DeepFace.extract_faces(frame, detector_backend="dlib", align = True, expand_percentage=50.0)
            if len(face) > 0:
                # Get the bounding box coordinates
                x_min = face[0]['facial_area']['x']
                y_min = face[0]['facial_area']['y']
                x_max = x_min + face[0]['facial_area']['w']
                y_max = y_min + face[0]['facial_area']['h']
                # Draw the bounding box and the student number
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
                cv2.putText(frame, str(k), (x_min, y_min), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
                # Save the cropped face to the database folder
                cropped_frame = frame[y_min:y_max, x_min:x_max]
                student_name = main_window.lineEdit_4.text()
                # path = f"./database/{student_name}"
                path = f"./database/{student_name}"
                if not os.path.exists(path):
                    os.makedirs(path)
                cv2.imwrite(f"{path}/{k}.jpg", cropped_frame)

            height, width, _ = frame.shape
            bytes_per_line = 3 * width
            q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

            pixmap = QPixmap.fromImage(q_img)
            scene.clear()
            scene.addPixmap(pixmap)

            key = cv2.waitKey(1)
            if key == ord('q') or key == ord('Q') or key == 27 or k == 0:
                main_window.alive = False
            k -= 1
        # Release the video source and destroy the window
        scene.clear()
        camera_view.setScene(scene)
        source.release()
        return 1