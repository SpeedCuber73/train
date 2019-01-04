"""
Вводится строка. Удалить из нее все пробелы. После этого
определить, является ли она палиндромом (перевертышем),
т.е. одинаково пишется как с начала, так и с конца.
"""

input_string = input("Введите строку: ")
string = input_string.replace(' ', '')
is_palindrome = False
if string == string[::-1]:
    is_palindrome = True

print(f"Это полиндром: {is_palindrome}")
