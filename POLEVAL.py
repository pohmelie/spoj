i = 0
while True:
    i += 1
    n = int(input())
    if n == -1:
        break
    c = tuple(map(int, reversed(input().split())))
    k = int(input())
    x = tuple(map(int, input().split()))
    print("Case {}:".format(i))
    for j in x:
        r = c[0]
        for k in range(1, n + 1):
            r += c[k] * pow(j, k)
        print(r)
