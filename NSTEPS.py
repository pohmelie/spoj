for _ in range(int(input())):
    x, y = tuple(map(int, input().split()))
    print((x + y - x % 2) if x == y or x - 2 == y else "No Number")
