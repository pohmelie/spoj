while True:
    a, d = tuple(map(int, input().split()))
    if a == 0 and d == 0:
        break
    at = min(map(int, input().split()))
    de = tuple(filter(lambda x: x <= at, map(int, input().split())))
    print("Y" if len(de) < 2 else "N")
