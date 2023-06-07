# import random
#
# class Unit:
#     def __init__(self, unit_id, team):
#         self.unit_id = unit_id
#         self.team = team
#
# class Soldier(Unit):
#     def follow_hero(self, hero):
#         print(f"Солдат {self.unit_id} следует за героем {hero.unit_id}")
#
# class Hero(Unit):
#     def __init__(self, unit_id, team, level=1):
#         super().__init__(unit_id, team)
#         self.level = level
#
#     def increase_level(self):
#         self.level += 1
#
# # Создаем героев и команды
# hero1 = Hero(1, "Team A")
# hero2 = Hero(2, "Team B")
#
# # Создаем списки солдат
# soldiers_team_a = []
# soldiers_team_b = []
#
# # Генерируем солдат и добавляем их в соответствующие списки
# for i in range(10):
#     soldier_team = random.choice(["Team A", "Team B"])
#     soldier = Soldier(i+1, soldier_team)
#     if soldier_team == "Team A":
#         soldiers_team_a.append(soldier)
#     else:
#         soldiers_team_b.append(soldier)
#
# # Выводим длину списков солдат
# print("Длина солдатских команд:")
# print(f"Team A: {len(soldiers_team_a)}")
# print(f"Team B: {len(soldiers_team_b)}")
#
# # Поднимаем уровень героя команды с более длинным списком
# if len(soldiers_team_a) > len(soldiers_team_b):
#     hero1.increase_level()
# else:
#     hero2.increase_level()
#
# # Отправляем одного из солдат первого героя следовать за ним
# soldier_to_follow = random.choice(soldiers_team_a)
# soldier_to_follow.follow_hero(hero1)
#
# # Выводим идентификационные номера героя и солдата
# print(f"Герой {hero1.unit_id} и солдат {soldier_to_follow.unit_id} готовы к бою!")