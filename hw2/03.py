# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
from typing import Dict, Any, Union

seasons_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето',
                9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

mounth = 0
while mounth < 1 or mounth > 12:
    try:
        mounth = int(input('Введите месяц в виде целого числа от 1 до 12: '))
    except ValueError:
        print('Необходимо ввести число!')
print(f'Месяц {mounth} соответствует сезону: {seasons_dict.get(mounth)}')
print('-' * 100)
if mounth in winter:
    print(f'Месяц {mounth} соответствует сезону: зима')
elif mounth in spring:
    print(f'Месяц {mounth} соответствует сезону: весна')
elif mounth in summer:
    print(f'Месяц {mounth} соответствует сезону: лето')
else:
    print(f'Месяц {mounth} соответствует сезону: осень')

