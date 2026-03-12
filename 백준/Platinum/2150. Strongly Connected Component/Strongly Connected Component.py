import sys
I=sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m=map(int,I().split())
g=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,I().split())
    g[a].append(b)

d=[0]*(n+1)
f=[0]*(n+1)
s=[]
c=0
sn=0
r=[]

def dfs(x):
    global c,sn
    c+=1
    d[x]=c
    p=d[x]
    s.append(x)
    for y in g[x]:
        if d[y]==0:
            p=min(p,dfs(y))
        elif not f[y]:
            p=min(p,d[y])
    if p==d[x]:
        t=[]
        while 1:
            y=s.pop()
            f[y]=1
            t.append(y)
            if y==x: break
        t.sort()
        r.append(t)
        sn+=1
    return p

for i in range(1,n+1):
    if d[i]==0: dfs(i)

r.sort()
print(len(r))
for e in r:
    print(*e,-1)