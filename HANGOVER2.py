mem = tuple(map(lambda x: sum(map(lambda y: 1 / (y + 2), x)), map(range, range(1, 277))))
while True:
    n = float(input())
    if n == 0.0:
        break
    for i, v in enumerate(mem, 1):
        if v > n:
            print(i, "card(s)")
            break
