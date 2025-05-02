from itertools import combinations as c
n,m=map(int,input().split())
l=list(map(int,input().split()))
r=[]
for t in c(l,m):    
    s=sum(t)
    if(s in r): continue
    f=1
    for i in range(2,int(s**0.5)+1):
        if(s%i==0): f=0; break
    if(f): r.append(s)
if(not r): print(-1)
else: print(*sorted(r))