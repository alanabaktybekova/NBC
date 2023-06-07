# 1
# class Soldier:
#     def __init__(self, name):
#         self.name = name
#
# class Guns:
#     def __init__(self, model, ammo_capacity):
#         self.model = model
#         self.ammo_capacity = ammo_capacity
#         self.ammo_count = ammo_capacity
#
#     def shoot(self):
#         if self.ammo_count > 0:
#             print('тиги-тигитиш')
#             self.ammo_count -= 1
#         else:
#             print('Патроны закончились, перезарядитесь')
#
#     def reload(self):
#         self.ammo_count = self.ammo_capacity
#         print('Оружие перезаряжено')
#
# class Act_of_Shooting(Soldier, Guns):
#     def __init__(self, name, model, ammo_capacity):
#         Soldier.__init__(self, name)
#         Guns.__init__(self, model, ammo_capacity)
#
#     def fire(self):
#         self.shoot()
#         if self.ammo_count == 0:
#             self.reload()
#             self.shoot()
#
# rayn = Act_of_Shooting('Райан', 'AK-47', 30)
# rayn.fire()
# rayn.fire()
# rayn.fire()

# 2
# class House:
#     def __init__(self, house_type, area):
#         self.house_type = house_type
#         self.area = area
#         self.furniture_list = []
#         self.remaining_area = area
#
#     def add_furniture(self, furniture):
#         if furniture.area <= self.remaining_area:
#             self.furniture_list.append(furniture)
#             self.remaining_area -= furniture.area
#             print(f"{furniture.name} был добавлен в дом")
#         else:
#             print(f"Недостаточно места в доме для {furniture.name}")
#
#     def print_house_info(self):
#         print(f"Тип дома: {self.house_type}")
#         print(f"Общая площадь: {self.area}")
#         print(f"Оставшаяся площадь: {self.remaining_area}")
#         furniture_names = ", ".join([furniture.name for furniture in self.furniture_list])
#         print(f"Список мебели: {furniture_names}")
#
#
# class Furniture:
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#
#
# bedroom = Furniture('Спальня', 4)
# wardrobe = Furniture('Гардероб', 2)
# table = Furniture('Стол', 1.5)
# sofa = Furniture('Диван', 2)
#
# my_house = House('Квартира', 50)
# my_house.add_furniture(bedroom)
# my_house.add_furniture(wardrobe)
# my_house.add_furniture(table)
# my_house.add_furniture(sofa)
#
# my_house.print_house_info()

# 3
# class Student:
#     def __init__(self, name, age, major):
#         self.name = name
#         self.age = age
#         self.major = major
#
#     def __str__(self):
#         return f"<name: {self.name}, age: {self.age}, major: {self.major}>"
#
#
#
# Alana = Student("Alana Baktybekova", 23, "English")
# Janul = Student("Janul Abdykadyrova", 24, "Biology")
# Penny = Student("Nazar Baktybekov", 21, "Physics")
#
#
# print(Alana)
# print(Janul)

# 4
# def dollarize(amount):
#     # Определяем знак числа
#     sign = '-' if amount < 0 else ''
#     # Преобразуем число в строку и разделяем целую и дробную части
#     str_amount = str(abs(round(amount, 2)))
#     whole_part, decimal_part = str_amount.split('.')
#     # Добавляем запятые к целой части
#     whole_part_with_commas = ""
#     while whole_part:
#         whole_part, last_three = whole_part[:-3], whole_part[-3:]
#         whole_part_with_commas = f",{last_three}{whole_part_with_commas}"
#     whole_part_with_commas = whole_part_with_commas[1:] if whole_part_with_commas.startswith(",") else whole_part_with_commas
#     # Форматируем и возвращаем результат
#     return f"{sign}${whole_part_with_commas}.{decimal_part.ljust(2, '0')}"
#
# print(dollarize(123456.78901))
# print(dollarize(-123456.7801))

# 5
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

deck = Deck()
deck.shuffle_deck()

card1 = deck.deal_card()
card2 = deck.deal_card()

print(card1)
print(card2)