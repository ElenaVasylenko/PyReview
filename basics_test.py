# import re
#
# a = 'abcd'
# b = 'cd'
#
# print(b in a)
# print(a.__contains__(b))
# print(a.find(b))
# print(a.rfind(b))
#
#
# l = [[1,2,3]]
#
# m = l.copy()
# print(m)
# l[0][1] = 'X'
# print(l)
# print(m)
#
# z = {1:'bill', 2:'age', 3:'22'}
# v = list(z.values())
# print(v)
#

matrix = [[0, 2, 4, 5],
          [3, 1, 1, 8]]

def main_diagonal(matrix :list):
    column_id = 0
    diagonal = []
    for row in matrix:
        if column_id < len(row):
            diagonal.append(row[column_id])
            column_id += 1
    return diagonal

#print(main_diagonal(matrix))
from  functools import reduce
numbers = [2, 2, 1]
# result = reduce(pow, numbers, 3)
# print(result)
#
# print(list(reversed(range(1,6))))


def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1), 1)
print(factorial(7))

t = (2, 3, 4)
print(t)
