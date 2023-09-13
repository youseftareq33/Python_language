import mysql.connector
from Student import Student

class connectionDB:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="1202057",
            database="DB_Python"
        )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


    def get_data(self):
        query = "SELECT * FROM Student"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        students = []
        for row in results:
            id, name = row
            student = Student(id, name)
            students.append(student)
        return students





    def insert_data(self, student):
        query = "INSERT INTO Student (id, name) VALUES (%s, %s)"
        values = (student.id, student.name)
        self.cursor.execute(query, values)
        self.connection.commit()

    def update_data(self, student):
        query = "UPDATE Student SET name = %s WHERE id = %s"
        values = (student.name, student.id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_data(self, student_id):
        query = "DELETE FROM Student WHERE id = %s"
        self.cursor.execute(query, (student_id,))
        self.connection.commit()
