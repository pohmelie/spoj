n = int(input())
for _ in range(n):
    input()
    m, n = tuple(map(int, input().split()))
    x = sorted(map(lambda _: int(input()), range(m - 1)), reverse=True)
    y = sorted(map(lambda _: int(input()), range(n - 1)), reverse=True)
    xs, ys, xm, ym, xi, yi = sum(x), sum(y), 1, 1, 0, 0
    s = 0
    while xs and ys:
        if x[xi] >= y[yi]:
            xs, xi, ym, s = xs - x[xi], xi + 1, ym + 1, s + x[xi] * xm
        else:
            ys, yi, xm, s = ys - y[yi], yi + 1, xm + 1, s + y[yi] * ym
    s = s + xs * xm + ys * ym
    print(s)
