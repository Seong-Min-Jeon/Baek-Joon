import sys,heapq
I=sys.stdin.readline
for _ in range(int(I())):
    n,m,o=map(int,I().split())
    l=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c=map(int,I().split())
        l[b].append((a,c))
    r=[1e99]*(n+1)
    r[o]=0
    q=[(0,o)]
    while q:
        d,p=heapq.heappop(q)
        if(r[p]<d): continue
        for i,e in l[p]:
            if(r[i]>d+e):
                r[i]=d+e
                heapq.heappush(q,(d+e,i))
    a,b=0,0
    for e in r:
        if(e!=1e99): a+=1; b=max(b,e)
    print(a,b)