max_num = 0

while True:
    num=int(input('Введите число (0 для остановки)>>> '))
    if num == 0:
        break
    if max_num == 0:
        max_num = num
    else:
        if num > max_num:
            max_num = num
if max_num != 0:
    print('Самое большое число>>>', max_num)
else:
    print('Числа не введены')