import sys
ip=sys.stdin.readline

def bfs(d,s):
    v[s]=1
    q=[]
    q.append((s,0))
    while(len(q)!=0):
        u=q[0][0]
        c=q[0][1]
        del q[0]
        for e in sorted(d.get(u,[])):
            if(v[e]==0):
                v[e]=c+1
                q.append((e,c+1))

a,b=map(int,ip().split())
r=[0 for _ in range(a+1)]
r[0]=2**100
d={}
for _ in range(b):
    x,y=map(int,ip().split())
    if(x in d): d[x].append(y)
    else: d[x]=[y]
    if(y in d): d[y].append(x)
    else: d[y]=[x]
for i in range(1,len(r)):
    v=[0 for _ in range(a+1)]
    bfs(d,i)    
    r[i]=sum(v)-1
print(r.index(min(r)))