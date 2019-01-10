"""
Написать функцию, которая превращает список целых чисел в список строк
"""


def from_int_to_str(int_list):
    return list(map(str, int_list))


my_list = [1, 43, 22]
print(my_list)
print(from_int_to_str(my_list))
