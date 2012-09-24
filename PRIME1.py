import math
import random

def mr(m,r):
    t, s = m-1, 0    
    while not t%2:
        s+=1
        t//=2
    for i in range(r):        
        a=random.randint(2,m-2)
        x=(a**t)%m
        if x==1 or x==m-1: continue
        next_i=False
        for j in range(s-1):                        
            x=(x**2)%m
            if x==1: return False
            if x==m-1:
                next_i=True
                break
        if not next_i: return False
    return True                

def prime(n):
    for i in range(2,math.floor(math.sqrt(n))+1):        
        if not n%i: return False
    return True

t=int(input())
mn=[]
for i in range(t):
    mn.append(input().split())
for i in range(t):
    m=int(mn[i][0])
    n=int(mn[i][1])
    if m<=2:
        print(2)
        m=3
    if m<=5:
        print(3)
        m=5
    for j in range(m,n+1,2):
        if mr(j,3) and prime(j): print(j)
    print()