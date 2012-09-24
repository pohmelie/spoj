for _ in range(int(input())):
    pew, pfw = tuple(map(int, input().split()))
    coins = tuple(map(lambda _: tuple(map(int, input().split())), range(int(input()))))
    m, s = {0:0}, "This is impossible."
    for i in range(1, pfw - pew + 1):
        for p, w in coins:
            if i - w in m:
                m[i] = min(m.get(i, m[i - w] + p), m[i - w] + p)
    if pfw - pew in m:
        s = "The minimum amount of money in the piggy-bank is {}.".format(m[pfw - pew])
    print(s)
