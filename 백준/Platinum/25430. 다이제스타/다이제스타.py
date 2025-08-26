import sys,heapq
I=sys.stdin.readline
f=lambda:map(int,I().split())
n,m=f()
l=[[] for _ in range(n+1)]
for _ in range(m):
    i,j,d=f()
    l[i].append((j,d))
    l[j].append((i,d))
s,z=f()
r=[[(1e99,0)] for _ in range(n+1)]
r[s].append((0,0))
q=[(0,s,0)]
while q:
    d,p,x=heapq.heappop(q)
    b=0
    for g,y in r[p]:
        if(g<d and y<x): b=1
    if(b): continue
    for i,e in l[p]:
        if(e<=x): continue
        b=1
        for g,y in r[i]:
            if(d+e>g and e>y): b=0
        if(b):
            r[i].append((d+e,e))
            q.append((d+e,i,e))
m=1e99
for g,y in r[z]:
    m=min(m,g)
if(m==1e99): print('DIGESTA')
else: print(m)