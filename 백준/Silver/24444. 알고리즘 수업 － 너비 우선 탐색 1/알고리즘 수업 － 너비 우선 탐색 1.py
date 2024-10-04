import sys
ip=sys.stdin.readline

def bfs(d:dict,s):
    v[s]=1
    q=[]
    q.append(s)
    c=1
    while(len(q)!=0):
        u=q[0]
        del q[0]
        for e in sorted(d.get(u,[])):
            if(v[e]==0):
                c+=1
                v[e]=c
                q.append(e)
    return v
a,b,c=map(int,ip().split())
v=[0 for _ in range(a+1)]
d={}
for _ in range(b):
    x,y=map(int,ip().split())
    if(x in d): d[x].append(y)
    else: d[x]=[y]
    if(y in d): d[y].append(x)
    else: d[y]=[x]
r=bfs(d,c)
del r[0]
for e in r:
    print(e)