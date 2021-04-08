letters = 'abcdefghijklmnopqrstuwxyz'
upper_Letters = letters.upper()
digits = '0123456789'
symbols = '!@#$%^&*()\'\\'

alphabet_hard =digits + letters + upper_Letters + symbols

alphabet_simple = '0123456789abcdefghijklmnopqrstuwxyz'

#алгоритм основан на системах счисления


base = len(alphabet_simple)  #база системы счисления

counter = 0  #счётчик итераций в десятиричной системе исчесления

for counter in range(1000):

    password = ''
    while counter > 0:
        counter // base
        rest = counter % base #остаток от деления, который и является фрагментами числа в нужной системе
        counter = counter // base

        password = alphabet_simple[rest] + password

    print(password)
    #алгоритм не выдаёт числа 0, 01,02 ...Только с 1


