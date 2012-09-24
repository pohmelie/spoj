from math import sqrt


for _ in range(int(input())):
    w, v, u, U, V, W = tuple(map(int, input().split()))
    X = (w - U + v) * (U + v + w)
    x = (U - v + w) * (v - w + U)
    Y = (u - V + w) * (V + w + u)
    y = (V - w + u) * (w - u + V)
    Z = (v - W + u) * (W + u + v)
    z = (W - u + v) * (u - v + W)
    a = sqrt(x * Y * Z)
    b = sqrt(y * Z * X)
    c = sqrt(z * X * Y)
    d = sqrt(x * y * z)
    print("{:.4f}".format(sqrt((-a + b + c + d) * (a - b + c + d) * (a + b - c + d) * (a + b + c - d)) / (192 * u * v * w)))
