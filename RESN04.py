def yoba(piles):
    steps,div=0,1    
    for p in piles:
        steps+=p//div
        div+=1
    return steps

tests=int(input())
for t in range(tests):
    input()
    steps=yoba([int(s) for s in input().split()])
    print("ALICE" if steps%2 else "BOB")