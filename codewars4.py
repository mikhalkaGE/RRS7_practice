
# https://www.codewars.com/kata/56576f82ab83ee8268000059 --- Running out of space --- DONE
# def spacey(array):
#     new = []
#     for i in range(len(array)):
#         new.append(''.join(array[:i+1]))
#     return new
# def spacey(array):
#     return [''.join(array[:i+1]) for i in range(len(array))]
# print(spacey(['kevin', 'has','no','space']))

# https://www.codewars.com/kata/58640340b3a675d9a70000b9 --- All Star Code Challenge #3 --- DONE
# def remove_vowels(strng):
#     return ''.join(i for i in strng if i not in 'aeiou')
# print(remove_vowels('wefwegnjier'))

# https://www.codewars.com/kata/5168b125faced29f66000005 --- Return substring instance count --- DONE
# def solution(full_text, search_text):
#     return full_text.count(search_text)
# print(solution('ccddeeccddeecc', 'cc'))

# https://www.codewars.com/kata/54ff3102c1bad923760001f3 --- Vowel Count --- DONE
# def get_count(sentence):
#     count = 0
#     for i in sentence:
#         if i in "aeiou":
#             count += 1
#     return count
# def get_count(sentence):
#     return sum(c in 'aeiou' for c in sentence)
# def get_count(sentence):
#     return sum(1 for i in sentence if i in "aeiou")
# print(get_count('cjcycftidyoiaoiao'))

# https://www.codewars.com/kata/55d6a0e4ededb894be000005 --- The old switcheroo 2 -- DONE
# abc = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'e': 5,
#     'f': 6,
#     'g': 7,
#     'h': 8,
#     'i': 9,
#     'j': 10,
#     'k': 11,
#     'l': 12,
#     'm': 13,
#     'n': 14,
#     'o': 15,
#     'p': 16,
#     'q': 17,
#     'r': 18,
#     's': 19,
#     't': 20,
#     'u': 21,
#     'v': 22,
#     'w': 23,
#     'x': 24,
#     'y': 25,
#     'z': 26
# }
# def encode(string):
#     return ''.join(str(abc[i]) if i.isalpha() else i for i in string.lower())
# def encode(string):
#     num = ''
#     for i in string.lower():
#         if i.isalpha():
#             num += str(ord(i)-96)
#         else:
#             num += i
#     return num
# def encode(string):
#   return ''.join(str(ord(i)-96) if i.isalpha() else i for i in string.lower())
# print(encode('abc-#@5'))

# https://www.codewars.com/kata/586e1d458cb711f0a800033b --- Thinkful - List and Loop Drills: Lists of lists --- DONE
# def process_data(data):
#     res = 1
#     res_list = []
#     for i in data:
#         subs = i[0] - i[1]
#         res_list.append(subs)
#     for j in res_list:
#         res *= j
#     return res
# def process_data(data):
#     res = 1
#     for i in data:
#         res *= i[0] - i[1]
#     return res
# print(process_data([[2, 5], [3, 4], [8, 7]]))

# https://www.codewars.com/kata/58659b1261cbfc8bfc00020a --- Thinkful - Logic Drills: Graceful addition --- DONE
# https://www.codewars.com/kata/585a29183d357b31f700023f --- Thinkful - String Drills: Jedi name --- DONE
# https://www.codewars.com/kata/5a87449ab1710171300000fd --- Tidy Number (Special Numbers Series #9) --- 
# https://www.codewars.com/kata/55805ab490c73741b7000064 --- makeBackronym --- DONE
# #preloaded variable: "dictionary"
# def make_backronym(acronym):
#     bac = []
#     for i in acronym:
#         bac.append(dictionary[i.upper()])
#     return ' '.join(bac)
# def make_backronym(acronym):
#     return ' '.join(dictionary[i.upper()] for i in acronym)

# https://www.codewars.com/kata/57fcaed83206fb15fd00027a --- Replace every nth --- DONE
# def replace_nth(text, n, old_value, new_value):
#     new_text = []
#     count = 0
#     for i in text:
#         if i == old_value and n > 0:
#             count += 1
#             if count % n == 0:
#                 new_text.append(new_value)
#             else: new_text.append(i)
#         else:
#             new_text.append(i)
#     return ''.join(new_text)

# https://www.codewars.com/kata/581f4ac139dc423f04000b99 --- Transpose two strings in an array --- DONE
# from itertools import zip_longest
# def transpose_two_strings(arr):
#     pairs = list(zip_longest(arr[0], arr[1], fillvalue=" "))
#     return '\n'.join([' '.join(pair) for pair in pairs])
# from itertools import zip_longest
# def transpose_two_strings(lst):
#     return "\n".join(f"{a} {b}" for a, b in zip_longest(*lst, fillvalue=" "))

# *
# https://www.codewars.com/kata/64cac86333ab6a14f70c6fb6
# https://www.codewars.com/kata/63b84f54693cb10065687ae5