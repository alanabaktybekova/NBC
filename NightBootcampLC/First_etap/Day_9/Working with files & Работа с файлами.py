# Exercise №1 & Пример №1
# a = open('people.txt', 'w')
#
# name = input('Введите имя -')
# a.write(name)
#
# a.close()
# a = open('people.txt', 'r')
# data = a.read()
# print(data)
# a.close()

# a = open('people.txt', 'w')
# with open('people.txt', 'r') as a:
#     print(a.read())
#     print('Открылся')
# print('Закрылся')

# Пример №2
# with open('users.txt', 'w') as a:
#     login = input()
#     password = input()
#     a.write(login + ' ' + password)

# Пример №3
# with open('3primer.txt', 'w') as text:
#     text = input('Введите текст: ')
#     print(text)
# if 'w' in text:
#     print('Да, в тексте есть w')
# else:
#     print('Нет, в тексте нет w')

# Пример №4
# with open('python.txt', 'w') as my_file:
#     enter = '''
#     Python is a widely used high-level programming language
#     for general-purpose programming, created by Guido van Rossum
#     and first released in 1991. An interpreted language, Python has
#     a design philosophy that emphasizes code readability (notably using
#     whitespace indentation to delimit code blocks rather than curly
#     brackets or kewords), and a syntax that allows programmers to
#     express concepts in fewer lines of code than might be used in languages such as C++ or Java.
#     '''
#     my_file.write(enter)
#
# with open('python.txt', 'r') as my_file:
#     data = my_file.read()
#
# r = data.split(' ')
# t_words = []
# for i in r:
#     if 't' in i:
#         t_words.append(i)
#     elif 'x' in i:
#         t_words.append(i)
#
# print(t_words)

# Пример №1
# a = 'dastan 123  ilan 123  ulan 321'
# with open('database.txt', 'w') as f:
#     f.write(a)
#
# with open('database.txt', 'r') as f:
#     data = f.read()
#
# users = data.split('  ')
# users1 = str(users)
# users2 = users1.split(' ')
# print(users2)
#
# login = input('Напишите логин - ')
# password = input('Введите пароль - ')
#
# for i in users2:
#     if login == i.split(' ')[0] and password == i.split(' ')[0]:
#         print('Пользователь сущ. пропишите пароль')
#         password1 = input('Введите пароль -')
#     elif login != i.split(' ')[0] and password != i.split(' ')[0]:
#         print('Не верный пароль')
#         password1 = input('Введите пароль ещё раз -')
#         while True:
#             if password1 == password and password1 == i.split(' ')[1]:
#                 print('Вы вошли')
#             else:
#                 print('Попробуй еще раз')
#             break
# with open('database.txt', 'a') as f:
#     f.write('  ' + login + ' ' + password)
#     print('Вы вошли успешна')

# Пример №1
# a = ['dastan 1234 ilan 4321 alana qwerty']
# with open('database1.txt1', 'r') as a:
#     a.read()
#     print(a)




