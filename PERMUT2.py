while True:
    n = int(input())
    if n == 0:
        break
    x = tuple(map(int, input().split()))
    for i in range(n):
        if x[x[i] - 1] != i + 1:
            print("not ambiguous")
            break
    else:
        print("ambiguous")
