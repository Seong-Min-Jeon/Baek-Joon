import sys,heapq
I=sys.stdin.readline
n,m,k=map(int,I().split())
l=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,I().split())
    f=1
    for i in range(len(l[a])):
        if(l[a][i][0]==b):
            l[a][i]=(b,min(c,l[a][i][1]))
            f=0
    if(f): l[a].append((b,c))
    f=1
    for i in range(len(l[b])):
        if(l[b][i][0]==a):
            l[b][i]=(a,min(c,l[b][i][1]))
            f=0
    if(f): l[b].append((a,c))
r=[[1e99]*(n+1) for _ in range(k+1)]
q=[(0,1,0)]
r[0][1]=0
while q:
    d,p,f=heapq.heappop(q)
    if(r[f][p]<d): continue
    for i,e in l[p]:
        if(f<k and d<r[f+1][i]): r[f+1][i]=d; heapq.heappush(q,(d,i,f+1))
        if(d+e<r[f][i]): r[f][i]=d+e; heapq.heappush(q,(d+e,i,f))
print(min(e[-1] for e in r))