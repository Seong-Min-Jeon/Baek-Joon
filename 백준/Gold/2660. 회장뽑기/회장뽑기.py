import sys
I=sys.stdin.readline
n=int(I())
d=[[] for _ in range(n+1)]
while True:
    a,b=map(int,I().split())
    if(a<0): break
    d[a].append(b)
    d[b].append(a)
r=[]
m=1e9
for i in range(1,n+1):
    q=[(i,0)]
    v=[-1]*(n+1)
    v[i]=0
    while q:
        p,c=q.pop(0)
        for f in d[p]:
            if(v[f]==-1):
                q.append((f,c+1))
                v[f]=c+1
    if(max(v)<m):
        m=max(v)
        r.clear()
        r.append(i)
    elif(max(v)==m):
        r.append(i)
print(m,len(r))
print(*r)