local r,M,m,n=io.read,math.max,{},0
for _=1,r("*n")do
    for i=1,r("*n")do
        m[i],n=0,0
        for j=1,i do
            n,m[j]=m[j],M(m[j],n)+r("*n")
        end
    end
    print(M(unpack(m)))
end
