for _ in range(int(input())):
    m=[]
    for i in range(int(input())):
        n=tuple(map(int,input().split()))
        m+=[0]
        for j in range(1,i+1):
            m[j]=max(m[j],m[j-1])+n[j]
        m[0]+=n[0]
    print(max(m))
