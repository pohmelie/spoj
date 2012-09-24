m = dict()
while True:
    b, n = tuple(map(int, input().split()))
    if b == 0 and n == 0:
        break
    p = tuple(map(lambda _: tuple(map(int, input().split())), range(n)))
    m.clear()
    m[0], best = (0, ()), (0, 0)
    for i in range(1, b + 1):
        for j in range(n):
            fee, fun = p[j]
            if (i - fee in m) and (j not in m[i - fee][1]) and \
               ((i not in m) or (m[i][0] < m[i - fee][0] + fun)):
                m[i] = (m[i - fee][0] + fun, m[i - fee][1] + (j,))
                if m[i][0] > best[1]:
                    best = (i, m[i][0])
    print(" ".join(map(str, best)))
    input()
