
# https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd --- Beginner Series #1 School Paperwork --- DONE
# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe --- Even or Odd --- DONE
# https://www.codewars.com/kata/5f70c883e10f9e0001c 89673 --- Gravity Flip --- DONE
# def flip(d, a):
#     a.sort()
#     return a if d=='R' else a[::-1]
# def flip(d,a):
#     return sorted(a, reverse = d == 'L')
# print(flip('L', [3, 2, 1, 2]))

# https://www.codewars.com/kata/55a996e0e8520afab9000055 --- Who ate the cookie? --- DONE
# def cookie(x):
#     if type(x) == str:
#         name = 'Zach'
#     elif type(x) == bool:
#         name = 'the dog'
#     elif type(x) == float or int:
#         name = 'Monica'
#     return f'Who ate the last cookie? It was {name}!'
# def cookie(x):
#     return f"Who ate the last cookie? It was {'the dog' if isinstance(x, bool) else 'Zach' if isinstance(x, str) else 'Monica'}!"
# print(cookie("Ryan"))
# print(cookie(1))
# print(cookie(2.8))
# print(cookie(True))

# https://www.codewars.com/kata/56dae9dc54c0acd29d00109a --- Grasshopper - Function syntax debugging --- DONE
# https://www.codewars.com/kata/53dc23c68a0c93699800041d --- Sentence Smash --- DONE
# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c --- A Needle in the Haystack --- DONE
# https://www.codewars.com/kata/57089707fe2d01529f00024a --- Grasshopper - If/else syntax debug --- DONE
# https://www.codewars.com/kata/55b1fd84a24ad00b32000075 --- Selective fear of numbers --- DONE
# def am_I_afraid(day,num):
#     return {
#         'Monday':  num == 12,
#         'Tuesday': num > 95,
#         'Wednesday': num == 34,
#         'Thursday': num == 0,
#         'Friday': num % 2 == 0,
#         'Saturday': num ==  56,
#         'Sunday': num == 666 or num == -666,
#     }[day]
# print(am_I_afraid('Monday', 13))

# https://www.codewars.com/kata/54530f75699b53e558002076 --- NATO Phonetic Alphabet --- DONE
# LETTERS is preloaded
# LETTERS = {}  
# def nato(word):
#     lst = []
#     for i in word.upper():
#         lst.append(LETTERS.get(i))
#     return ' '.join(lst)
# def nato(word):
#     return ' '.join(LETTERS[i] for i in word.upper())

# https://www.codewars.com/kata/59b0a6da44a4b7080300008a --- Converting 12-hour time to 24-hour time --- DONE
# def to24time(hour, minute, period):
#     if period == 'am':
#         if hour == 12:
#             hour = 0
#     else:
#         if hour != 12:
#             hour += 12
#     return f'{hour:02}{minute:02}'
# def to24time(hour, minute, period):
#     return f'{hour % 12 + (period == "pm") * 12:02}{minute:02}'
    # def to24time(hour, minute, period):
    #     if period == 'pm' and 0 < hour < 12: hour += 12
    #     elif period == 'am' and hour == 12: hour = 0
    #     return f'{hour:02d}{minute:02d}'
# print(to24time( 1,  0, 'am'), '0100')
# print(to24time( 1,  0, 'pm'), '1300')
# print(to24time(12,  0, 'am'), '0000')
# print(to24time(12,  0, 'pm'), '1200')
# print(to24time( 6, 30, 'am'), '0630')
# print(to24time( 9, 45, 'pm'), '2145')

# https://www.codewars.com/kata/5390bac347d09b7da40006f6 --- Jaden Casing Strings --- DOME
# def to_jaden_case(string):
#     str = string.split()
#     str_cap = [i.capitalize() for i in str]
#     return ' '.join(str_cap)
# def to_jaden_case(string):
#     return ' '.join(word.capitalize() for word in string.split())
# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

# https://www.codewars.com/kata/559e5b717dd758a3eb00005a --- Dropcaps --- DONE
# def drop_cap(words):
#     return " ".join(i.capitalize() if len(i)>2 else i for i in words.split(" "))
# print(drop_cap('   space WALK   '))

# https://www.codewars.com/kata/583df40bf30065fa9900010c --- The mean of two means --- DONE
# https://www.codewars.com/kata/55b051fac50a3292a9000025 --- Filter the number --- DONE
# def filter_string(string):
#     lst = []
#     for i in string:
#         lst.append(i)
#     return int(''.join(j for j in lst if j.isnumeric()))
# def filter_string(string):
#     return int(filter(str.isdigit, string))
# def filter_string(string):
#     return int(''.join(j for j in string if j.isdigit()))
# print(filter_string("a1b2c3"))

# *
# https://www.codewars.com/kata/64c7bbad0a2a00198657013d --- Reverse sublists of even numbers --- CHEATING!!!!
# def rev_sub(arr):
#     result = []
#     i = 0
#     while i < len(arr):
#         if arr[i] % 2 == 0:  # Check if the current element is even
#             j = i
#             while j < len(arr) and arr[j] % 2 == 0:
#                 j += 1
#             result.extend(reversed(arr[i:j]))  # Reverse and add the sublist
#             i = j
#         else:
#             result.append(arr[i])  # Add odd numbers directly
#             i += 1
#     return result


