max_num= None

while True:
    num=int(input('Введите число (0 для остановки)>>> '))
    if num == 0:
        break
    if max_num is None:
        max_num = num
    else:
        if num > max_num:
            max_num = num
if max_num is  not None:
    print('Самое большое число>>>', max_num)
else:
    print('Числа не введены')