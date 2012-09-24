from itertools import product


for _ in range(int(input())):
    x, y = tuple(map(lambda x: tuple(map(int, x)), input().split()))
    lx, ly = len(x), len(y)
    z = [0] * (lx + ly)
    for i, j in product(range(-1, -1 - lx, -1), range(-1, -1 - ly, -1)):
        z[i + j + 1] += x[i] * y[j]
    carry = 0
    for i in range(-1, -1 - lx - ly, -1):
        carry, z[i] = divmod(z[i] + carry, 10)
    s = "".join(map(str, z)).lstrip("0")
    print(s if s else "0")
