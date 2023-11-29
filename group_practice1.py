# while True:
#     user_input = input('(ENTER to EXIT) Fill in square size: ')
#     if user_input == '':
#         break
#     square = int(user_input)
#     s = square**2
#     p = square*4
#     print(f'square is {s}, perimetr is {p}')

##################### door's entrance #########################
# import math
# doors_h = int(input('enter doors height - '))
# doors_w = int(input('enter doors width - '))
# doors_t = int(input('enter doors thickness - '))

# plank_l = int(input('enter planks length - '))
# plank_w = int(input('enter planks width - '))

# entrance_length = doors_h * 2 + doors_w
# pices_needed = math.ceil(entrance_length / plank_w)
# pices_from_one_plank = plank_l // doors_t
# plank_needed = math.ceil(pices_needed / pices_from_one_plank)

# print('entrance_length - ' + str(entrance_length))
# print('pices needed by plank width - ' + str(pices_needed))
# print('pices from one plank - ' + str(pices_from_one_plank))
# print('plank_needed - ' + str(plank_needed))

##########################  10000   ####################################
# while True:
#     user_input = input('Enter number from -10000 to 10000: ')
#     if user_input == '':
#         break
#     num = int(user_input)
#     if (abs(num) > 10000):
#         print('Number should be from -10000 to 10000')
#     else:
#         print(f'The next number for {num} is {num + 1}.')
#         print(f'The previous number for {num} is {num - 1}.')
#         break

############################# Hypotenuza ####################################
# a = int(input('Enter katet a: '))
# b = int(input('Enter katet b: '))
# c = math.sqrt(a**2 + b**2)

# print(f'For katet {a} and katet {b} hypotenuza is {c}')
    
################################  MKAD    ######################################
# mkad = 109
# v = int(input('Enter speed - '))
# t = int(input('Enter time - '))
# s = v * t
# mkad_km = s%109
# print(mkad_km)

