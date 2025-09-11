import sys,heapq
I=sys.stdin.readline
f=lambda:map(int,I().split())
n,m,e=f()
l=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=f()
    l[a].append((b,c))
    l[b].append((a,c))
z=[*f()]
x,y=f()
if(x==y): print('IMPOSSIBLE'); exit()
r=[1e99]*(n+1)
r[y]=0
q=[(0,y)]
while q:
    d,p=heapq.heappop(q)
    if(r[p]<d): continue
    for i,e in l[p]:
        if(r[i]>d+e/160):
            r[i]=d+e/160
            heapq.heappush(q,(r[i],i))
a,c=0,1e9
while a<=c:
    b=(a+c)/2
    v=[1e99]*(n+1)
    v[x]=0
    q=[(0,x)]
    while q:
        d,p=heapq.heappop(q)
        if(v[p]<d): continue
        for i,e in l[p]:
            if(v[i]>d+e/b and r[i]>d+e/b):
                v[i]=d+e/b
                heapq.heappush(q,(v[i],i))
    w=0
    for i in z:
        if(r[i]>v[i]): w=1
    if(w): c=b-1e-6
    else: a=b+1e-6
print(b if b<1e8 else 'IMPOSSIBLE')