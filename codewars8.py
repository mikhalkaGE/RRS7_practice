# https://www.codewars.com/kata/585d7d5adb20cf33cb000235 --- CHITTED
# def find_uniq(arr):
#     a, b = set(arr)
#     if arr.count(a) == 1:
#         return a
#     return b

# print(find_uniq([ 1, 1, 1, 2, 1, 1 ])) # 2







# https://www.codewars.com/kata/586560a639c5ab3a260000f3 --- CHITTED
# def rotate(str_):
#     arr = []
#     temp = ''
#     for i in range(len(str_)):
#         temp = str_[i+1:] + str_[:i+1]
#         arr.append(temp)
#     return arr

# print(rotate("Hello")) # ["elloH", "lloHe", "loHel", "oHell", "Hello"]







# https://www.codewars.com/kata/57fafb6d2b5314c839000195 --- DONE
# import re
# def remove(s):
#     res = []
#     for i in s.split():
#         if len(re.findall(r'!', i))!=1:
#             res.append(i)
#     return ' '.join(res)

#     return ' '.join(i for i in s.split() if len(re.findall(r'!', i))!=1)

#     return ' '.join(i for i in s.split() if i.count('!')!=1)

# print(remove('!!!Hi !!hi!!! !hi')) # '!!!Hi !!hi!!!'






# https://www.codewars.com/kata/59f70440bee845599c000085
# https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3
# https://www.codewars.com/kata/628df6b29070907ecb3c2d83
# https://www.codewars.com/kata/5a86073fb17101e453000258
# https://www.codewars.com/kata/59269e371a640c0e98000085
# https://www.codewars.com/kata/590c4c342ad5cd6a8700005c
# https://www.codewars.com/kata/5442e4fc7fc447653a0000d5
# https://www.codewars.com/kata/58bf67eb68d8469e3c000041
# https://www.codewars.com/kata/58c20c8d61aefc518f0000fd
# https://www.codewars.com/kata/6344701cd748a12b99c0dbc4
# https://www.codewars.com/kata/55f347cfb44b879e1e00000d



# ###############       Re        #####################
# https://www.codewars.com/kata/5637b03c6be7e01d99000046 --- CHITTED 
# import re
# def make_password(phrase):
#     chng_dict = {'i': '1', 'I': '1', 's': '5', 'S': '5', 'o': '0', 'O': '0'}

    # passw = ''
    # x = phrase.split()
    # for i in x:
    #     passw += i[0]

    # passw = ''.join(i[0] for i in phrase.split())

    # for k, v in chng_dict.items():
    #     passw = passw.replace(k, v)
    # return passw


    # pattern = r'\b\w'
    # str1 = ''.join(re.findall(pattern, phrase))
    # passw = re.sub(r'[iI]', '1', str1)
    # passw = re.sub(r'[sS]', '5', passw)
    # passw = re.sub(r'[oO]', '0', passw)
    # return passw

# print(make_password("Give me liberty or give me death")) # "Gml0gmd"
# print(make_password("Keep Calm and Carry On")) # "KCaC0"








# https://www.codewars.com/kata/56a24b309f3671608b00003a --- CHITTED

# import re
# def dad_filter(string):
#     return (re.sub(r',+', ',', string)).strip().rstrip(',')


# print(dad_filter("all this,,,, used to be trees,,,,,,        ")) # "all this, used to be trees"






# https://www.codewars.com/kata/552e45cc30b0dbd01100001a

# import re
# def zipvalidate(postcode):
#     pattern = r'[12346]\d{5}'
#     return bool(re.fullmatch(pattern, postcode))

# print(zipvalidate('198328@@')) # False




# https://www.codewars.com/kata/56a24b4d9f3671584d000039
# https://www.codewars.com/kata/563a8656d52a79f06c00001f
# https://www.codewars.com/kata/56d31aaefd3a52902a000d66
# https://www.codewars.com/kata/52fba66badcd10859f00097e
# https://www.codewars.com/kata/55d410c492e6ed767000004f
# https://www.codewars.com/kata/585a36b445376cbc22000072
# https://www.codewars.com/kata/51f2b4448cadf20ed0000386
# https://www.codewars.com/kata/55f91a98db47502cfc00001b
# https://www.codewars.com/kata/62cb487e43b37a5829ab5752
