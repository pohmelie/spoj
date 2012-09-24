from functools import partial, reduce


def mins(s, inds, shift):
    ret = (inds[0],)
    for i in range(1, len(inds)):
        a, b = s[ret[0] + shift], s[inds[i] + shift]
        if a > b:
            ret = (inds[i],)
        elif a == b:
            ret += (inds[i],)
    return ret

for _ in range(int(input())):
    s = input()
    size = len(s)
    print(reduce(partial(mins, s), range(size), tuple(range(-size, 0)))[0] + size + 1)
