from connectionDB import connectionDB
from Student import Student

db = connectionDB()
students = db.get_data()
#stud=Student(2,"Ahmad")
#db.insert_data(stud)
#db.update_data(Student(1,"Rami"))
#db.delete_data(2)
db.close_connection()


for student in students: 
    student.print_Data()


