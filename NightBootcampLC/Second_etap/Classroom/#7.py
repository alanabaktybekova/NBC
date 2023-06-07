class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def drive(self, distance):
        fuel_needed = distance / 10
        if self.fuel >= fuel_needed:
            self.__subtract_fuel(fuel_needed)
            self.__add_distance(distance)
            print('Поехали!')
        else:
            print('Нужно больше топлива, пожалуйста, залейте больше!')

    def __add_distance(self, distance):
        self.odometer += distance

    def __subtract_fuel(self, fuel_needed):
        self.fuel -= fuel_needed

my_car = Car(make='Laborgini', model='Urus', year='2021')

my_car.drive(20)
my_car.drive(500)

