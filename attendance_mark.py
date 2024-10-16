
import time
import ctypes
import sqlite3

def mark_attendance(label_name, roll_no):
    roll_no = roll_no.split(": ")[1]
    label_name = label_name.text().split(": ")[1]
    conn = sqlite3.connect("msccsai_students.db")
    mycursor = conn.cursor()

    #Create a table for each month
    query = f"CREATE TABLE IF NOT EXISTS {time.strftime('%B')}_{time.strftime('%Y')} (Attendance_ID INTEGER PRIMARY KEY AUTOINCREMENT, student_rollno INTEGER, student_name TEXT, date TEXT, session TEXT, status TEXT, FOREIGN KEY(student_rollno) REFERENCES students_details(id));"
    mycursor.execute(query)

    #Check if the session is morning or afternoon
    if time.localtime().tm_hour < 12:
        session = "Morning"
    else:
        session = "Afternoon"

        #Check if the attendance for the morning session is marked or not using a dialog box
        status_morning = ctypes.windll.user32.MessageBoxW(0, "Were you present for the morning session?", "Mark Attendance", 4)
        if status_morning == 6:
            status = "Present"
            morning_attendance = ctypes.windll.user32.MessageBoxW(0, "Did you mark the attendance for the morning session?", "Mark Attendance", 4)
            if morning_attendance == 6:
                print()
            else:
                sql = f"INSERT INTO {time.strftime('%B')}_{time.strftime('%Y')} (student_rollno, student_name, date, session, status) VALUES ({roll_no},'{label_name}', '{time.strftime('%Y-%m-%d')}', 'Morning', '{status}')"
                mycursor.execute(sql)
        else:
            status = "Late"

            #Insert the attendance for the morning session
            sql = f"INSERT INTO {time.strftime('%B')}_{time.strftime('%Y')} (student_rollno, student_name, date, session, status) VALUES ({roll_no},'{label_name}', '{time.strftime('%Y-%m-%d')}', 'Morning', '{status}')"
            mycursor.execute(sql)

    #Insert the attendance for the afternoon session
        sql = f"INSERT INTO {time.strftime('%B')}_{time.strftime('%Y')} (student_rollno, student_name, date, session, status) VALUES ({roll_no}, '{label_name}', '{time.strftime('%Y-%m-%d')}', '{session}', 'Present')"
        mycursor.execute(sql)
    conn.commit()
    conn.close()

    #Display a message box to show that the attendance has been marked
    ctypes.windll.user32.MessageBoxW(0, f"Attendance for {label_name} marked successfully", "Mark Attendance", 0)
    return
