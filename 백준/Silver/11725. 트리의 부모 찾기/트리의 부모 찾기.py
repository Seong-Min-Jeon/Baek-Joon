import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline

def dfs(d,s,p):
    v[s]=p    
    if(s not in d): return
    for e in sorted(d[s]):
        if(v[e]==0): dfs(d,e,s)

a=int(ip())
v=[0 for _ in range(a+1)]
d={}
for _ in range(a-1):
    b,c=map(int,ip().split())
    if(b in d): d[b].append(c)
    else: d[b]=[c]
    if(c in d): d[c].append(b)
    else: d[c]=[b]
dfs(d,1,-1)
del v[0:2]
for e in v:
    print(e)