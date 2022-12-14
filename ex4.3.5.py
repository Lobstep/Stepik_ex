# Вводится текущее время (секунды) в диапазоне [0; 59]. Если значение равно 59, то следующее должно быть 0.
# И так по кругу. Необходимо  вычислить следующее значение с проверкой граничного значения 59.
# Реализуйте это с помощью тернарного условного оператора. Результат отобразите на экране.
sec = int(input())
print(sec + 1 if sec < 59 else 0)

# P.S. Попробуйте также реализовать эту же задачу с использованием только арифметических операций.

sec = int(input())
print(sec % 59 + 1 if sec != 59 else 0)