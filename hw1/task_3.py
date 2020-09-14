#3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
not_number_n = input("Введите число n: ")
if int(not_number_n) < 0:
    not_number_n = str(-int(not_number_n))
    not_number_nn = not_number_n + not_number_n
    not_number_nnn = not_number_nn + not_number_n
    print("n + nn + nnn = %d" % (-int(not_number_n) - int(not_number_nn) - int(not_number_nnn)))
else:
    not_number_nn = not_number_n + not_number_n
    not_number_nnn = not_number_nn + not_number_n
    print("n + nn + nnn = %d" %(int(not_number_n)+int(not_number_nn)+int(not_number_nnn)))