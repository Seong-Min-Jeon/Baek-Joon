n,m,a,b=map(int,input().split())
s=set()
for _ in range(m):
    x,y=map(int,input().split())
    for i in range(x,y+1): s.add(i)
q=[(0,0)]
v=[-1]*(n+1)
while q:
    p,c=q.pop(0)
    for i in (a,b):
        if(0<=p+i<=n and v[p+i]==-1 and p+i not in s):
            v[p+i]=c+1
            q.append((p+i,c+1))
print(v[-1])