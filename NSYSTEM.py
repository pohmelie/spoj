class yoba:
    order = "ixcm"
    def __init__(self, str=""):
        self.num = {"m":0, "c":0, "x":0, "i":0}
        n = 1
        for c in str:
            if c.isdigit():
                n = int(c)
            else:
                self.num[c] = n
                n = 1

    def __add__(self, other):
        ret = yoba()
        rem = tmp = 0
        for k in yoba.order:
            tmp = self.num[k] + other.num[k] + rem
            ret.num[k] = tmp % 10
            rem = tmp // 10
        if rem:
            for k in yoba.order:
                ret.num[k] = 9
        return ret

    def __str__(self):
        ret = str()
        for k in yoba.order[::-1]:
            if self.num[k] > 1:
                ret += str(self.num[k])
            if self.num[k] > 0:
                ret += k
        return ret

c = int(input())
while c:
    c -= 1
    a, b = tuple(input().split())
    print(yoba(a) + yoba(b))
