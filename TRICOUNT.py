for _ in range(int(input())):
    n = int(input())
    print(n * (n + 2) * ((n << 1) | 1) >> 3)
