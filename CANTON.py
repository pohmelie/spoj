def hor():
    n, d = 1, 1
    while True:
        yield n, d
        n, d = n + 2 * d + 3, d + 2

for _ in range(int(input())):
    n, h, d = int(input()), 1, 1
    for horn, i in hor():
        h, d = horn, i
        if horn >= n:
            break
    x, y, i = d, 1, h
    while i != n and x != 1:
        x, y, i = x - 1, y + 1, i - 1
    if i != n:
        y, i = y - 1, i - 1
    while i != n and y != 1:
        x, y, i = x + 1, y - 1, i - 1
    print("TERM {} IS {}/{}".format(i, y, x))
