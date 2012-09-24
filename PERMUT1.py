mem = {(1, 0):1}

def yoba(n, k):
    if k < 0 or n < 1:
        return 0
    elif (n, k) not in mem:
        mem[(n, k)] = sum(map(lambda i: yoba(n - 1, k - i), range(n)))
    return mem[(n, k)]

for _ in range(int(input())):
    n, k = tuple(map(int, input().split()))
    print(yoba(n, k))
