def yoba():
    d, s = 2, 0.0
    while True:
        d, s = d + 1, s + 1 / d
        yield d - 2, s

while True:
    n = float(input())
    if n == 0.0:
        break
    for i, v in yoba():
        if v > n:
            print(i, "card(s)")
            break
