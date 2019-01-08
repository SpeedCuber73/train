"""
Через сколько итераций функция random.randint(1, 10) выдаст повтор?
"""

import random

digit_set = set()

while True:
    number = random.randint(1, 10)
    if number in digit_set:
        break

    digit_set.add(number)

print(digit_set)
print(len(digit_set) + 1)
