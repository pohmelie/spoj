for i in range(int(input())):
    print("Scenario #{}:".format(i + 1))
    c, f = tuple(map(int, input().split()))
    l = tuple(reversed(sorted(map(int, input().split()))))
    s, fc = l[0], 1
    while s < c and fc < f:
        s, fc = s + l[fc], fc + 1
    print(fc if s >= c else "impossible")
