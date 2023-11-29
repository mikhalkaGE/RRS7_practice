
# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number='17'):
#     return (f'  To: {mail}\n Приветствую, {name}!\n Вам назначен экзамен, который пройдет {date}, в {time}.\n По адресу: {place}.\n Экзамен будет проводить {teacher} в кабинете {number}.\n Желаем удачи на экзамене!')


# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))

#################################          JOIN METHOD          ##################################

# def concat(*args, sep = ' '):
#     return sep.join(map(str, args))

# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))


#####################################   palindrome    #############################################

# def is_palindrome(text):
#     text = ''.join(i for i in text if i.isalnum()).lower()
#     # print(text)
#     # print(text[::-1])
#     return text == text[::-1]

# print(is_palindrome('А роза упала на лапу Азора.'))
# print(is_palindrome('Gabler Ruby - burrel bag!'))
# print(is_palindrome('BEEGEEK'))


###################################  DAYS  ########################################

# def get_days(month):
#     days_in_month = {
#         1: 31,
#         2: 28,
#         3: 31,
#         4: 30,
#         5: 31,
#         6: 30,
#         7: 31,
#         8: 31,
#         9: 30,
#         10: 31,
#         11: 30,
#         12: 31
#     }
#     return days_in_month[month]

# print(get_days(1))
# print(get_days(2))
# print(get_days(9))


###############################################  FACTORS  ####################################################

# def number_of_factors(num):
#     factors = [i for i in range(1, num+1) if num % i == 0]
#     return len(factors)

# print(number_of_factors(1))
# print(number_of_factors(5))
# print(number_of_factors(10))
