"""
Посчитать сколько слов в строке начинается с символа 'a' или 'A'.
Разделителями являются ' ', '.', ',', '?', '!'
"""

input_string = input("Введите строку: ")
words = input_string.replace('?', ' ').replace('!', ' ').replace(',', ' ').replace('.', ' ').split()
count = 0
for word in words:
    if word[0].capitalize() == 'A':
        count += 1
print(count)
