n,b,c=list(map(int,input().split()))
l=list(map(int,input().split()))
s=0
if(b<c):
    print(sum(l)*b); exit()
for i in range(n-2):
    if(l[i+1]>l[i+2]>0 and l[i]>=l[i+1]-l[i+2]):
        m=l[i+1]-l[i+2]
        for j in range(2): l[i+j]-=m
        s+=(b+c)*m
    elif(l[i+1]>l[i+2]>0):
        m=l[i]
        for j in range(2): l[i+j]-=m
        s+=(b+c)*m
        continue
    t=[l[i],l[i+1],l[i+2]]
    m=min(t)
    for j in range(3): l[i+j]-=m
    s+=(b+2*c)*m
    if(l[i]==0): continue
    t=[l[i],l[i+1]]
    m=min(t)
    for j in range(2): l[i+j]-=m
    s+=(b+c)*m
    if(l[i]==0): continue
    m=l[i]
    l[i]=0
    s+=b*m
t=[l[-2],l[-1]]
m=min(t)
l[-2]-=m
l[-1]-=m
s+=(b+c)*m
s+=b*l[-2]
s+=b*l[-1]
print(s)