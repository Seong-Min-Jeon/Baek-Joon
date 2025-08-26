import sys,heapq
I=sys.stdin.readline
f=lambda:map(int,I().split())
n,m=f()
l=[[] for _ in range(n+1)]
for _ in range(m):
    i,j,d=f()
    l[i].append((j,d))
    l[j].append((i,d))
s,z=f()
r=[{1e20:1e20} for _ in range(n+1)]
r[s][0]=0
q=[(0,s,0)]
while q:
    d,p,x=heapq.heappop(q)
    if(r[p].get(x,1e20)<d): continue
    for i,e in l[p]:
        if(e>x and r[i].get(e,1e20)>d+e):
            r[i][e]=d+e
            q.append((d+e,i,e))
m=min([e for e in r[z].values()])
if(m==1e20): print('DIGESTA')
else: print(m)