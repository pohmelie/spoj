n = 0
while True:
    s, n, st, rep = input().strip(), n + 1, 0, 0
    if s[0] == "-":
        break
    for c in s:
        if c == "{":
            st = st + 1
        elif st == 0:
            st, rep = 1, rep + 1
        else:
            st = st - 1
    print("{}. {}".format(n, rep + st // 2))
