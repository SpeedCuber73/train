"""
Задекорировать функцию сумматора, чтобы она записывала результат в указанный файл
"""


def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator


@logger('logger.txt')
def summator(num_list):
    return sum(num_list)


print(summator([1, 2, 5, 3, 3]))
