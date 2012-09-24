for _ in range(int(input())):
    input()
    n = int(input())
    print("YES" if sum(map(lambda _: int(input()), range(n))) % n == 0 else "NO")
