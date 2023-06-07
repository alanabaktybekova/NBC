# № Exsemple
# def send_welcome():
#     text = '''Здравствуй человей
# Я рад тебя видеть'''
#     print(text)
# send_welcome()

# №1
# list_1 = ['name', 'age', '1', '19']
#
#
# def reverse_list():
#     my_list1 = list_1[0:len(list_1)//2]
#     my_list2 = list_1[len(list_1)//2:len(list_1)]
#     total = my_list1[::-1] + my_list2[::-1]
#     print(total)
#
# reverse_list()

# №2
# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
# print(list(fib(10)))

# №3
# a = int(input('Первое число - '))
# b = int(input('Вторая числа - '))
# def sloshenie():
#     c = a + b
#     print('Ответ: ', c)
#     return c
# sloshenie()
#
# def vychitanye():
#     c = a - b
#     print('Ответ: ', c)
#     return c
#
# vychitanye()
#
# def obshee():
#     d = sloshenie()
#     e = vychitanye()
#     f = d, e
#     print(f)
#     return f
#
# obshee()

# №1
# a = input('Как вы хотите назвать новый файл - ')
# def foo(fname):
#     stri = input("Вводите строку")
#     with open(fname, "w") as fout:
#         fout.write(stri + "\n")
#     with open(fname, "r") as finp:
#         for st in finp:
#             print(st, end='')
# foo

# №2
# from random import randint
# def gen_number():
#     code = '0444'
#     code1 = int(code)
#     code2 = randint(111111,999999)
#     print(code1, code2[3:])
#
# gen_number()


