# 1
# class Student:
#     def __init__(self, name, group):
#         self.name = name
#         self.group = group
#
#     def show(self):
#         return f"Студент {self.name} из группы {self.group}"
#
#     def __del__(self):
#         print(f"Экземпляр класса Student для студента {self.name} удален")
#
# student1 = Student("Иванов Иван", "Группа 1")
# print(student1.show())
#
# del student1

# 2
# class Student:
#     def __init__(self, name, conf):
#         self.name = name
#         self.lab_results = [-1] * conf['lab_num']
#         self.exam_result = 0
#         self.conf = conf
#
#     def make_lab(self, m, n = None):
#         if n is None:
#             n = self.lab.results.index(-1)
#         if n >= self.conf['lab_num']:
#             return self
#         self.lab_results[n] = min(m, self.conf['lab_max'])
#         return self
#
#     def make_exam(self, m):
#         self.exam_result = min(m, self.conf['exam_max'])
#         return self
#
#     def is_certifid(self):
#         lab_sum = sum(max(0, res) for res in self.lab_results)
#         exam_otvet = self.exam_result
#         total_otvet = lab_sum + exam_otvet
#         min_otvet = self.conf['k'] * (self.conf['lab_max'] * self.conf['lab_num'] + self.conf['exam_max'])
#         return total_otvet, total_otvet >= min_otvet
#
# studen = Student('Alana', 96)
# print(studen.make_exam())


