"""
найти сумму цифр, из которых состоит строка.
строка передается как аргумент командной строки.
В строке, подаваемой на вход, будут только символы,
соответствующие цифрам от 0 до 9.
"""

import sys

digit_string = sys.argv[1]

total = 0

for digit in digit_string:
    total += int(digit)

print(total)
