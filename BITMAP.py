pp = lambda f, n, m: "\n".join(map(lambda y: " ".join(map(lambda x: str(f[(y, x)]), range(m))), range(n)))
env = lambda y, x: ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1))
f = dict()
for t in range(int(input())):
    if t != 0:
        input()
    n, m = tuple(map(int, input().split()))
    f.clear()
    for y in range(n):
        for x, ch in enumerate(input()):
            if ch == "1":
                f[(y, x)] = 0
    changes, front = True, tuple(f)
    while changes:
        changes = False
        _front, front = front, ()
        for y, x in _front:
            for yn, xn in env(y, x):
                if 0 <= yn < n and 0 <= xn < m and (yn, xn) not in f:
                    f[(yn, xn)] = min(map(lambda z: f.get(z, n + m), env(yn, xn))) + 1
                    changes, front = True, front + ((yn, xn),)
    print(pp(f, n, m))
