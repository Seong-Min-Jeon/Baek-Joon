import copy
n,m=map(int,input().split())
l=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    l[a].append(b)
    l[b].append(a)
m=0
def f(l,c):
    global m
    b=0
    for p in l:
        b+=len(p)
    if(b==0): m=max(m,c); return
    a,i=0,0
    for j,p in enumerate(l):
        if(len(p)>a): a=len(p); i=j
    g=0
    for p in l[i]:
        if(len(l[p])==0): g+=len(l[p]); continue
        z=copy.deepcopy(l)
        z[i].clear()
        z[p].clear()
        f(z,c+2)
    if(g==0):
        z=copy.deepcopy(l)
        z[i].clear()
        f(z,c)
f(l,0)
if(m<n): m+=1
print(m)