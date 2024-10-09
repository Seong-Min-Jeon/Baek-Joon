import sys
ip=sys.stdin.readline

def bfs(d:dict, s):
    v[s]=1
    q=[s]
    while len(q)>0:
        a=q[0]
        del q[0]
        c.add(a)
        for e in d.get(a,[]):
            if(v[e]==0):
                v[e]=1
                q.append(e)        

n=int(ip())
v=[0 for _ in range(n+1)]
c=set()
d={}
for _ in range(int(ip())):
    a,b=map(int,ip().split())
    if(a in d): d[a].append(b)
    else: d[a]=[b]
    if(b in d): d[b].append(a)
    else: d[b]=[a]
bfs(d,1)
print(len(c)-1)