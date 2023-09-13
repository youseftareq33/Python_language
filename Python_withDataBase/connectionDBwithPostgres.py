import psycopg2
from Student import Student 

conn= psycopg2.connect(
    host="localhost",
    dbname="stud_record",
    user="postgres",
    password="1202057",
    port="5432"
)

cur=conn.cursor()

def get_data():
    cur.execute("SELECT * FROM Student")
    results = cur.fetchall()
    students = []
    for row in results:
        id, name = row
        student = Student(id, name)
        students.append(student)
    return students

stud_list=get_data()

for student in stud_list: 
    student.print_Data()

id=10
name="gg"
#INSERT INTO Student (id, name) VALUES (%s, %s);", (id, name)
#cur.execute("INSERT INTO Student (id, name) VALUES (2, 'Rami');")
#cur.execute("DELETE FROM Student WHERE id = 2;")
#cur.execute("UPDATE Student SET name = 'Updated Name' WHERE id = 2;")

conn.commit()

cur.close()
conn.close()