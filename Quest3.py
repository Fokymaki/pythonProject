#Задание 3
def poisk(input_str_array):
    input_str_array.sort(reverse=True)
    print(''.join(input_str_array))


poisk(['1','005','9','1000'])
