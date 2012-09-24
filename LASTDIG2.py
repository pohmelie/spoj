m = tuple((tuple(((i * j) % 10 for j in range(10))) for i in range(10)))
for _ in range(int(input())):
    a, b = tuple(input().split())
    a, b = int(a[-1]), int(b)
    if(b == 0):
        a, b = 1, 1
    steps, tail, i = dict(), a, 1
    while i < b:
        if tail not in steps:
            steps[tail] = i
            i, tail = i + 1, m[tail][a]
        else:
            i = b - (b - i) % (i - steps[tail])
            steps.clear()
    print(tail)
