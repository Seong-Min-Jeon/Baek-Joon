import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
for z in range(int(I())):
    a,b,c=F()
    t={}
    for i in range(b):
        x,y=F()
        t[(i,x)]=y
    l=[[] for _ in range(a+1)]
    for _ in range(c):
        v=list(F())
        for i in range(2,1+v[1]):
            l[v[i]].append((v[i+1],v[0]))
            l[v[i+1]].append((v[i],v[0]))
    r=[[1e99]*(a+1) for _ in range(b)]
    for k in t.keys():        
        r[k[0]][k[1]]=0
        q=[(0,k[0],k[1])]
        while q:
            d,i,p=heapq.heappop(q)
            if(r[i][p]<d): continue
            for j,e in l[p]:
                if(r[i][j]>d+e*t[k]):
                    r[i][j]=d+e*t[k]
                    heapq.heappush(q,(r[i][j],i,j))
    m=1e99
    for j in range(a+1):
        m=min(m,max(r[i][j] for i in range(b)))
    if(m==1e99): m=-1
    print(f'Case #{z+1}: {m}')