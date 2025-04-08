import sys
sys.setrecursionlimit(10**6)
I=sys.stdin.readline
n=int(I())
l=[[] for _ in range(n+1)]
for _ in range(n-1):
    x,y=map(int,I().split())
    l[x].append(y)
    l[y].append(x)
r=[0]*(n+1)
v=[0]*(n+1)
v[1]=1
def dfs(s):
    if(s!=1 and len(l[s])==1): r[s]=2; return
    for e in l[s]:
        if(v[e]==0):
            v[e]=1
            dfs(e)
            f=0
            for k in l[e]:
                if(r[k]==2): f=1
            if(f): r[e]=1
            else: r[e]=2
dfs(1)
f=0
for k in l[1]:
    if(r[k]==2): f=1
if(f): r[1]=1
else: r[1]=2
for e in r[1:]:
    if(e==1): print('donggggas')
    else: print('uppercut')