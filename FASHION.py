from operator import mul


for _ in range(int(input())):
    input()
    yoba = lambda: sorted(map(int, input().split()))
    print(sum(map(mul, yoba(), yoba())))
