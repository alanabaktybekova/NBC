# Example
# class House:
#     def __init__(self, doors, rooms, price, s=10):
#         self.doors = doors
#         self.rooms = rooms
#         self.price = price
#         self.s = s
#
#     def add_new_door(self):
#         self.doors += 1
#
#     def remove_doors(self, col=1):
#         self.doors -= col
#
#     def __str__(self):
#         return f'Дверей - {self.doors}\nКомнат - {self.rooms}'
#
#     def __add__(self, other):
#         return self.price + other.price
#
#
# artemhome = House(8, 5, 50000, s=6)
# dastanhome = House(6, 5, 20000, 4)
#
# print(artemhome + dastanhome)

#*****************************************************************************1

#Ex from presentation №1
# class Laptop:
#     def __init__(self, model):
#         self.model = model
#         self.specs = {}
#
#     def add_processor(self, processor):
#         self.specs['Processor'] = processor
#
#     def add_ram(self, ram):
#         self.specs['RAM'] = ram
#
#     def add_graphics_card(self, graphics_card):
#         self.specs['Graphics Card'] = graphics_card
#
#     def add_hard_drive(self, hard_drive):
#         self.specs['Hard Drive'] = hard_drive
#
#     def add_motherboard(self, motherboard):
#         self.specs['Motherboard'] = motherboard
#
#     def add_screen_size(self, screen_size):
#         self.specs['Screen Size'] = screen_size
#
#     def get_specs(self):
#         return {self.model: self.specs}
#
# laptop = Laptop('Acer Nitro 5''\n')
# laptop.add_processor('Intel Core i7-9750H''\n')
# laptop.add_ram('16 GB DDR4''\n')
# laptop.add_graphics_card('NVIDIA GeForce GTX 1650''\n')
# laptop.add_hard_drive('512 GB SSD''\n')
# laptop.add_motherboard('Acer Nitro AN515-54-70KK''\n')
# laptop.add_screen_size('15.6-inch Full HD IPS display''\n')
# print(laptop.get_specs())

#Ex from presentation №2
# class DataParser:
#     def __init__(self, data_dict):
#         self.data = data_dict
#
#     def get_keys_tuple(self):
#         return tuple(self.data.keys())
#
#     def get_values_tuple(self):
#         return tuple(self.data.values())
#
#     def get_keys_list(self):
#         return list(self.data.keys())
#
#     def get_values_list(self):
#         return list(self.data.values())
#
#     def get_keys_set(self):
#         return set(self.data.keys())
#
#     def get_values_set(self):
#         return set(self.data.values())
#
# my_data_dict = {"name": "John", "age": 30, "city": "New York"}
# my_data_parser = DataParser(my_data_dict)
#
# keys_tuple = my_data_parser.get_keys_tuple()
# values_list = my_data_parser.get_values_list()
# keys_set = my_data_parser.get_keys_set()
#
# print(keys_tuple)
# print(values_list)
# print(keys_set)

#Ex from presentation №3
# class HotelData:
#     def __init__(self, data):
#         self.data = data
#
#     def get_hotel_names(self):
#         names = []
#         for hotel in self.data:
#             names.append(hotel['name'])
#         return names
#
#     def get_names_and_locations(self):
#         names = []
#         locations = []
#         for hotel in self.data:
#             names.append(hotel['name'])
#             locations.append(hotel['location'])
#         return {'names': names, 'locations': locations}
#
#     def add_status_id_to_markers(self):
#         for hotel in self.data:
#             for marker in hotel['markers']:
#                 marker['status_id'] = 1
#         return self.data
#
# data = [{'name': 'Hotel A', 'location': 'Location A', 'markers': [{'id': 1}, {'id': 2}]},
#         {'name': 'Hotel B', 'location': 'Location B', 'markers': [{'id': 3}, {'id': 4}]}]
#
# hotel_data = HotelData(data)
#
# print(hotel_data.get_hotel_names())
#
# print(hotel_data.get_names_and_locations())
#
# print(hotel_data.add_status_id_to_markers())
