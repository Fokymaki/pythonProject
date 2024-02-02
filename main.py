# #
# import numpy as np
# # Задание 1
# import re
# def cool_num(input_str):
#     for m in range(len(input_str)):
#         z = input_str[m].split('\\')
#         print(z[0].zfill(4) + '\\'+ z[1].zfill(5))
#
# def read_str(input_str):
#     match = re.findall(r'\d{2,4}\\\d{2,5}',s,re.I)
#     cool_num(match)
#
# s = input()
# read_str(s)


# def poisk_max_element(z):
#     max = 0
#     for i in range(len(z)):
#         if z[i][1] > max:
#             max = z[i][1]
#     return max
# def new_way_banks(k,l):
#     max = poisk_max_element(l)
#     for i in range(k):
#         for j in range(len(l)):
#             if l[j][1] == max:
#                 l[j][1] = (l[j][0] * l[j][1]) / (l[j][0] + 1)
#                 l[j][0] += 1
#         max = poisk_max_element(l)
#     output_new_ways(l)
# def output_new_ways (new_ways_of_banks):
#     for i in range(len(new_ways_of_banks)):
#         for j in range(new_ways_of_banks[i][0]):
#             print(new_ways_of_banks[i][1])
# def read_str(input_str):
#     final_input_str = []
#     new_input = input_str[0].split(' ')
#     k = int(new_input[1])
#
#     input_str = input_str[1:]
#     input_str = list(map(int, input_str))
#     for i in range(len(input_str)):
#         final_input_str.append([1, input_str[i]])
#     new_way_banks(k,final_input_str)
# str =[]
# while True:
#     s = input()
#
#     if s:
#         str.append(s)
#
#     else:
#         break
# read_str(str)
# new_way_banks(k,l)

#Задание 3
# def poisk(input_str_array):
#     input_str_array.sort(reverse=True)
#     print(''.join(input_str_array))
#
# max_num = []
# while True:
#     input_str = input()
#
#     if input_str:
#         max_num.append(input_str)
#
#     else:
#         break
#
# poisk(max_num)




