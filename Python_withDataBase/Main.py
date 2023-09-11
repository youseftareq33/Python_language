from connectionDB import connectionDB
from Student import Student

db = connectionDB()
students = db.get_data()
db.close_connection()

for student in students: 
    student.print_data()
