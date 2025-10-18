#курс Лучший по Python. Часть 2, 15.2
#Пример простого кода на python с использованием random
import random

drop = random.randint(1, 8)

if drop == 1:
    superpower = 'Заморозка времени'
elif drop == 2:
    superpower = 'Невидимость'
elif drop == 3:
    superpower = 'Чтение мыслей'
elif drop == 4:
    superpower = 'Защитное поле'
else:
    print('Увы, ничего не выпало, повезёт в следующий раз!')