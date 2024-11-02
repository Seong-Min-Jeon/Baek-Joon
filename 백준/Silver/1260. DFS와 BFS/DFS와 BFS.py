import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline

def dfs(d,s):
    global o
    v[s]=o
    print(s, end=' ')
    o+=1
    if(s not in d): return
    for e in sorted(d[s]):
        if(v[e]==0): dfs(d,e)

def bfs(d,s):
    c=1
    w[s]=c
    print(s, end=' ')
    c+=1
    q=[s]
    while len(q)>0:
        a=q[0]
        del q[0]
        for e in sorted(d.get(a,[])):
            if(w[e]==0):
                w[e]=c
                print(e, end=' ')
                c+=1
                q.append(e)
        
a,b,c=map(int,ip().split())
v=[0 for _ in range(a+1)]
w=[0 for _ in range(a+1)]
d={}
for _ in range(b):
    x,y=map(int,ip().split())
    if(x in d): d[x].append(y)
    else: d[x]=[y]
    if(y in d): d[y].append(x)
    else: d[y]=[x]
o=1
dfs(d,c)
print()
bfs(d,c)