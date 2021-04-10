letters = 'abcdefghijklmnopqrstuwxyz'
upper_Letters = letters.upper()
digits = '0123456789'
symbols = '_!@#$%^&*()\'\\'

alphabet_hard =digits + letters + upper_Letters + symbols
alphabet_simple = '0123456789abcdefghijklmnopqrstuwxyz'
alphabet_digits = '0123456789'

#алгоритм основан на системах счисления

alphabet = alphabet_hard  #выбрать алфавит
base = len(alphabet)  #определить базу системы счисления
length = 0  #счётчик длины поролей
counter = 0  #счётчик итераций в десятиричной системе исчесления

while True:

    password = ''
    temp = counter
    
    while temp > 0:  #цикл, который переводит в нужную систему счесления
        temp // base
        rest = temp % base #остаток от деления, который и является фрагментами числа в нужной системе
        temp = temp // base

        password = alphabet[rest] + password

    while len(password) < length:  #чтобы были цифры с нуля
        password = '0' + password

    #код с использованием подобранного пороля
    #import requests
    #response = requests.post('http://something/auth', json = {'login': 'admin', 'password': password})
    #if response.status_code == 200:
            #print('success', password)
            #break
        
    print(password)

    if password == alphabet[-1] * length:  #если перебран последний пароль на этой длине
        length += 1  #переходим к паролям большей длинны
        counter = 0  #обнуляем счётчик, чтобы снова рисовались нули
    else:
        counter += 1
  


