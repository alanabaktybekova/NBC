import datetime
import random
import datetime


class Patient:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.created_date = datetime.datetime.now()
        print(self.created_date)
        self.end_date = None
        self.id = random.randint(0, 10000)

    def remove(self):
        self.end_date = datetime.datetime.now()
        print(self.end_date, self.created_date)
        return f'Вы ждали свою очередь - {self.end_date - self.created_date}'

    def check_info(self):
        if self.end_date:
            return f'Человек по имени - {self.first_name} {self.last_name}\nВ очереди был - {self.end_date - self.created_date}'
        return f'Человек по имени - {self.first_name} {self.last_name}\nВ очереди - {self.end_date - datetime.datetime.now()}'


class Queue:
    def __init__(self):
        self.patients = []

    def get_active_patients(self):
        return len([i for i in self.patients if not i.end_date])

    def get_unactive_patients(self):
        return len([i for i in self.patients if i.end_date])

    def add_patient(self, patient: Patient):
        self.patients.append(patient)

    def remain(self, talon):
        for i in range(len(self.patients)):
            if self.patients[i].id == talon:
                return i * 10
        return 'Вашего талона здесь нет'

    def get_time_info(self, talon):
        for i in range(len(self.patients)):
            if self.patients[i].id == talon:
                return self.patients[i].check_info()

    def close_talon(self, talon):
        for i in range(len(self.patients)):
            if self.patients[i].id == talon:
                return self.patients[i].remove()