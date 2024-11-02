import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline

def dfs(d,s):
    v[s]=1
    if(s not in d): return
    for e in sorted(d[s]):
        if(v[e]==0): dfs(d,e)

a,b=map(int,ip().split())
v=[0 for _ in range(a+1)]
d={}
for _ in range(b):
    x,y=map(int,ip().split())
    if(x in d): d[x].append(y)
    else: d[x]=[y]
    if(y in d): d[y].append(x)
    else: d[y]=[x]
c=0
for i in range(1,a+1):
    if(v[i]==0):
        dfs(d,i)
        c+=1
print(c)
