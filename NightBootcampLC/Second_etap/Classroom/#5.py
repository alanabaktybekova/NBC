# class Abonent:
#     def __init__(self, id, last_name, first_name, middle_name, address, credit_card_number, debit, credit, city_calls_time, calls_time):
#         self.id = id
#         self.last_name = last_name
#         self.first_name = first_name
#         self.middle_name = middle_name
#         self.address = address
#         self.credit_card_number = credit_card_number
#         self.debit = debit
#         self.credit = credit
#         self.city_calls_time = city_calls_time
#         self.calls_time = calls_time
#
#     def set_id(self, id):
#         self.id = id
#
#     def set_last_name(self, last_name):
#         self.last_name = last_name
#
#     def set_first_name(self, first_name):
#         self.first_name = first_name
#
#     def set_middle_name(self, middle_name):
#         self.middle_name = middle_name
#
#     def set_address(self, address):
#         self.address = address
#
#     def set_credit_card_number(self, credit_card_number):
#         self.credit_card_number = credit_card_number
#
#     def set_debit(self, debit):
#         self.debit = debit
#
#     def set_credit(self, credit):
#         self.credit = credit
#
#     def set_city_calls_time(self, city_calls_time):
#         self.city_calls_time = city_calls_time
#
#     def set_calls_time(self, calls_time):
#         self.calls_time = calls_time
#
#     def set_intercity_calls_time(self, intercity_calls_time):
#         self.intercity_calls_time = intercity_calls_time
#
#     def get_id(self):
#         return self.id
#
#     def get_last_name(self):
#         return self.last_name
#
#     def get_first_name(self):
#         return self.first_name
#
#     def get_middle_name(self):
#         return self.middle_name
#
#     def get_address(self):
#         return self.address
#
#     def get_credit_card_number(self):
#         return self.credit_card_number
#
#     def get_debit(self):
#         return self.debit
#
#     def get_credit(self):
#         return self.credit
#
#     def get_city_calls_time(self):
#         return self.city_calls_time
#
#     def get_calls_time(self):
#         return self.calls_time
#
#
#     def print_info(self):
#         print(f"Абонент {self.last_name} {self.first_name} {self.middle_name}")
#         print(f"Идентификационный номер: {self.id}")
#         print(f"Адрес: {self.address}")
#         print(f"Номер кредитной карточки: {self.credit_card_number}")
#         print(f"Дебет: {self.debit}")
#         print(f"Кредит: {self.credit}")
#         print(f"Время городских переговоров: {self.city_calls_time}")
#         print(f"Время междугородных переговоров: {self.intercity_calls_time}")
#
#     @staticmethod
#     def filter_by_city_calls_time(abonents, threshold):
#         result = []
#         for abonent in abonents:
#             if abonent.get_city_calls_time() > threshold:
#                 result.append(abonent)
#         return result
#
#     @staticmethod
#     def filter_by_intercity_calls(abonents):
#         result = []
#         for abonent in abonents:
#             if abonent.get_intercity_calls_time() > 0:
#                 result.append(abonent)
#         return result
#
#     @staticmethod
#     def sort_by_last_name(abonents):
#         return sorted(abonents, key=lambda abonent: abonent.get_last_name())
#
# abonent = Abonent('1234566', 'Baktybek', 'Imanbaev', 'satylganovich', 'lenuna st 139', '041348481', '17084', 'prostochel', '1234567')
# print(abonent.get_id())
# print(abonent.get_first_name())
# print(abonent.get_debit())
# print(abonent.get_last_name())
# print(abonent.get_city_calls_time())
# print(abonent.get_credit())
# print(abonent.get_address())
# print(abonent.get_calls_time())
# print(abonent.get_credit_card_number())
# print(abonent.get_middle_name())