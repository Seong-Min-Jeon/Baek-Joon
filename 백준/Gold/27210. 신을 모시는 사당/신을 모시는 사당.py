n=int(input())
t=list(map(int,input().split()))
l,r=[],[]
for i in range(n):
    if(t[i]==1): l.append(1); r.append(-1)
    else: l.append(-1); r.append(1)
m,s=0,0
for e in l:
    s+=e
    if(s<0): s=0
    m=max(m,s)
s=0
for e in r:
    s+=e
    if(s<0): s=0
    m=max(m,s)
print(m)