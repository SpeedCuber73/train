"""
В этом задании вам нужно создать интерфейс для работы с файлами.
Класс File должен поддерживать несколько необычных операций.

Класс инициализируется полным путем.
obj = File('/tmp/file.txt')

Класс должен поддерживать метод write.
obj.write('line\n')

Объекты типа File должны поддерживать сложение.
first = File('/tmp/first')
second = File('/tmp/second')
new_obj = first + second
В этом случае создается новый файл и файловый объект, в котором содержимое
второго файла добавляется к содержимому первого файла.
Новый файл должен создаваться в директории, полученной с помощью tempfile.gettempdir.
Для получения нового пути можно использовать os.path.join.

Объекты типа File должны поддерживать протокол итерации, причем итерация проходит по строкам файла.
for line in File('/tmp/file.txt'):
  ...

И наконец, при выводе файла с помощью функции print должен печататься его полный путь,
переданный при инициализации.
obj = File('/tmp/file.txt')
print(obj)
'/tmp/file.txt'
"""


import tempfile
import os


class File:

    def __init__(self, filename):
        self.__filename = filename
        self.__current_line = 0

    def __str__(self):
        return self.__filename

    def __add__(self, other):
        with open(str(other), 'r') as f:
            other_text = f.read()

        with open(str(self), 'r') as f:
            result_text = f.read() + other_text

        new_filename = os.path.join(tempfile.gettempdir(), "arbitrary.txt")
        with open(new_filename, 'w') as f:
            f.write(result_text)

        return File(new_filename)

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.__filename, 'r') as f:
            lines = f.readlines()
            if self.__current_line >= len(lines):
                raise StopIteration
            else:
                result = lines[self.__current_line]
                self.__current_line += 1
                return result

    def write(self, text):
        with open(self.__filename, 'a') as f:
            f.write(text)
