class Employee:
    def __new__(cls):
        print("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst
    
    def __init__(self):
        print("__init__ magic method is called")
        self.name = 'Satya'


emp_instance = Employee()


print(emp_instance.name)

# new method: responsible for creating and returning a new instance of a class before it's initialized.