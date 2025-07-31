import sys,heapq
I=sys.stdin.readline
n,m=map(int,I().split())
l=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,I().split())
    l[a].append((b,c))
    l[b].append((a,c))
a,b,c=map(int,I().split())
x,y=[],[]
for t in (a,b,c):
    r=[1e99]*(n+1)
    v=[[] for _ in range(n+1)]
    q=[(0,t)]
    r[t]=0
    while q:
        d,p=heapq.heappop(q)
        if(r[p]<d): continue
        for i,e in l[p]:
            if(d+e<r[i]):
                r[i]=d+e
                heapq.heappush(q,(d+e,i))
                v[i]=[p]
            elif(d+e==r[i]):
                v[i].append(p)
    x.append(r)
    y.append(v)
m=[x[0][i]+x[1][i]+x[2][i] for i in range(n+1)]
o=set()
for i in range(3):
    t=y[i]
    v=m.index(min(m))
    while True:
        if(t[v]==[]): break
        else: o.add((t[v][0],v)); v=t[v][0]
print(min(m),len(o))
for e in o:
    print(*e)