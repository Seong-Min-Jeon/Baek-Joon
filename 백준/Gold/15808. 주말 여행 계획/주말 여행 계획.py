import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
n=int(I())
l=[[] for _ in range(n+2)]
for i in range(1,n+1):
    t=[*F()]
    for j in range(1,n+1):
        if(t[j-1]!=0):
            l[i].append((j,t[j-1]))
            l[j].append((i,t[j-1]))
p,q=F()
for _ in range(p):
    a,w=F()
    l[0].append((a,-w))
for _ in range(q):
    a,w=F()
    l[a].append((n+1,-w))
r=[1e99]*(n+2)
r[0]=0
q=[(0,0)]
while q:
    d,p=heapq.heappop(q)
    if(r[p]<d): continue
    for i,e in l[p]:
        if(r[i]>d+e):
            r[i]=d+e
            heapq.heappush(q,(d+e,i))
print(-r[-1])