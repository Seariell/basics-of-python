#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
string1 = "qwerty"
while not string1.isdigit():
    string1 = input("Введите целое положительное число: ")
max_num = string1[0]
index_string1 = 1
while index_string1 < len(string1):
    max_num = max(max_num, string1[index_string1])
    index_string1 += 1
print("Самая большая цифра в чашем числе: %s" % max_num)
