# Attendance Management system using facial recognition

This project implements an attendance management system using facial recognition technology. It utilizes PySide6 for the GUI, OpenCV and DeepFace library for camera operations, and SQLite for database management. The application allows users to start and stop the camera, mark attendance, and view attendance records.

## Features

- **Facial Recognition**: Uses OpenCV to recognize faces and mark attendance.
- **GUI**: Built with PySide6 for a user-friendly interface.
- **Database Management**: Uses SQLite to store and manage attendance records.
- **CSV Integration**: Imports student details from CSV files.
- **Monthly Attendance Tables**: Creates separate tables for each month to store attendance records.


## Installation

1. **Clone the repository**:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Set up the virtual environment**:
    (recommended python version 3.10.11)
    ```sh
    python -m venv attendance
    source attendance/Scripts/activate  # On Windows
    # source attendance/bin/activate    # On Unix or MacOS
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Configure required paths in paths.py**

2. **Run the application**:
    ```sh
    python app.py
    ```

3. **Mark Attendance**:
    - Start the camera by clicking the "START" button.
    - The system will recognize faces and mark attendance in the database.
    - Stop the camera by clicking the "STOP" button.

4. **View Attendance**:
    - Click the "View Attendance" button to open a new window displaying attendance records.

## Database

- The system uses an SQLite database.
- The student details can be stored as a csv file, which must then be added to the paths.py.
- Attendance records are stored in monthly tables named `<Month>_<Year>`.


## Acknowledgements

- OpenCV, DeepFace for facial recognition.
- PySide6 for the GUI framework.
- SQLite for database management.
