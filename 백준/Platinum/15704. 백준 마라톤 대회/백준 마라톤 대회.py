import sys,heapq
I=sys.stdin.readline
f=lambda:map(int,I().split())
n,m,k=f()
l=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c,t=f()
    l[a].append((b,c,t))
    l[b].append((a,c,t))
x,z=0,10**9
while x<=z:
    y=(x+z)//2
    r=[1e99]*(n+1)
    r[1]=0
    q=[(0,1)]
    while q:
        d,p=heapq.heappop(q)
        if(r[p]<d): continue
        for i,c,t in l[p]:
            o=d+c*(y-t)**2 if y>t else d
            if(o<r[i]):
                r[i]=o
                heapq.heappush(q,(o,i))
    if(r[-1]>k): z=y-1
    else: x=y+1
print(z)