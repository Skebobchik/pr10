from random import choice

balance = 1000

while True:
    print('Меню')
    print('1. Узнать баланс')
    print('2. Снять 100 руб')
    print('3. Положить 100 руб')
    print('4. Выход')

    choice= input('Введите номер операции>>> ')
    if choice == '1':
        print('Текущий баланс>>> ', balance)
    elif choice == '2':
        if balance >= 100:
            balance = balance - 100
            print('Успешно снято с вашего счета!')
        else:
            print('Недостаточно средств!')
    elif choice == '3':
        balance += 100
        print('Успешно пополнено на 100 руб!')
    elif choice == '4':
        print('До свидания!')
        break
    else:
        print('Неверный выбор!')