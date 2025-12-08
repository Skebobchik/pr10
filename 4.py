

total=0
while True:
    price=int(input('Введите цену товара (0 для закрытия)>>> '))
    if price==0:
        break
    if price<0:
        print('Ошибка цены')
        continue
    total+=price
if total > 1000:
    discount = total *0.1
    total -= discount
print('Итоговая сумма к оплате>>> ', total)