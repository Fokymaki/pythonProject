#Задание 2
def poisk_max_element(z):
    max = 0
    for i in range(len(z)):
        if z[i][1] > max:
            max = z[i][1]
    return max
def new_way_banks(k,l):
    max = poisk_max_element(l)
    for i in range(k):
        for j in range(len(l)):
            if l[j][1] == max:
                l[j][1] = (l[j][0] * l[j][1]) / (l[j][0] + 1)
                l[j][0] += 1
        max = poisk_max_element(l)
    output_new_ways(l)
def output_new_ways (new_ways_of_banks):
    for i in range(len(new_ways_of_banks)):
        for j in range(new_ways_of_banks[i][0]):
            print(new_ways_of_banks[i][1])
def read_str(input_str):
    final_input_str = []
    new_input = input_str[0].split(' ')
    k = int(new_input[1])

    input_str = input_str[1:]
    input_str = list(map(int, input_str))
    for i in range(len(input_str)):
        final_input_str.append([1, input_str[i]])
    new_way_banks(k,final_input_str)
str =[]
while True:
    s = input()

    if s:
        str.append(s)

    else:
        break
read_str(str)