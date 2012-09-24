n=[]
n.append(int(input()))
while n[-1]!=42:
    n.append(int(input()))
for i in n:
    if i!=42:print(i)