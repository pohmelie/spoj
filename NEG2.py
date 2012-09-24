from math import log, ceil


def yoba(x):
    b = ceil(log(1 - (1 - 4) * abs(x) / (1 if x > 0 else 2), 4) - 1) * 2 + (0 if x > 0 else 1)
    xs = yoba(x - pow(-2, b)) if x != pow(-2, b) else ""
    return "1" + "0" * (b - len(xs)) + xs

n = int(input())
print(yoba(n) if n != 0 else "0")

"""
def brute(s):
    b, n = len(s), 0
    while b > 0:
        n, b = n + pow(-2, b - 1) * int(s[-b]), b - 1
    return n

print(brute(yoba(n) if n != 0 else "0"))

for i in range(-1000, 1000):
    if i != 0:
        if brute(yoba(i)) != i:
            print("Fail on i =", i)
"""
