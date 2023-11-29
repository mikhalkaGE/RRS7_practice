# quoted_list = []
# def quotes(words):
#     for i in words.split():
#         i = f'"{i}"'
#         quoted_list.append(i)
#     return ' '.join(quoted_list)
# def quotes(words):
#     return ' '.join(f'"{i}"' for i in words.split())
# print(quotes('the world is mine take a look what you have started'))




# def del_palindrom(nums):
#     return ' '.join(str(i) for i in nums if str(i) != str(i)[::-1])
# print(del_palindrom([18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]))




# def sorted_tuples(numbers):
#     list = []
#     for i in numbers:
#         list.append(sum(i)/len(i))
#         list.sort(reverse=True)
#     return list
# print(sorted_tuples([(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]))

# def sorted_tuples(numbers):
#     return sorted(([sum(i)/len(i) for i in numbers]), reverse = True)
# print(sorted_tuples([(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]))



# def lowercase(i):
#     return i.lower()
# def order(text):
#     return ' '.join(sorted(text.split(), key = lambda i: i.lower()))
# print(order('cate Frog cat FROGs bee CATERS mouse cATwalk dolphin mOus Cats CatAlo'))




# import random
# def_list = ['basis', 'agree', 'baseBAll', 'chemicAL', 'agenda', 'bAr', 'aFTer', 'chicken', 'Chef', 'chemical', 'chief', 'CHIcken', 'child', 'baseball']
# def sorted_gematry(n):
#     list = random.sample(def_list, n)
#     return sorted(list, key = gematry)
    
# def gematry(i):
#     for i in list:
#         i.upper()
#         for j in range(len(i)):
#             ord(j) - 65

# print(sorted_gematry(4))