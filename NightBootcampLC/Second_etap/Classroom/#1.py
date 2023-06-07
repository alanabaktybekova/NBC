#a)
class Person:
    def __init__(self, fullName, address, age=18):
        self.fullName = fullName
        self.age = age
        self.place = address

    def talk(self):
        print(f'{self.fullName} говорит')

    def move(self, newAddres):
        self.place = newAddres

    def __str__(self):
        return f"Person(fullName={self.fullName}, age={self.age}, place={self.place})"

person = Person("Nazar Baktybekov", "139 Lenina St", 15)
print(person)



