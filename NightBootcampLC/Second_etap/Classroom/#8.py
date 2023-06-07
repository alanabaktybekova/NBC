class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Name:', self.name)
        print('Age:', self.age)


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('Section:', self.section)


student = Student("Alana", 18, "A")
student.displayStudent()
