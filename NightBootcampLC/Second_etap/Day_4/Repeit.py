# class Phone:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         return f'phone - {self.name}'
#
#
# class SmartPhone(Phone):
#     def __init__(self, name, camera):
#         super().__init__(name)
#         self.camera = camera
#
#     def photo(self):
#         return 'Снимок сделан'
#
#     def info(self):
#         return f'Phone - {self.name}\nCamera - {self.camera}'
#
#
# class Iphone(SmartPhone):
#     def __init__(self, name, camera, internet):
#         super().__init__(name, camera)
#         self.internet = internet
#
#     def change_name(self, new_name):
#         self.name = new_name

# Work from presentatoin
# class HotelMarkers:
#     def __init__(self, data):
#         self.data = data
#
#     def get_hotel_names(self):
#         return [hotel['NAME'] for hotel in self.data['MARKERS']]
#
#     def get_hotel_data(self):
#         names = [hotel['NAME'] for hotel in self.data['MARKERS']]
#         locations = [hotel['POSITION'] if 'POSITION' in hotel else hotel['LOCATION'] for hotel in self.data['MARKERS']]
#         return {'names': names, 'locations': locations}
#
#     def add_status_id(self, status_id):
#         for hotel in self.data['MARKERS']:
#             hotel['status_id'] = status_id
#
# data = {
#     "MARKERS": [
#         {
#             "NAME": "RIXOS THE PALM DUBAI",
#             "POSITION": [25.1212, 55.1535],
#         },
#         {
#             "NAME": "SHANGRI-LA HOTEL",
#             "LOCATION": [25.2084, 55.2719]
#         },
#         {
#             "NAME": "GRAND HYATT",
#             "LOCATION": [25.2285, 55.3273]
#         }
#     ]
# }
#
# hotel_markers = HotelMarkers(data)
#
# # Получение всех имен отелей
# print(hotel_markers.get_hotel_names()) # ['RIXOS THE PALM DUBAI', 'SHANGRI-LA HOTEL', 'GRAND HYATT']
#
# # Получение всех данных об отелях
# print(hotel_markers.get_hotel_data()) # {'names': ['RIXOS THE PALM DUBAI', 'SHANGRI-LA HOTEL', 'GRAND HYATT'], 'locations': [[25.1212, 55.1535], [25.2084, 55.2719], [25.2285, 55.3273]]}
#
# # Добавление поля status_id
# hotel_markers.add_status_id(1)
# print(data)

# Work from presentation 2
# class Factory:
#     def engine(self):
#         return "Двигатель создан"
#
#     def bridge(self):
#         return "Ходовая часть создана"
#
#
# class Toyota(Factory):
#     def wheels(self):
#         return "Колёса готовы"
#
#     def windows(self):
#         return "Стёкла готовы"
#
#
# toyota = Toyota()
# results = []
# results.append(toyota.engine())
# results.append(toyota.bridge())
# results.append(toyota.wheels())
# results.append(toyota.windows())
#
# print(results)

