#Необходимо определить, можно ли их интерпретировать (воспринимать) как длины сторон треугольника.
# Напомню, что сумма длин двух произвольных сторон всегда должна быть больше третьей стороны.
# На экран вывести True, если треугольник формируется и False - в противном случае.
# Задача делается без использования условного оператора.
a, b, c = map(int, input().split())
print(a + b > c and a + c > b and b + c > a)