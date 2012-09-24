c = int(input())
while c:
    c -= 1
    print(str(sum(map(lambda x: int(x[::-1]), input().split())))[::-1].strip("0"))
    #input -> split -> reverse -> int -> sum -> str -> reverse -> strip -> print
