import math# Добавляем библиотеку

x = int(input("Введите число "))#Просим ввести число с клавиатуры

if x >= 0:
    x = math.sqrt(x)
    print(x)
else:
    x = x * x
    print(x)
