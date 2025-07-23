import sys,heapq
I=sys.stdin.readline
n,m,s,g=map(int,I().split())
l=[[] for _ in range(n+1)]
for _ in range(m):a,b,c=map(int,I().split());l[a].append((b,c));l[b].append((a,c))
r=[1e99]*(n+1);v=[[] for _ in range(n+1)];q=[(0,s)];r[s]=0
while q:
 d,p=heapq.heappop(q)
 if(r[p]<d):continue
 for i,e in l[p]:
  if(d+e<r[i]):r[i]=d+e;v[i].clear();v[i].append(p);heapq.heappush(q,(d+e,i))
  elif(d+e==r[i]):v[i].append(p)
r=set();q=[g]
while q:
 a=q.pop();r.add(a)
 for e in v[a]:q.append(e)
print(len(r));print(*sorted(list(r)))