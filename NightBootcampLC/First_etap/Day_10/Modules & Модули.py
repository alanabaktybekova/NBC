#Ex 1
# import random
# students = [
#     'Alana','Ilan', 'Nazar', 'Baha' 'Alana', 'Ilan', 'Matvey', 'Artem',
#     'Ernest', 'Sonun', 'Sarynji', 'Cholpon',
#     'Aichurek', 'Dastan'
# ]
# for i in range(9):
#     student = random.choice(students)
#     print(student)
#     students.remove(student)
#     a = input()
#
#
# print(students)

# Ex 2
# import random
# try:
#     correct_answer = 0
#     wrong_answer = 0
#     a = 1
#     a1 = int(input('Здравствуйте! Давайте поиграем в таблицу умножения. Если вы хотите начать напишите цифру "1" - '))
# while a1 == a:
#     # решение с +
#     number = int(input('Напишите самое наибольшее значение - '))
#     number1 = random.randint(0, number)
#     number2 = random.randint(0, number)
#     answer = number1 + number2
#     answer1 = int(input('Напишите ответ - ' + str(number1) + '+' + str(number2) + '=' + '?'))
#     if answer1 == answer:
#         print('Молодец ты еще наверное учишься в школе! Правильно')
#     else:
#         print('Сразу видно что ты уже закончил школу! Не правильно')
#     # решение с *
#     number = int(input('Напишите самое наибольшее значение - '))
#     number1 = random.randint(0, number)
#     number2 = random.randint(0, number)
#     answer = number1 * number2
#     answer1 = int(input('Напишите ответ - ' + str(number1) + '*' + str(number2) + '=' + '?'))
#     if answer1 == answer:
#         print('Молодец ты еще наверное учишься в школе! Правильно')
#     else:
#         print('Сразу видно что ты уже закончил школу! Не правильно')
#
#     # решение с /
#     number = int(input('Напишите самое наибольшее значение - '))
#     number1 = random.randint(0, number)
#     number2 = random.randint(0, number)
#     answer = number1 / number2
#     answer1 = int(input('Напишите ответ - ' + str(number1) + '/' + str(number2) + '=' + '?'))
#     if answer1 == answer:
#         print('Молодец ты еще наверное учишься в школе! Правильно')
#     else:
#         print('Сразу видно что ты уже закончил школу! Не правильно')
#
#     # решение с -
#     number = int(input('Напишите самое наибольшее значение - '))
#     number1 = random.randint(0, number)
#     number2 = random.randint(0, number)
#     answer = number1 - number2
#     answer1 = int(input('Напишите ответ - ' + str(number1) + '-' + str(number2) + '=' + '?'))
#     if answer1 == answer:
#         correct_answer += 1
#         print('Молодец ты еще наверное учишься в школе! Правильно')
#     else:
#         wrong_answer += 1
#         print('Сразу видно что ты уже закончил школу! Не правильно')
#
#
#     print('Правильные ответов - ', correct_answer, 'Не правильно - ', wrong_answer)
# expet:


