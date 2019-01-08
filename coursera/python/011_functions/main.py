"""
Вывести на экран текст файла, затем переписать его и снова вывести.
Испльзовать функцию read_rewrite_read(filename)
"""


def read_rewrite_read(filename: str):
    with open(filename, 'r+') as f:
        print(f.read())
        f.seek(0)
        f.truncate()
        f.write("this is new line")
        f.seek(0)
        print(f.read())


filename = 'text.txt'
read_rewrite_read(filename)
