#Задание 2
def poisk_max_element(z):
    max_id = 0
    max = 0
    for i in range(len(z)):
        if z[i][1] > max:
            max_id = i
    return max_id
def new_way_banks(k,l):
    li = []
    for j in range(len(l)):
        li.append([1, l[j]])
    max_id = poisk_max_element(li)
    for i in range(k):
        li[max_id][1] = (li[max_id][0] * li[max_id][1]) / (li[max_id][0] + 1)
        li[max_id][0] += 1
        max_id = poisk_max_element(li)
    output_new_ways(li)

def output_new_ways (new_ways_of_banks):
    for i in range(len(new_ways_of_banks)):
        for j in range(new_ways_of_banks[i][0]):
            print(new_ways_of_banks[i][1])

new_way_banks(2,[100])
