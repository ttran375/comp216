# Python Module calc
import calc


def add(x, y):
    return x + y


def diff(x, y):
    return abs(x - y)


result_add = calc.add(2, 5)
print(result_add)  # returns 7

result_diff = calc.diff(4, 6)
print(result_diff)  # returns 2
