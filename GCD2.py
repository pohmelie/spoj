for _ in range(int(input())):
    a, b = tuple(map(int, input().split()))
    while b != 0:
        a, b = b, a % b
    print(a)
