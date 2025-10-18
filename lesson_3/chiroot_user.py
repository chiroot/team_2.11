#курс Лучший по Python. Часть 2, 15.2
# добавить описание кода

import random

drop = random.randint(1, 8)

if drop == 1:
    superpower = 'Заморозка времени'
elif drop == 10:
    superpower = 'Мимикрирование'
else:
    print('Увы, ничего не выпало, повезёт в следующий раз!')
