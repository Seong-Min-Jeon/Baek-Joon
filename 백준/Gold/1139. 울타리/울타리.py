def f(a,b,c):
    p=(a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5
n=int(input())
l=[*map(int,input().split())]
d=[0]*(1<<n)
for i in range(n):
    for j in range(n):
        for k in range(n):
            for b in range(1<<n):
                if(i!=j and j!=k and i!=k and b&(1<<i)==0 and b&(1<<j)==0 and b&(1<<k)==0 
                   and l[i]<=l[j]<=l[k] and l[i]+l[j]>l[k]):
                    d[b|(1<<i)|(1<<j)|(1<<k)]=max(d[b|(1<<i)|(1<<j)|(1<<k)],d[b]+f(l[i],l[j],l[k]))
print(max(d))