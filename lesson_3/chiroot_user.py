#курс Лучший по Python. Часть 2, 15.2
# добавить описание кода

import random

drop = random.randint(1, 8)

if drop == 1:
    superpower = 'Заморозка времени'
else:
    print('Увы, ничего не выпало, повезёт в следующий раз!')

print('Try again and repeat')
