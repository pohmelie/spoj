for _ in range(int(input())):
    a, b, c, d = tuple(map(float, input().split()))
    p = (a + b + c + d) / 2
    print("{:.2f}".format(pow((p - a) * (p - b) * (p - c) * (p - d), 0.5)))
