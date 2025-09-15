import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m=F()
l=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=F()
    l[a].append((b,c))
t=[]
k=0
for _ in range(int(I())):
    a,b,c=F()
    k=max(k,c)
    t.append((a,b,c))
r=[[[1e99]*(k+1) for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    q=[(0,i)]
    # r[i][i][0]=0
    while q:
        d,p=heapq.heappop(q)
        if(r[i][p][k]<d): continue
        for j,e in l[p]:
            if(r[i][j][k]>d+e):
                r[i][j][k]=d+e
                r[i][j].sort()
                heapq.heappush(q,(d+e,j))
for i,p,k in t:
    print(r[i][p][k-1] if r[i][p][k-1]!=1e99 else -1)