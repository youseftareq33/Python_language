from abc import ABC

class Person(ABC):
    
    def __init__(self,__name,__income):
        self.__name=__name
        self.__income=__income

    # getter and setter:
    def get_name(self):
        return self.__name
    
    def set_name(self, new__name):
        self.__name = new__name

    
    def get_income(self):
        return self.__income

    def set_income(self, new__income):
        self.__income = new__income


    # methods:
    def eat():
        pass

    def speak():
        pass

    #overload method
    def calculate_income(self, num_years, extra=0):
        return (self.__income * 12 * num_years)+extra