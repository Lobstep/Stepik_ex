# Вводятся названия городов в одну строчку через пробел.
# На основе этой строки формируется список с помощью команды:
# cities = input().split()
# Необходимо вывести значение последнего элемента этого списка на экран.
cities = list(input().split()[-1:])
print(''.join(cities))