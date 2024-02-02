#Задание 1
import re
def cool_num(input_str):
    for m in range(len(input_str)):
        z = input_str[m].split('\\')
        print(z[0].zfill(4) + '\\'+ z[1].zfill(5))

def read_str(input_str):
    match = re.findall(r'\d{2,4}\\\d{2,5}',input_str,re.I)
    cool_num(match)


read_str('Адресс 124\\56. Почта 78\\900')


