# Вводятся три целых положительных числа (максимум трехзначные) через пробел в одну строчку.
# Для двухзначных и однозначных чисел нужно добавить слева незначащие нули так, чтобы все числа содержали по три цифры.
# Вывести на экран полученные числа в столбик.
a, b, c = input().split()
print(a.rjust(3, '0'), b.rjust(3, '0'), c.rjust(3, '0'),sep='\n')
