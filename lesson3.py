########################################  LIST  ##########################################

# lst = [10, 'Hello', None, True, 25, 36.6]
# print(lst[1])
# print(lst[-5])
# print(len(lst))
# text = 'Bye'
# lst.append(text)
# print(lst)


# lst2 = []
# for i in lst:
#     if isinstance(i, int):
#         lst2.append(i)
# print(lst2)
# print(sum(lst2))


# lst = [1, 2, 3, 4, 5, 6]
# lst2 = []
# for num in lst:
#     if num%2 == 0:
#         lst2.append(num**2)
# print(lst2)
# lst3 = [num**2 for num in lst if not num%2]
# print(lst3)


###########################################  TUPLES  ################################################

# my_tuple = 1, 2, 3
# my_tuple2 = ('lemon', 'apple', 'cherry')
# my_tuple3 = ('mango')
# print(type(my_tuple))
# print(type(my_tuple2))
# print(type(my_tuple3))

# def sum_it(*args):
#     return sum(args)

# print(sum_it(1, 3, 5))


##############################################  SET  ###############################################

# set1 = {1, 2, 3, 'one', 'ten'}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# set3 = {1, 2, 3}

# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))
# set1.remove(1)
# print(set1)
# set1.add(89)
# print(set1)


#########   HW   ###########

        # Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2][0])
# print(my_list[2][1])
# print(my_list[2][2])
# final_list = my_list[2]
# print(final_list)
# print(*final_list)
# print(*final_list, sep='\n')
# print(' '.join(map(str, final_list)))
# print(' '.join(str(i) for i in final_list))




#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print(sum(i for i in list_1 if isinstance(i, int)))
# print(*(i for i in list_1 if isinstance(i, str) and 'a' in i), sep=', ')



# Превратите лист в кортеж
# lst = ['cat', 'dog', 'horse', 'cow']
# tup = tuple(lst)
# print(tup)



# Напишите программу, которая определяет, какая семья больше. 
#       1) Программа имеет два input() - например, family_1, family_2. 
#       2) Членов семьи нужно перечислить через запятую. 
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

# family_1 = tuple(input('Family one is: ').split(','))
# family_2 = tuple(input('Family two is: ').split(','))
# # print(family_1, family_2)
# if len(family_1)>len(family_2):
#     print(*family_1)
# elif len(family_1) == len(family_2):
#     print('EQUAL')
# else:
#     print(*family_2)





# Найдите сумму всех значений в словаре 
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))

# res = 0
# for i in my_dictionary:
#     res += my_dictionary[i]
# print(res)





# Удалите повторяющиеся значения из списка 
# lst = [1, 2, 3, 4, 5, 3, 2, 1]
# print(set(lst))





# Даны два множества: 
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга 
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set2.intersection(set1))
# print(set2.symmetric_difference(set1))
# print(set1.issubset(set2))
# print(set2.issubset(set1))
