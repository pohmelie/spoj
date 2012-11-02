from itertools import starmap


def yoba(x, z):
    zi, s = 0, 0
    for n in x:
        if zi < len(z) and n == z[zi]:
            yield s
            yield z[zi]
            zi, s = zi + 1, 0
        else:
            s = s + n
    yield s

while True:
    x = tuple(map(int, input().split()[1:]))
    if x == ():
        break
    y = tuple(map(int, input().split()[1:]))
    z = tuple(sorted(set(x) & set(y)))
    print(sum(starmap(max, zip(yoba(x, z), yoba(y, z)))))
