# Вводятся три строчки стихотворения (каждая с новой строки).
# Сохранить его в виде вложенного списка с разбивкой по строкам и словам (слова разделяются пробелом).
# Результирующий список lst вывести на экран командой: print(lst)
# Мороз и солнце день чудесный
# Еще ты дремлешь друг прелестный
# Пора красавица проснис
a = list(input().split())
b = list(input().split())
c = list(input().split())
lst = [a, b, c]
print(lst)