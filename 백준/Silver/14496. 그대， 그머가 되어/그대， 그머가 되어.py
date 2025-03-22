import sys
I=sys.stdin.readline
a,b=map(int,I().split())
n,m=map(int,I().split())
l=[[] for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,I().split())
    l[x].append(y)
    l[y].append(x)
v=[-1]*(n+1)
q=[(a,0)]
v[a]=0
while q:
    p,c=q.pop(0)
    for e in l[p]:
        if(v[e]==-1):
            q.append((e,c+1))
            v[e]=c+1
print(v[b])