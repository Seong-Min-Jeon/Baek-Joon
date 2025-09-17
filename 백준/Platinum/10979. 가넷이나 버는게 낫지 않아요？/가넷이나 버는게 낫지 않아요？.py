import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
for k in range(int(I())):
    n,m=F()
    l=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c,d=F()
        l[a].append((b,c,d))
        l[b].append((a,c,d))
    r=[[(1e99,0)]*2 for _ in range(n+1)]
    r[1][0]=(0,0)
    q=[(0,0,1)]
    while q:
        d,c,p=heapq.heappop(q)
        if(r[p][1][0]<d): continue
        for i,e,f in l[p]:
            if(r[i][1][0]>d+e or (r[i][1][0]==d+e and r[i][1][1]>c-f)):
                r[i][1]=(d+e,c-f)
                r[i].sort()
                heapq.heappush(q,(d+e,c-f,i))
    g=0
    if(r[-1][0][0]==r[-1][1][0]): g=r[-1][0][1]
    else: g=r[-1][1][1]
    print(f'Game #{k+1}: Suckzoo ends game in time {r[-1][1][0]}, earning {-g} garnet(s).')