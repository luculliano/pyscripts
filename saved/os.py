# when fileis large. See last 10 lines
with open('grades.txt') as file:
    lines = []
    for line in file:
        lines.append(line.strip())
        if len(lines) > 10:
            del lines[0]
    print(*lines, sep='\n')
# or
with open(file) as file:
    for line in file:
        ...
# or chunksize=2kB, or 65536=64kB.
def hash_func(filename, chunksize=2048):
    with open(filename, 'rb') as file:
        sha1 = hashlib.sha1()
        while True:
            content = file.read(chunksize)
            if not content:
                break
            sha1.update(content)
        print(sha1.hexdigest(), filename)


# uptime comparison of functions
import time


def for_and_append(iterable):
    result = []
    for elem in iterable:
        result.append(elem)
    return result  # с использованием цикла for и метода append()


def list_comprehension(iterable):
    return [elem for elem in iterable]  # с использованием списочного выражения


def list_function(iterable):
    return list(iterable)


def which_faster(iter, *funcs):
    times = {}
    for func in funcs:
        s = time.perf_counter()
        res = func(iter)
        f = time.perf_counter()
        times.setdefault(func.__name__, f - s)

    return dict(sorted(times.items(), key=lambda tpl: tpl[1]))


print(which_faster(range(100_000), for_and_append, list_comprehension, list_function))


# {'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}
import csv

def csv_columns(filename):
    with open(filename, encoding='utf-8') as file:
        content = csv.DictReader(file, delimiter=';')
        d = {}
        for line in content:
            for key in line.keys():
                d.setdefault(key, []).append(line[key])
        return d

print(csv_columns('sales.csv'))


# total dir size
import os


def get_size():
    total_size = 0
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            full_filename = os.path.join(dirpath, filename)
            if not os.path.islink(full_filename):
                total_size += os.stat(full_filename).st_size

    return f'{total_size} bytes = {round(total_size / 1024)} KB = {round(total_size / 1024 ** 2)} MB = {round(total_size / 1024 ** 3)} GB'


print(get_size())
