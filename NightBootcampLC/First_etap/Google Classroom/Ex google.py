# ex from google class room №Три последовательных числа
# x = int(input('Введите число - '))
# a = x
# b = x
# print('Это остальные числа от программы - ', x, a + 1, b + 2)

# ex from google class room №Арифметические операции
# x = int(input('Введите 1 число - '))
# a = int(input('Введите 2 число - '))
# b = print('Ваши введёные числа - ', x, 'и', a)
# print(x, '+', a, '=', x + a,)
# print(x, '-', a, '=', x - a,)
# print(x, '*', a, '=', x * a,)

# ex from google class room №Знакомство
# x = input('Здравствуйте!,давайте знакомится! - ')
# a = input('Ваша фамилия ? - ')
# b = input('Как вас зовут ? - ')
# c = input('Ваше отчество ? - ')
# d = input('Введите ваше возраст - ')
# e = input('Введите ваше пол - ')
# f = input('Введите ваше место работы - ')
# g = input('Введите ваше место учебы - ')
# h = input('На каком вы курс? - ')
# i = input('Введите ваше направление - ')
# j = input('Вы раньше изучали программирования ранее? - ')
# k = input('Какую вы хотите вашу будущью зарплату? - ')
# print('Хотите ли вы дружить?:', x, '\n', 'Фамилия:', a, '\n', 'Имя:', b, '\n', 'Отчество:', c, '\n', 'Возраст:', d,
#       '\n', 'Пол:', e, '\n', 'Место работы:', f, '\n', 'Место учебы:', g, '\n', 'Курс:', h, '\n', 'Направления:', i,
#       '\n', 'Знание о программирования:', j, '\n', 'Будущяя зарплата:', k, '\n')

# ex from google class room №Пароль
# a = input('Введите пароль - ')
# b = input('Введите пароль повторно - ')
# if a == b:
#     print('Пароль принят!')
# else:
#     print('Пароль не принят!')

# ex from google class room №Купе
# x=int(input('Напишите ваш номер места - '))
# if x <= 36:
#     print((x-1)//4+1, '- это ваш номер купе')
# elif x > 36:
#     print('Извините закончились места!')

# ex from google class room №Собеседования
# a = input('Какой язык программирования вы знаете? - ')
# b = input('Какой ваш возраст? - ')
# c = input('Какой ваш опыт? - ')
# d = input('Какую вы хотите зарплату? - ')
# if a == 'python':
#     print('Ok')
# elif b == 18 < 65:
#     print('Ok',b)
# elif c >= 3:
#     print('Ok', c)
# elif d <= 60000:
#     print('Ok', d)
# else:
#     print('Извините вы нам не подходите')

# ex from google class room №Описания ноутбука
# a = input('Напишите ваш модель ноутбука - ')
# b = input('На каком платформе был создан ваш ноутбук - ')
# c = input('Напишите какого году был выпущен ваш ноутбук - ')
# print('Ваша модель ноутбука - ', a)
# print('Ваш ноутбук использует платформу - ', b)
# print('Ваш ноутбук был выпущин в - ', c)

# ex from google class room №Расстояние в метрах
# a = int(input('Здравствуйте!, Я конветатор, я могу перевести с метров на сантиметры.Введите метры - '))
# b = a // 100
# print(b, ' - это в сантиметры')

# ex from google class room №Сама неотвратимость
# a = int(input('Населения - '))
# print((a + 1) // 2, 'Выжившие')

# ex from google class room №Номер в купе
# a = int(input('Напишите номер купе - '))
# if a <= 36:
#     print((a - 1) // 4 + 1, '- это ваш номер купе')
# elif a > 36:
#     print('Извините, но купе закончились')

# ex from google class room №Подсчет зарабной платы
# a = int(input('ЗП - '))
# b = int(input('оклад - '))
# c = int(input('ДК - '))
# d = int(input('ДФ - '))
# e = int(input('премии - '))
# f = int(input('налог - '))
# g = int(input('удержания - '))
# print((b/c * d + e) * ((100 - f) / 100) - g)

# ex from google class room №Четное и не четное
# a = int(input('Напишите число - '))
# if a % 2 == 0:
#     print(a, '- Это четное число')
# else:
#     print(a, '- Это не четное число')

# ex from google class room №Соотношения
# a = int(input('Напишите число  - '))
# if (a // 1000) + (a % 10) == ((a % 1000) // 100) - ((a % 100) // 10):
#    print("Да")
# else:
#    print("Нет")

# ex from google class room №Четырехзначное число
# a = int(input('Введите 1 число - '))
# b = int(input('Введите 2 число - '))
# c = int(input('Введите 3 число - '))
# x = int(input('Введите 4 число - '))
# if (a < b) and (a < c) and (a < x):
#     print(a)
# if (b < a) and (b < c) and (b < x):
#     print(b)
# if (c < a) and (c < b) and (c < x):
#     print(c)
# else:
#     print(x, '- Это наименьшее число')

# ex from google class room №Ход Короля
# x1 = int(input('Напишите 1 число от 1 до 8 для первой клетки - '))
# y1 = int(input('Напишите 2 число от 1 до 8 для второй клетки - '))
# x2 = int(input('Напишите 3 число от 1 до 8 - '))
# y2 = int(input('Напишите 4 число от 1 до 8 - '))
# if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
#     print('YES')
# else:
#     print('NO')

# ex from google class room №Ход Короля
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a - c == 1:
#     print('YES')
# elif c - a == 1:
#     print('YES')
# elif b - d == 1:
#     print('YES')
# elif d - b == 1:
#     print('YES')
# else:
#     print('NO')

# ex from google class room №Котлета
# k = int(input('Сколько котлет надо - '))
# m = int(input('Сколько нужно минут чтобы обжарить котлету со всех сторон - '))
# n = int(input('За какое наименьшее время нужно поджарить с обеих сторон котлет - '))
# if n <= k:
#   t = 2 * m
# elif n * 2 % k == 0:
#     t = m * (n * 2 // k)
# else:
#     t = m * (1 + (n * 2 // k))
# print(t, '- надо столько времени чтобы пожарить котлету')

# New ex googleclassroom
# ex from google class room №while 1
# a = 0
# b = 0
# while a < 1000:
#     a = b
#     b += 1
#     print(a)

# ex from google class room №while 2
# n = int(input('Введите число - '))
# while n > 100:
#     n = int(input(n, '- Это число больше 100'))
# print(n)

# ex from google class room №2 #1
# a = 'Nazar'
# for i in range(10):
#     print(a)

# ex from google class room №2 #2
# for i in range(1, 101):
#     print(i)

# ex from google class room №2 #3
# for i in range(1, 101):
#     if i // 4:
#         print(i)

# ex from google class room №3
# a = int(input('Сколько хотите накопить? - '))
# b = 0
# while b < a:
#     c = int(input('Взнос: '))
#     d = int(input('Взнос: '))
#     e = int(input('Взнос: '))
#     b += c + d + e
#     print('Поздравляю! Вы накопили ', b, 'сомов!')

# ex from google class room №4

# ex from google class room №only even number
# for i in range(10):
#     print(input('Введите число - '))
#     if i % 2:
#         print('YES')
#     else:
#         print('NO')

# ex from google class room №6
# print('*')
# print('*', '*')
# print('*', '*', '*')
# print('*', '*', '*', '*')
# print('*')
# print('*', '*')
# print('*', '*', '*')
# print('*', '*', '*', '*')
# print('*', '*', '*', '*', '*')
# print('*', '*', '*', '*', '*', '*')
# print('*', '*', '*', '*', '*', '*', '*')
# print('*', '*', '*', '*', '*', '*', '*', '*')

# ex from google classroom Numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers)

# № ex 0
# text = """
# The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
# Simple is better than complex.Complex is better than complicated.
# Flat is better than nested.Sparse is better than dense.
# Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
# Errors should never pass silently.Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one--and preferably only onUP,BROADCAST,RUNNING,MULTICASTe --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea --let's do more of those!
# """

# a = str(text)
# for i in a:
#      if a.istitle():
#         print(i)

# № ex 1
# with open('The Zen of Python.txt', 'w')as a:
#     b = input('Напишите текст про Python - ')
#     a.write(b)
#
# def reader():
#     if 'c' in a













