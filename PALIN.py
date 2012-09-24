def inc(s, size):
    for i in range(size // 2 - ((size % 2) ^ 1), -1, -1):
        if s[i] == ord("9"):
            s[i] = ord("0")
        else:
            s[i] += 1
            return s, size
    else:
        return bytearray("1", "utf-8") + s, size + 1

def yoba(s):
    size = len(s)
    for i in range(size // 2 - 1, -1, -1):
        if s[i] > s[-i - 1]:
            break
        elif s[i] < s[-i - 1]:
            s, size = inc(s, size)
            break
    else:
        s, size = inc(s, size)
    for i in range(size // 2):
        s[-i - 1] = s[i]
    return s.decode()

def brute(num):
    while True:
        num += 1
        nums = str(num)
        for i in range(len(nums) >> 1):
            if nums[i] != nums[-i - 1]:
                break
        else:
            return nums
'''
for i in range(10000):
    yobar = yoba(bytearray(str(i), "utf-8"))
    bruter = brute(i)
    if yobar != bruter:
        print("i =", i, "yoba =", yobar, "brute =", bruter)
print("Done...")
'''
for _ in range(int(input())):
    print(yoba(bytearray(input().strip(), "utf-8")))
