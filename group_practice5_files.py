# def file_n_lines(file_name: str, n: int) -> None:
#     f = open(file_name)
#     rows = f.readlines()
#     return ''.join(rows[:n]).strip()
# def file_n_lines(file_name: str, n: int) -> None:
#     f = open(file_name)
#     for _ in range(n):
#         print(f.readline().strip())
# file_n_lines('population.txt', 3)



# def create_file_with_numbers(n):
#     with open(f'range_{n}.txt', 'w') as f:
#         for i in range(1,n+1):
#             f.write(str(i)+'\n')
# create_file_with_numbers(5)



# def longest_word_in_file(file_name: str) -> str:
#     with open(file_name, encoding = 'utf-8') as file:
#         max_len = 0
#         longest_w = ''
#         for i in file:
#             words = ''.join(j for j in i if j.isalnum() or j.isspace()).strip().split()
#             for w in words:
#                 if len(w) >= max_len:
#                     longest_w = w
#                     max_len = len(w)
#     return longest_w
# print(longest_word_in_file('test.txt'))




# with open('numbers.txt') as file:
#     three = 0
#     two = 0
#     for nums in file:
#         if len(nums.strip()) == 3:
#             three += 1
#         if len(nums.strip()) == 2:
#             two += int(nums)
#     print(f'{three},{two}')
# with open('numbers.txt') as f:
#     list=[*map(str.strip, f)]
#     three = len([*filter(lambda x: len(x)==3, list)])
#     two = sum(map(int, filter(lambda x: len(x)==2, list)))
#     print(f'{three},{two}')





# with open('population.txt') as file:
#     for row in file:
#         pop = (row.split('\t')[1]).strip()
#         if row[0] == 'G' and int(pop) > 500000:
#             print(row.strip())
        




with open('nums.txt') as file:
    # for line in file:
    #     lines = ''.join(j for j in line if j.isdigit() or j.isspace()).strip().split()
    #     sum = 0
    #     for j in lines:
    #         sum += int(j)
    # print(type(lines)) 
    s = 0
    c = '0'
    for i in file.read():
        if i.isdigit():
            c += i
        else:
            s += int(c)
            c = '0'
    print(s)



# import json
# str_json = {
#   "id": 123456,
#   "email": "user@example.com",
#   "username": "USERNAME",
#   "phone_number": "string"
# }
# with open('test.json', 'w') as file:
#     json.dump(str_json, file, indent=2)

# with open('test.json', 'r') as file:
#     data_from_json = json.load(file)
# print(data_from_json)
# print(data_from_json['id'])
# print(data_from_json['username'])
# print(data_from_json['email'])
