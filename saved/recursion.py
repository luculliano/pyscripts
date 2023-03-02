# 1 to use recursion, the step arg is required
def draw_rect(width, height, step=0):
    if step < height:
        print(width * '*')
        draw_rect(width, height, step + 1)
draw_rect(5, 5)
#the above has disadvantage-if step is not 0 - algorithm breaks, so:
# вложенные ф-ия и механизм замыкания
def draw_rect(width, height):
    def rec(step):
        if step < height:
            print(width * '*')
            rec(step + 1)
    rec(0)
draw_rect(5, 5)


# 2 print nums from 1 to 5
def print_numbers(start, end):
    def rec(step):
        if step <= end:
            print(step)
            rec(step + 1)
    rec(start)
print_numbers(-2, 2)


# 3 sand_clock
def print_sand():
    collection = '1', '2', '3', '4'
    def rec(step, n, h):
        if step > 4:
            print(f"{' ' * (n * h // 2)}{collection[n] * step}")
            rec(step - 4, n + 1, h)
            print(f"{' ' * (n * h // 2)}{collection[n] * step}")
        else:
            print(f"{' ' * (n * h // 2)}{collection[n] * step}")
    rec(16, 0, 4)
print_sand()


#block where recursion funcs not only print but estimate and return values
# 1
# basic: 0!=1, if n>0=>n!=n*(n-1)
# return 4 * 3 * 2 * 1 * 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(4))
# the same usin lambda
factorial = lambda n: 1 if n == 0 else n * (n - 1)

#2 sum of digits [0; n], that's a formula.
def sum_to(n):
    if n == 0:
        return n
    else:
        return n + sum_to(n - 1)
print(sum_to(5))

# 3 sum of list
def recursive_sum(nums):
    if not nums:
        return 0
    return nums[0] + recursive_sum(nums[1:])

# 4 fibonaci
# Ф-ии вызываются поселдовательно, сначала левая-после правая и они строят дерево
# чисел, поэтому при большом n программа будет занимать очень много места и долго
# вычислять, ибо приходится несколько раз одно и то же значение в ф-ию передавать снова. Далее хранит n единиц и складывает их.
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
# to make it good:
# here i use Мемоизацию-способ оптимизации, когда сохраятся рез-тат выполнения ф-ии и исп. при след. вызове. В питоне по ум. мемоизация выкл, ее можно вкл вручную (декоратор lru_cache в модуле functools)
def fib(n):
    cache = {1: 1, 2: 1}
    def rec(n):
        result = cache.get(n)
        if result is None:
            result = fib(n - 1) + fib(n - 2)
            cache[n] = result
        return result
    return rec(n)
print(fib(6))

# 4 count amount of nums in mum
n = 123
def digit(n):
    if n < 10:
        return 1
    else:
        return 1 + digit(n/10)
print(digit(n))


# 5 sum of numebers of the number
def sum_nums(n):
    if n > 0:
        return n % 10 + sum_nums(n // 10)
    else:
        return 0

# 6 sum in range indexes as [3, 7], i.e. 4+5+6+7+8=30
def range_sum(numbers, start, end):
    if start < end:
        return numbers[start] + range_sum(numbers, start + 1, end)
    else:
        return numbers[end]
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))

# 6 as pow(5, 2) = 5 ** 2 = 25
def get_pow(a, n):
    if n > 0:
        return a * get_pow(a, n - 1)
    else:
        return 1
print(get_pow(5, 2))

# 7 recursive a + b
def recursive_sum(a, b):
    if b == 0:
        return a
    return recursive_sum(a + 1, b - 1)
print(recursive_sum(1, 20))

# 8
def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])
print(is_palindrome('stepik'))
print(is_palindrome('level'))

# 9
def print_subtraction(n):
    if n > 0:
        print(n)
        print_subtraction(n - 5)
        print(n)
    else:
        print(n)
print_subtraction(20)


# 10 Рекурсия-удобна при работе с влженными структурами данных.
# надо обойти спиоск и все вложенные списки и найти только строки.
def get_all_str(data):
    if type(data) == str:
        print(data, end=" ")
    if type(data) == list:
        for i in data:
            get_all_str(i)
numbers = ["1", ["2", "3", ["4"], ["5", ["6", "7"]]]]
get_all_str(numbers)

# 11 пройтись по списку и найти значение нужного ключа.
def find_key(data, key):
    if key in data:
        return data[key]
    for v in data.values():
        if type(v) == dict:
            # если ключа нет-ф-ия ничего не делает, т.е.вернет None
            value = find_key(v, key)
            if value is not None:
                return value
info = {
    "name": "Alyson",
    "surname": "Hannigan",
    "birthday": {"day": 24, "month": "March", "year": 1974},
    "family": {"parents": {"mother": "Emilie Posner", "father": "Alan Hannigan"}},
}
print(find_key(info, "year"))
print(find_key(info, "father"))

# 12 recursive sum in nested list
def recursive_sum(nested_list):
    if type(nested_list) != list:
        return nested_list
    if not nested_list:
        return 0
    return recursive_sum(nested_list[0]) + recursive_sum(nested_list[1:])
my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(recursive_sum(my_list))

# 13 linear
def linear(some_list):
    if not some_list:
        return some_list
    if type(some_list[0]) == list:
        return linear(some_list[0]) + linear(some_list[1:])
    return some_list[:1] + linear(some_list[1:])
my_list = [3, [4], [5, [6, [7, 8]]]]
print(linear(my_list))

# fib nums optimization with __dict__
# кэширем значения в __dict__.
def fib(n):
    if n < 2:
        return n
    if n not in fib.__dict__:
        return fib(n - 1) + fib(n - 2)
    return fib.n
