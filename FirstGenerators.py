print('Интенсив python. Защита от кибер атак')
print('День 1. \n Повторим основы Python')
print('Генераторы поролей')

#Good password generator

import random

#N = input('Какая длинна пароля?') 

def good_password_generator(leight = 10, b1 = True):
    password = ''


    letters = 'abcdefghijklmnopqrstuwxyz'
    upper_Letters = letters.upper()
    digits = '0123456789'
    symbols = '!@#$%^&*()'

    if b1:
        alphabet = letters + upper_Letters + digits + symbols
    else:
        alphabet = letters + upper_Letters + digits

    for i in range(leight):
        char = random.choice(alphabet)
        password += char

#   print('Число возможных комбинаций', len(alphabet) ** N)
#   print('Ваш пароль:', password, sep = '\n')
    return password



#Bad password generator

popular_passwords = """123456
123456789
picture1
password
12345678
111111
123123
12345
1234567890
senha"""
#вместо константы подгружать файл с самыми популярными поролями
popular_passwords = popular_passwords.split('\n')

def bad_password_generator():
    return random.choice(popular_passwords)
    #Можно использовать для взлома))




#можно проверить, сколько нужно итераций, чтобы получилось длва одинаковых пароля
def theory_bad():
    a = bad_password_generator()
    b = ''
    counter = 0
    while a != b:
        b = bad_password_generator()
        counter += 1
    return counter

def theory_good():
    a = good_password_generator(3, True)
    b = ''
    counter = 0
    while a != b:
        b = good_password_generator(3, True)
        counter += 1
    return counter


print(bad_password_generator())
print(good_password_generator())

print(theory_bad())
print(theory_good())

#Переведи всё это на ООП!!!

