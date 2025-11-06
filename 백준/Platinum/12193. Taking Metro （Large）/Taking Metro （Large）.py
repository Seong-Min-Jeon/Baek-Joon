import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
for T in range(int(I())):
    I()
    l=[[]]
    o={}
    for k in range(1,int(I())+1):
        s,w=F()
        t=[[] for _ in range(s+1)]
        for i,e in enumerate(F()):
            t[i+1].append((k,i+2,e))
            t[i+2].append((k,i+1,e))
        l.append(t)
        o[k]=w
    m=[[[] for _ in range(1001)] for _ in range(1001)]
    s=set()
    for _ in range(int(I())):
        a,b,c,d,w=F()
        m[a][b].append((c,d,w))
        m[c][d].append((a,b,w))
        s.add((a,b))
        s.add((c,d))
    print(f"Case #{T+1}:")
    for _ in range(int(I())):
        a,b,x,y=F()
        r=[[1e99]*(1001) for _ in range(1001)]
        v=[[1e99]*(1001) for _ in range(1001)]
        r[a][b]=0
        q=[(0,0,a,b)]        
        while q:
            t,d,c,p=heapq.heappop(q)
            if(t==0 and r[c][p]<d): continue
            if(t==1 and v[c][p]<d): continue
            if(t==0):
                if(v[c][p]>d+o[c]):
                    v[c][p]=d+o[c]
                    heapq.heappush(q,(1,v[c][p],c,p))
                for i,j,e in m[c][p]:
                    if(r[i][j]>d+e):
                        r[i][j]=d+e
                        heapq.heappush(q,(0,r[i][j],i,j))
            if(t==1):
                for i,j,e in l[c][p]:
                    if((i,j) in s and r[i][j]>d+e):
                        r[i][j]=d+e
                        heapq.heappush(q,(0,d+e,i,j))
                    if(v[i][j]>d+e):
                        v[i][j]=d+e
                        heapq.heappush(q,(1,d+e,i,j))
        z=min(r[x][y],v[x][y])
        print(z if z!=1e99 else -1)