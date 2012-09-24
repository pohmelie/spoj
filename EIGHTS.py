nums = tuple(filter(lambda x: pow(x, 3) % 1000 == 888, range(1000)))
for _ in range(int(input())):
    k, i = divmod(int(input()) - 1, len(nums))
    print("{}{}".format(k, nums[i]) if k else nums[i])
