n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n-2):
    if(l[i+1]>l[i+2]>0 and l[i]>=l[i+1]-l[i+2]):
        m=l[i+1]-l[i+2]
        for j in range(2): l[i+j]-=m
        s+=5*m
    elif(l[i+1]>l[i+2]>0):
        m=l[i]
        for j in range(2): l[i+j]-=m
        s+=5*m
        continue
    t=[l[i],l[i+1],l[i+2]]
    m=min(t)
    for j in range(3): l[i+j]-=m
    s+=7*m
    if(l[i]==0): continue
    t=[l[i],l[i+1]]
    m=min(t)
    for j in range(2): l[i+j]-=m
    s+=5*m
    if(l[i]==0): continue
    m=l[i]
    l[i]=0
    s+=3*m
t=[l[-2],l[-1]]
m=min(t)
l[-2]-=m
l[-1]-=m
s+=5*m
s+=3*l[-2]
s+=3*l[-1]
print(s)