# Напишите функцию, принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.
def get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]
n = int(input())
print(get_factors(n))

# 2
print(*[int(i) ** 2 for i in input().split(' ') if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4])

# 3. Input n digits in format "1 2 3...n", merge all together.
def merge(list1, list2):
    l = list1 + list2
    l.sort()
    return l

total_list = []
for i in range(int(input())):
    l = [int(i) for i in input().split(' ')]
    total_list = merge(total_list, l)

print(*total_list)


# 4
# greet takes 1+ args
def greet(name, *args):
    return f'Hello, {" and ".join(((name,) + args))}!'


# 5. sort the list by categories
athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39),
            ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100),
            ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

# I)
def generator_comparator(value_of_tpl):
    def comparator(tpl):
        return tpl[value_of_tpl - 1]
    return comparator  # return comparator function
comp = generator_comparator(int(input()))
athletes.sort(key=comp)

# II)
def comparator(tpl):
    return tpl[value_of_tpl - 1]
value_of_tpl = input()
# needs to be not other name-so key won't see it, and function not see it local but see global
athletes.sort(key=comparator)


# 6. THINK ABOUT IT
import math

def pwr(p):
    def num_pwr(x):
        return x ** p
    return num_pwr

my_dict = {'квадрат': pwr(2), 'куб': pwr(3), 'корень': pwr(0.5), 'модуль': abs, 'синус': math.sin}

x, key = int(input()), input()

print(my_dict[key](x))


# 7. check input string on positive int or float
is_non_negative_num = lambda x: x.replace('.', '', 1).isdigit()
is_non_negative_num = lambda x: x.lstrip('-').replace('.', '', 1).isdigit()


# 8. Sort by digits, after words
mixed_list = [
    'beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15,
    65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal',
    'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60,
    'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12,
    'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64,
    38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide',
    'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant',
    'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46,
    'betray', 47, 'able', 11
]
print(*sorted(sorted(mixed_list, key=lambda el: el if isinstance(el, int) else 0), key=lambda el: el if isinstance(el, str) else ''))
'''
returnes (True, 'beside') True=1=>in the end, so ins will go to the beegining,
when 0=0, it will compare by second eleement of tuple
'''
print(*sorted(mixed_list, key=lambda x: (isinstance(x, str), x)))


# 9 zip
def read_csv():
    with open('data.csv') as file:
        keys, *values = [line.strip().split(',') for line in file.readlines()]
        return [dict(zip(keys, value)) for value in values]


# x6+2x5+3x4+4x3+5x2+6x+7x6+2x5+3x4+4x3+5x2+6x+7, [1, 2, 3, 4, 5, 6, 7], 1
from functools import reduce
from operator import add

evaluate = lambda lst, x: reduce(add, map(lambda coef, n: coef * x ** n, lst, range(len(lst))[::-1]), 0)
print(evaluate(list(map(int, input().split())), int(input())))


# using generator
abscissas, ordinates, applicates = (map(float, input().split()) for _ in range(3))
print(all(x ** 2 + y ** 2 + z ** 2 <= 4 for x, y, z in zip(abscissas, ordinates, applicates)))


# check password
pswd = 'asFdg234'
print(('NO', 'YES')[all([len(pswd) > 6, any(map(str.isupper, pswd)), any(map(str.isdigit, pswd)), any(map(str.islower, pswd))])])
