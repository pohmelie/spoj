def subline(str,index=0,operands="+-*/^"):
    operator=None
    while index<len(str):  
        if str[index]==")":
            return index
        elif str[index] in operands:
            operator=str[index]        
        else:
            if str[index]=="(":
                index=subline(str,index+1,operands)
            else:           
                print(str[index],end="")
            if operator:
                print(operator,end="")
                operator=None
        index+=1           

i=int(input())
s=[]
while i:
    s.append(input())
    i-=1

for str in s:
    subline(str)
    print()