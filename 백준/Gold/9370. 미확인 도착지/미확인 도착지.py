import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
for _ in range(int(I())):
    n,m,t=F()
    s,g,h=F()
    l=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c=F()
        l[a].append((b,c))
        l[b].append((a,c))
    w={int(I()) for _ in range(t)}
    r=[1e99]*(n+1)
    v=[[] for _ in range(n+1)]
    r[s]=0
    q=[(0,s)]
    while q:
        d,p=heapq.heappop(q)
        if(r[p]<d): continue
        for i,e in l[p]:
            if(r[i]>d+e):
                r[i]=d+e
                heapq.heappush(q,(r[i],i))
                v[i]=[p]
            elif(r[i]==d+e):
                v[i].append(p)
    z=[]
    for e in w:
        if(r[e]==1e99): continue
        q=[e]
        while q and e not in z:
            p=q.pop()
            for f in v[p]:
                q.append(f)
                if((p==g and f==h) or (p==h and f==g)):
                    z.append(e)
                    break
    print(*sorted(z))