while True:
    s = input().strip()
    if s == "0":
        break
    l, d = len(s), {0:1, 1:(1 if s[-1] != "0" else 0)}
    for i in range(2, l + 1):
        double = s[l - i:l - i + 2]
        d[i] = d[i - 1] if "0" not in double else 0
        if "10" <= double <= "26":
            d[i] += d[i - 2]
    print(d[l])
