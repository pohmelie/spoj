"""for i in range(1000):
    n, c = i, 0
    while n > 1 and c < 1000:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 3
        c += 1
    if c < 1000:
        print(i)
"""
from math import log


n = int(input())
print("TAK" if pow(2, int(log(n, 2))) == n else "NIE")
