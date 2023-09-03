class Student:
    def __init__(self, __name, __student_id):
       
        self.__name = __name
        self.__student_id = __student_id

    
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, new_student_id):
        self.__student_id = new_student_id

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Student ID: {self.__student_id}")


student = Student("Alice", "12345")


student.display_info()


student.set_name("Bob")
student.set_student_id("54321")


student.display_info()
