#Задание 3
def poisk(input_str_array):
    input_str_array.sort(reverse=True)
    print(''.join(input_str_array))

max_num = []
while True:
    input_str = input()

    if input_str:
        max_num.append(input_str)

    else:
        break

poisk(max_num)
