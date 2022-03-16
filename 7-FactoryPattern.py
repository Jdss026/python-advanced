"""
Design Pattern: For modularity, increase complexy
Factory: Not sure what the class will do
"""

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def person_method():
        """Interface Method (each person will have this method"""

#p1 = IPerson() #can't instantiate abstclass IPerson
#p1.person_method()

class Student(IPerson):
    def __init__(self):
        self.name = "Basic Student Name"

    def person_method(self):
        print("I am a Student")

class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am a Teacher")

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()

        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1

if __name__ == "__main__":
    choice = input("Type of person?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()
    
"""
s1 = Student()
s1.person_method()

s1 = Teacher()
s1.person_method()
"""