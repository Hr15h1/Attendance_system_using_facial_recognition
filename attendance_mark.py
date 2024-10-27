
import time
import ctypes
import psycopg2
def mark_attendance(label_name, roll_no):
    roll_no = roll_no.split(": ")[1]
    label_name = label_name.text().split(": ")[1]
    conn = psycopg2.connect(
        user = 'postgres',
        password = 'admin',
        host = 'localhost',
        database = 'msccsai_students'
    )

    mycursor = conn.cursor()
    #Create a table for each month
    query = f"CREATE TABLE IF NOT EXISTS {time.strftime('%B')}_{time.strftime('%Y')} (attendance_ID SERIAL, student_rollno int, student_name varchar(100), time varchar(10), date varchar(11), morning varchar(10), afternoon varchar(10), FOREIGN KEY(student_rollno) REFERENCES students_details(id), PRIMARY KEY(attendance_ID, student_rollno));"
    mycursor.execute(query)

    #Check if the session is morning or afternoon
    if time.localtime().tm_hour < 12:
        sql = f"INSERT INTO {time.strftime('%B')}_{time.strftime('%Y')} (student_rollno, student_name, time, date, morning, afternoon) VALUES ({roll_no}, '{label_name}', '{time.strftime('%H:%M:%S')}', '{time.strftime('%Y-%m-%d')}', 'Present', 'Null')"
        mycursor.execute(sql)
    else:

        #Check if the attendance for the morning session is marked or not using a dialog box
        status_morning = ctypes.windll.user32.MessageBoxW(0, "Were you present for the morning session?", "Mark Attendance", 4)
        if status_morning == 6:
            #If the student was present for the morning session, mark the attendance for the afternoon session
            status = "Present"
            morning_attendance = ctypes.windll.user32.MessageBoxW(0, "Did you mark the attendance for the morning session?", "Mark Attendance", 4)
            if morning_attendance == 6:
                #If the attendance for the morning session is marked, insert the attendance for the afternoon session
                sql = f"UPDATE {time.strftime('%B')}_{time.strftime('%Y')} SET afternoon = 'Present' WHERE student_rollno = {roll_no} AND date = '{time.strftime('%Y-%m-%d')}'"
                mycursor.execute(sql)
            else:
                #If the attendance for the morning session is not marked, insert the attendance for the morning session and afternoon session
                sql = f"INSERT INTO {time.strftime('%B')}_{time.strftime('%Y')} (student_rollno, student_name, time, date, morning, afternoon) VALUES ({roll_no}, '{label_name}', '{time.strftime('%H:%M:%S')}', '{time.strftime('%Y-%m-%d')}', 'Present', 'Present')"
                mycursor.execute(sql)

        else:

            #If the student was not present for the morning session, insert the attendance for the afternoon session
            sql = f"INSERT INTO {time.strftime('%B')}_{time.strftime('%Y')} (student_rollno, student_name, time, date, morning, afternoon) VALUES ({roll_no}, '{label_name}', '{time.strftime('%H:%M:%S')}', '{time.strftime('%Y-%m-%d')}', 'Late', 'Present')"
            mycursor.execute(sql)

    
    conn.commit()
    conn.close()

    #Display a message box to show that the attendance has been marked
    ctypes.windll.user32.MessageBoxW(0, f"Attendance for {label_name} marked successfully", "Mark Attendance", 0)
    return
