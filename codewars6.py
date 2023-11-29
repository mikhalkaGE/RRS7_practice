
##################### Regular Expressions (RegEx) #####################

# https://www.codewars.com/kata/56a946cd7bd95ccab2000055 --- DONE

import re

# def lowercase_count(strng):
#     x = re.findall('[a-z]', strng)
#     return len(x)
# print(lowercase_count("abcABC123"))





# https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023 --- DONE

# def validate_usr(username):
#     x = re.findall('^[a-z0-9_]{4,16}$', username)     # return re.match('^[a-z0-9_]{4,16}$', username) is not None
#     if x:
#         return True
#     else:
#         return False
# print(validate_usr('sdf567'))





# https://www.codewars.com/kata/567bf4f7ee34510f69000032 --- DONE

# def is_digit(n):
#     return re.fullmatch('\d', n) is not None






# https://www.codewars.com/kata/55960bbb182094bc4800007b --- CHITTED

# def insert_dash(num):
#     return re.sub('([13579])(?=[13579])', r'\1-', str(num))

# print(insert_dash(6134547632))
# print(insert_dash(137589957356))





# https://www.codewars.com/kata/55968ab32cf633c3f8000008 --- 

# def initials(name):
#     # return re.findall(r'\b\w|(?<=\s)\w', name)

#     arr = name.split()
#     initial = ''
#     for i in range(len(arr)-1):
#         initial += arr[i][0].upper() + '.'
#     return initial + arr[-1].title()

# print(initials('Barack hussein wefgewg rhtrhweg rewgwe obama')) # ---> 'B.H.Obama'








# https://www.codewars.com/kata/559e5b717dd758a3eb00005a
# https://www.codewars.com/kata/55b051fac50a3292a9000025
# https://www.codewars.com/kata/55ccdf1512938ce3ac000056
# https://www.codewars.com/kata/56a25ba95df27b7743000016
