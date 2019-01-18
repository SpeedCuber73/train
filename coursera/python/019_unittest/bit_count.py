"""
Реализовать функцию подсчета единичных битов целого числа и протестировать ее
"""


def count_bits(number):
    """count the number of 1 bits in a binary representation of the number"""
    return bin(number).count('1')
