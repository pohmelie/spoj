mem = {(1, 0):2, (2, 0): 3, (2, 1): 1}
def f(n, k):
    if k >= n or k < 0:
        return 0
    if (n, k) not in mem:
        mem[(n, k)] = f(n - 1, k) + f(n - 2, k) + f(n - 1, k - 1) - f(n - 2, k - 1)
    return mem[(n, k)]

for _ in range(int(input())):
    i, n, k = tuple(map(int, input().split()))
    print(i, f(n, k))
