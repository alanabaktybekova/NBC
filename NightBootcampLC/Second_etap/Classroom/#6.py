# class Airplane:
#     def __init__(self, make, model, year, max_speed):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer =  0
#         self.is_flying = False
#
#     def take_off(self):
#         self.is_flying = True
#         print('Самолёт взлетает')
#
#     def fly(self, distance):
#         if self.is_flying:
#             self.odometer += distance
#             print(f'Самолет улетел {distance} km. Общее расстояние полета составляет {self.odometer} km.')
#         else:
#             print('Самолет не может летать, пока не взлетит.')
#
#     def land(self):
#         if self.is_flying:
#             self.is_flying = False
#             print('Самолет садится.')
#         else:
#             print('Самолет уже на земле.')
#
# my_plane = Airplane(make='Boing', model='345', year='2020', max_speed=965)
#
# my_plane.take_off()
# my_plane.fly(1000)
# my_plane.fly(500)
# my_plane.land()

