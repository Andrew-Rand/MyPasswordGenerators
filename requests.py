#Делаем запросы

import requests


response = requests.get('https://google.com')  #созадем объект класса requests с атрибутами 

print(response.text)  #dвыдает всю html страницу
print(response.status_code)  #tckb 200 - всё гуд


#Если слать много запросов, некоторые сайты психуют!!!

url_list = ['https://google.com', 
            'https://oz.by', 
            'https://svoeradio.fm', 
            'https://wt.edunano.ru', 
            'https://docs.cntd.ru/document/1200003911']
for i in url_list:
    counter = 1
    for j in range(100):
        response = requests.get(i)
        print( i, 'Запрос №', counter, ' ', 'статус', response.status_code)
        counter += 1
