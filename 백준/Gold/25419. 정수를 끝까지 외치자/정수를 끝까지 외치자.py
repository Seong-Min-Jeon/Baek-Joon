n,k=map(int,input().split())
l=[1]*(n+1)
t=[*map(int,input().split())]
for e in t:
    l[e]=0
l[0]=0
x,s,c=n+1,n+1,0
for i in range(1,n+1):
    if(l[i]==0):
        if(c==0): x=i
        c+=1
    else: c=0
    if(c==k): s=x; break
l=l[:s]
r=[-1]*len(l)
r[0]=0
for i in range(len(l)-1,-1,-1):
    if(l[i]==0): continue
    f=1
    for j in range(1,k+1):
        if(i+j<len(l) and r[i+j]==1): f=0; break
    r[i]=f
f=0
for i in range(1,k+1):
    if(i<len(l) and r[i]==1): f=1; break
print(f)