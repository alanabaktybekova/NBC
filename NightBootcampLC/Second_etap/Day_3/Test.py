import random
import string
import datetime

class Car:
    def __init__(self, car_number):
        self.car_number = car_number

class Parking:
    def __init__(self, max_places):
        self.max_places = max_places
        self.places = max_places
        self.cars = []
        self.records = {}
        self.__generate_tickets()

    def __generate_tickets(self):
        chars = string.ascii_uppercase + string.digits
        while len(self.records) < self.max_places:
            ticket = ''.join(random.choice(chars) for _ in range(6))
            if ticket not in self.records:
                self.records[ticket] = {'Машина': None, 'Вошел': None, 'Вышел': None, 'В парковке': False}

    def addCar(self, car):
        for ticket, record in self.records.items():
            if record['Машина'] is None:
                record['Машина'] = car
                record['Вошли'] = datetime.datetime.now()
                record['В паркинге'] = True
                self.cars.append(car)
                self.places -= 1
                print(f"Машина {car.car_number} добавлена на паркинг")
                print(f"Available places: {self.places}/{self.max_places}")
                print(f"Номер билета: {ticket}")
                return ticket
        print("Извините, сейчас нет свободных парковочных мест.")
        return None

    def out_car(self, ticket):
        if ticket in self.records and self.records[ticket]['В паркинге']:
            record = self.records[ticket]
            record['Выход'] = datetime.datetime.now()
            record['Паркинг'] = False
            self.cars.remove(record['Машина'])
            self.places += 1
            print(f"Машина {record['car'].car_number} покинула паркинг")
            print(f"Available places: {self.places}/{self.max_places}")
            return True
        else:
            print("К сожалению, билет недействителен или машина уже покинула парковку")
            return False

    def get_car_info(self, car):
        for ticket, record in self.records.items():
            if record['машина'] == car:
                print(f"Номер билета: {ticket}")
                print(f"Номер машины: {car.car_number}")
                if record['В паркинге']:
                    print("В данный момент машина находится на паркинге")
                else:
                    print(f"Автомобиль выехал со парковки в {record['Выход']}")
                return
        print("Извините, для этой машины нет записи")

    def get_ticket_info(self, ticket):
        if ticket in self.records:
            record = self.records[ticket]
            print(f"Номер билета: {ticket}")
            if record['машина'] is not None:
                print(f"Номер машины: {record['Машина'].car_number}")
                if record['В паркинге']:
                    print("В данный момент машина находится на паркинге")
                else:
                    print(f"Автомобиль выехал со стоянки в {record['выход']}")
            else:
                print("К этому билету не привязан ни одину машину")
        else:
            print("К сожалению, билет недействителен")

