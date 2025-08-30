import sys,heapq
I=sys.stdin.readline;f=lambda:map(int,I().split());n,m,k=f()
l=[[] for _ in range(n+1)]
for _ in range(m):a,b,c=f();l[a].append((b,c))
r=[[1e99]*(k+1) for _ in range(n+1)];r[1][0]=0;q=[(0,1)]
while q:
 d,p=heapq.heappop(q)
 for i,e in l[p]:
  if(r[i][k]>d+e):r[i][k]=d+e;r[i].sort();heapq.heappush(q,(d+e,i))
for i in range(n):print(-1 if r[i+1][k-1]==1e99 else r[i+1][k-1])