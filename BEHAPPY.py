def yoba(n, ab):
    if not len(ab):
        return 1 if n == 0 else 0
    else:
        ret = 0
        a, b = ab.pop()
        for i in range(a, b + 1):
            ret += yoba(n - i, ab[:])
        return ret


inp = lambda: tuple(map(int, input().split()))
while True:
    m, n = inp()
    if (m, n) == (0, 0):
        break
    ab = list()
    for i in range(m):
        ab.append(inp())
    print(yoba(n, ab))
