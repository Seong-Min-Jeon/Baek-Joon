import heapq, sys
I=sys.stdin.readline
n,m=map(int,I().split())
d=[[] for _ in range(n)]
z=0
for _ in range(m):
    a,b,c=map(int,I().split())
    d[a-1].append((b-1,c))
    d[b-1].append((a-1,c))
    z+=c
s,t=map(int,I().split())
s,t=s-1,t-1
q=[(0,s,0)]
v=[[1e9,1e9] for _ in range(n)]
v[s][0],v[s][1]=0,0
while q:
    c,p,u=heapq.heappop(q)
    if(v[p][u]<c): continue
    for x,y in d[p]:
        if(v[x][u]>c+y): v[x][u]=c+y; heapq.heappush(q,(c+y,x,u))
        if(u==0 and v[x][1]>c): v[x][1]=c; heapq.heappush(q,(c,x,1))
print(z-v[t][1])