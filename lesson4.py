######################    HW    ########################
# Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа): 
#      периметр квадрата, площадь квадрата и диагональ квадрата.

# import math
# a = int(input('Enter lenth: '))
# def square(a):
#     return {4*a, a*a, math.sqrt(2)*a}
# print(square(a))






# Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно 
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35 
# 	position: web developer

# def person(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
# person(name='John', last_name = 'Smith', age = 35, position = 'web developer')






# Используя лямбда-выражение, из списка  создайте новый список, содержащий только 
#      положительные числа
# Используя лямбда выражение, получите результат перемножения значений в предыдущем списке

# my_list = [20, -3, 15, 2, -1, -21]

# new_list = []
# for i in my_list:
#     if i>0:
#         new_list.append(i)

# new_list = list(filter(lambda x: x>0, my_list))
# print(new_list)

# from functools import reduce
# print(reduce(lambda x, y: x*y, my_list))








# Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра

# import time

# def time_decorator(func):
#     def wrapper(*args):
#         start = time.perf_counter()
#         result = func(*args)
#         end = time.perf_counter()
#         exec_time = end - start
#         print(f'{func.__name__} execution time is: {exec_time}')
#         return result
#     return wrapper

# @time_decorator
# def greeting(name):
#     print(f'Hello, {name}')

# greeting('batono')
