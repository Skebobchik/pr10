print('**********************проверка пароля**********************')

attempts= 3

while True:
    password=input('Введите пароль пж>>> ')
    corrected_password='admin'
    if password == corrected_password:
        print('пароль верен')
        break
    attempts-=1
    if attempts == 0:
        print('пароль неверен')
        break


