# Эта программа получает адрес сайта,
# и после проверок условий открывает
# его в браузере по умолчанию.

import os

url = input('Введите адрес сайта: ')

if 'https://' in url:
    os.system('start ' + url)
    print('Сработал блок кода: if')

elif 'www.' in url:
    os.system('start ' + url)
    print('Сработал блок кода: elif')

else:
    os.system('start ' + 'https://www.' + url)
    print('Сработал блок кода: else')
