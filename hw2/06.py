# homework lesson: 2, task: 6
"""
*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать
программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

products = list()
stop = True
i = 0
while stop:
    name = input('Введите название товара: ')
    price = input('Введите цену товара: ')
    while not price.isdigit():
        price = input('Введите цену товара: ')
    price = int(price)
    count = input('Введите количество товара: ')
    while not count.isdigit():
        count = input('Введите количество товара: ')
    count = int(count)
    unit = input('Введите наименование единиц товара: ')
    products.append((i + 1,
                     {'название': name,
                      'цена': price,
                      'количество': count,
                      'eд': unit,
                      }
                     ))
    still = input('Ввести еще один продукт? Да/нет: ')
    if still in ('Да', 'да', 'Д', 'д', '\n', '',):
        i += 1
    else:
        stop = 0
print(products)

names = list()
prises = list()
counters = list()
units = list()
for product in products:
    names.append(product[1]['название'])
    prises.append(product[1]['цена'])
    counters.append(product[1]['количество'])
    units.append(product[1]['eд'])
stat = {'название': names,
        'цена': prises,
        'количество': counters,
        'eд': units,
        }
print(stat)
