print('**********************проверка пароля**********************')


while True:
    password=input('Введите пароль пж>>> ')
    corrected_password='4590'
    if password == corrected_password:
        print('Доступ разрешен')
        break
    else:
        print('Ошибка. Попробуйте еще раз')