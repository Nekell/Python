import operator
from functools import reduce

print(reduce(operator.mul, [number for number in range(100, 1001) if number % 2 == 0]))
