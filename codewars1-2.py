
# https://www.codewars.com/kata/5302d846be2a9189af0001e4 --- Welcome to the City --- DONE
# https://www.codewars.com/kata/55225023e1be1ec8bc000390 --- Jenny's secret message --- DONE
# https://www.codewars.com/kata/563b74ddd19a3ad462000054 --- Stringy Strings --- DONE
# https://www.codewars.com/kata/56c22c5ae8b139416c00175d --- Job Matching #1 --- DONE
# https://www.codewars.com/kata/557b5e0bddf29d861400005d --- Miles per gallon to kilometers per liter --- DONE
# https://www.codewars.com/kata/56b29582461215098d00000f --- Lario and Muigi Pipe Problem --- DONE
# https://www.codewars.com/kata/57356c55867b9b7a60000bd7 --- Basic Mathematical Operations --- DONE
# https://www.codewars.com/kata/57280481e8118511f7000ffa --- Training JS #18: Methods of String object--concat() split() and its good friend join() --- DONE
# https://www.codewars.com/kata/57241e0f440cd279b5000829 --- Sum of Multiples --- DONE
# https://www.codewars.com/kata/58261acb22be6e2ed800003a --- Volume of a Cuboid --- DONE
# https://www.codewars.com/kata/58bf9bd943fadb2a980000a7 --- Who is going to pay for the wall? --- DONE
# https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b --- Reverse List Order --- DONE
# https://www.codewars.com/kata/5875b200d520904a04000003 --- Will there be enough space? --- DONE
# https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7 --- MakeUpperCase --- DONE
# https://www.codewars.com/kata/5601409514fc93442500010b --- How good are you really? -- DONE
# https://www.codewars.com/kata/5808e2006b65bff35500008f --- Find the position! -- DONE
# https://www.codewars.com/kata/57eae65a4321032ce000002d --- Fake Binary --- DONE
# https://www.codewars.com/kata/57e76bc428d6fbc2d500036d --- Convert a string to an array --- DONE

# def fake_bin(x):
#     return ''.join('0' if c < '5' else '1' for c in x)
# print(fake_bin('2344565'))

# def who_is_paying(name):
#     return [name] if len(name) <=2 else [name, name[:2]]
# print(who_is_paying("Mexico"))
# print(who_is_paying("Me"))
# print(who_is_paying(""))
# print(who_is_paying("I"))

# def sum_mul(n, m):
#     sum = 0
#     for i in range(n, m, n):
#         sum += i
#     return sum
# def sum_mul(n, m):
#     if n > 0 and m > 0:
#         return sum(range(n, m, n))
#     else:
#         return 'INVALID'
# print(sum_mul(2, 9))

# def split_and_merge1(string_, separator):
#     spl1 = string_.split()
#     print(spl1)
#     jn1 = [separator.join(list(i)) for i in spl1]
#     print(jn1)
#     return ' '.join(jn1)
# def split_and_merge(string_, separator):
#     return ' '.join(separator.join(i) for i in string_.split())
# print(split_and_merge("My name is John", "-"))
