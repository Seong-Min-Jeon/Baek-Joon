import sys,heapq
I=sys.stdin.readline
n,m=map(int,I().split())
l=[[] for _ in range(n+1)]
for _ in range(m):a,b,c=map(int,I().split());l[a].append((b,c));l[b].append((a,c))
a,b,c=map(int,I().split())
x,y=[],[]
for t in (a,b,c):
 r,v,k,q=[1e99]*(n+1),[-1]*(n+1),[0]*(n+1),[(0,t)];r[t]=0
 while q:
  d,p=heapq.heappop(q)
  if(k[p]): continue
  k[p]=1
  for i,e in l[p]:
   if(d+e<r[i]):r[i]=d+e;heapq.heappush(q,(d+e,i));v[i]=p
 x.append(r);y.append(v)
m,o=[x[0][i]+x[1][i]+x[2][i] for i in range(n+1)],set()
z=m.index(min(m))
for i in range(3):
 t,v=y[i],z
 while t[v]>0:o.add((t[v],v));v=t[v]
print(min(m),len(o))
for e in o:print(*e)