print('<<<<<<<<вычесление произведения>>>>>>>>')
product=1
while True:
    num=float(input('Введите число>>> '))
    if num <0:
        print("****обнаружено отрицательное число. Ввод завершен.****")

        break
    product *= num
    print(f'Произведение>>> {product}')
print(f"итоговое произведение>>> {product}")
