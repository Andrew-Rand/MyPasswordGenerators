letters = 'abcdefghijklmnopqrstuwxyz'
upper_Letters = letters.upper()
digits = '0123456789'
symbols = '!@#$%^&*()\'\\'

alphabet_hard =digits + letters + upper_Letters + symbols

alphabet_simple = '0123456789abcdefghijklmnopqrstuwxyz'

#алгоритм основан на системах счисления

alphabet = alphabet_hard
base = len(alphabet)  #база системы счисления
length = 0
counter = 0  #счётчик итераций в десятиричной системе исчесления

while True:

    password = ''
    temp = counter
    while temp > 0:
        temp // base
        rest = temp % base #остаток от деления, который и является фрагментами числа в нужной системе
        temp = temp // base

        password = alphabet[rest] + password

    while len(password) < length:  #чтобы были цифры с нуля
        password = '0' + password

    #код с использованием подобранного пороля
        
    print(password)

    if password == alphabet[-1] * length:  #если перебран последний пароль на этой длине
        length += 1  #переходим к паролям большей длинны
        counter = 0  #обнуляем счётчик, чтобы снова рисовались нули
    else:
        counter += 1
  


