while True:
    n = int(input())
    if n == -1:
        break
    nums = tuple(map(lambda _: int(input()), range(n)))
    mid, mod = divmod(sum(nums), n)
    print(-1 if mod != 0 else sum(map(lambda x: 0 if x <= mid else x - mid, nums)))
