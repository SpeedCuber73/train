"""
найти медиану списка целых чисел
"""

import random

numbers = []
numbers_size = random.randint(10, 15)

for _ in range(numbers_size):
    numbers.append(random.randint(10, 20))

numbers.sort()

half_size = len(numbers) // 2
median = None

if numbers_size % 2 == 1:
    median = numbers[half_size]
else :
    median = sum(numbers[half_size - 1:half_size + 1]) / 2

print(numbers)
print(median)
