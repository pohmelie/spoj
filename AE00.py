from math import sqrt


n = int(input())
print(sum(map(lambda x: n // x - x + 1, range(1, int(sqrt(n)) + 1))))
