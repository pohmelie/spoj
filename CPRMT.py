from collections import defaultdict


def yoba(s):
    d = defaultdict(lambda: 0)
    for ch in s:
        d[ch] += 1
    return d

while True:
    try:
        d1, d2, s = yoba(input()), yoba(input()), ""
        for ch in d1:
            if d2[ch] > 0:
                m = min(d1[ch], d2[ch])
                s, d1[ch], d2[ch] = s + ch * m, d1[ch] - m, d2[ch] - m
        print("".join(sorted(s)))
    except:
        break
