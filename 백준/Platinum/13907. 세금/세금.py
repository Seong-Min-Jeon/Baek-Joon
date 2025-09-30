import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m,k=F()
s,o=F()
l=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=F()
    l[a].append((b,c))
    l[b].append((a,c))
r=[set() for _ in range(n+1)]
r[s].add((0,0))
q=[(0,0,s)]
while q:
    c,d,p=heapq.heappop(q)
    for i,e in l[p]:
        f=0
        for x,y in r[i].copy():
            if(x<=c+1 and y<=d+e):
                f=1
            if(x>=c+1 and y>=d+e):
                r[i].remove((x,y))
        if(f): continue
        r[i].add((c+1,d+e))
        heapq.heappush(q,(c+1,d+e,i))
for i in range(k+1):
    t=set()
    m=1e99
    z=int(I()) if i!=0 else 0
    for x,y in r[o]:
        t.add((x,x*z+y))
        m=min(m,x*z+y)
    r[o]=t.copy()
    print(m)