n=int(input())
a,b=1e99,0
m=0
l=[]
for e in map(int,input().split()):
    b=max(b,e)
    m=max(m,b-a)
    l+=[m]
    if(a>e): a,b=e,e
print(*l)