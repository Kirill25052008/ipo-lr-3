day = int(input("Введите число "))# Просим ввести день с клавиатуры
month = str(input("Введите месяц "))# Просим ввести месяц с клавиатуры

if day < 1 or day > 31:
    print("Такого числа не может быть")
elif month == 'Март' or month == 'Апрель' or month == 'Май':
    print("Весна")
elif month == 'Июнь' or month == 'Июль' or month == 'Август':
    print("Лето")
elif month == 'Сентябрь' or month == 'Октябрь' or month == 'Ноябрь':
    print("Осень")
elif month == 'Декабрь' or month == 'Январь' or month == 'Февраль':
    if month == 'Февраль' and day > 28:
        print("В феврале только 28 дней")
    print("Зима")
